# pylint: disable=E1101

import numpy as np
import pandas as pd
import h5py
import os

AMINOS = 'ACDEFGHIKLMNPQRSTVWY'

def one_hot(amino):
    encoding = [1.0 if amino == x else 0.0 for x in AMINOS]
    return encoding

def one_hot_seq(seq, max_size=0):
    if max_size < 1:
        max_size = len(seq)
    
    temp = []
    for i in range(max_size):
        if i < len(seq):
            temp.append(one_hot(seq[i]))
        else:
            temp.append([0.0] * len(AMINOS))
    return np.array(temp)

def load_data_padded(path):
    """
    Load data and encode the sequences and targets as arrays of 1.0s and 0.0s.
    @param path: the file path to the csv to be read in.  Must have columns
        ["CAFA_ID", "Sequence", "GO_ID"].
    @return a tuple: (data_encodings, target_encodings)
    """
    df = pd.read_csv(path)
    seen = set()
    seqs = []
    for _, row in df.iterrows():
        seq = row['Sequence']
        if seq not in seen:
            seen.add(seq)
            seqs.append(seq)
    max_len = max([len(seq) for seq in seqs])
    data_encodings = np.array([one_hot_seq(seq, max_len) for seq in seqs])
    targets = np.array(get_labels(path))
    return data_encodings, targets

def load_data_discrete(path):
    """
    Loads the data, similar to `load_data()`, but outputs targets as discrete
    values (i.e. "cat", "dad" instead of [0, 1], [1, 0]).
    """
    df = pd.read_csv(path)
    seqs = [row['Sequence'] for _, row in df.iterrows()]
    max_len = max([len(seq) for seq in seqs])
    data_encodings = [one_hot_seq(seq, max_len) for seq in seqs]
    targets = [row['GO_ID'] for _, row in df.iterrows()]
    return data_encodings, targets

def encode_functions(df, id_col="id", function_col="go_id"):
    functions = sorted(list(set(df[function_col])))
    func_dict = {func: i for i, func in enumerate(functions)}
    ids = sorted(list(set(df[id_col])))
    id_dict = {id_: i for i, id_ in enumerate(ids)}
    encodings = np.zeros((len(ids), len(functions)))
    for i, row in df.iterrows():
        encodings[id_dict[row[id_col]], func_dict[row[function_col]]] = 1.0
    return encodings

def go_id_onehot(file_name, id_column="CAFA_ID", go_id_column="GO_ID"):
    go_ids = []
    with open(file_name) as inFile:
        go_id_map = {}
        headers = inFile.readline().rstrip('\n').split(',')
        go_id_index = headers.index(go_id_column)
        id_index = headers.index(id_column)
        for line in inFile:
            data = line.rstrip('\n').split(',')
            go_id = data[go_id_index]
            go_id_map.setdefault(data[id_index], []).append(go_id)
            if go_id not in go_ids:
                go_ids.append(go_id)
    one_hot = {}
    for id in go_id_map.keys():
        hot_map = []
        for i in range(len(go_ids)):
            if go_ids[i] in go_id_map[id]:
                hot_map.append(1.0)
            else:
                hot_map.append(0.0)
        one_hot[id] = hot_map
    return [go_ids, one_hot]

def get_labels(file_name):
    one_hot = go_id_onehot(file_name)[1]
    labels = []
    for cafa_id in one_hot:
        labels.append(np.array(one_hot[cafa_id]))
    return labels

def shuffle_unison(data, labels):
    assert len(data) == len(labels), \
        "Data and Labels different sizes.  {} != {}".format(len(data), len(labels))
    p = np.random.permutation(len(data))
    return data[p], labels[p]

def get_batch(data, labels, batch_size=25, shuffle=True):
    indices = np.random.choice(len(data), batch_size, replace=False)
    return data[indices], labels[indices]
    # if shuffle:
    #     data, labels = shuffle_unison(data, labels)
    # return data[:batch_size], labels[:batch_size]

class H5pyDao:
    def __init__(self, hdf5_path: str, percent_test: int=10, csv_path: str=None, chunk_size: int=1000):
        self.__path = hdf5_path
        self.__percent_test = percent_test
        self.__chunk_size = chunk_size

        if csv_path:
            self.load_data(csv_path, hdf5_path)
        assert os.path.isfile(hdf5_path), "{}: File does not exist.".format(hdf5_path)

        with h5py.File(hdf5_path) as f:
            num_attributes = f["attributes"].shape[0]
            num_labels = f["labels"].shape[0]
            assert num_attributes == num_labels, "Data and Labels different sizes.  {} != {}".format(num_attributes, num_labels)
            self.num_samples = num_attributes
            self.num_test = int(num_attributes * (percent_test/100))
            self.num_train = self.num_samples - self.num_test
            self.test_indices = np.random.choice(self.num_samples, self.num_test, replace=False)

    def cleanup(self):
        os.remove(self.__path)

    def get_batch_train(self, batch_size: int=25):
        repeat = True
        indices = np.random.choice(self.num_samples, batch_size, replace=False)
        while repeat:
            repeat = False
            for i in range(len(indices)):
                if indices[i] in self.test_indices:
                    repeat = True
                    indices[i] = np.random.random_integers(self.num_samples)

        with h5py.File(self.__path) as f:
            return f["attributes"][()][indices], f["labels"][()][indices]

    def get_batch_test(self, batch_size: int=25):
        indices = np.random.permutation(self.test_indices)[0:25]
        with h5py.File(self.__path) as f:
            return f["attributes"][()][indices], f["labels"][()][indices]

    def load_data(self, in_file, out_file):
        seen = set()
        seqs = []
        for chunk in pd.read_csv(in_file, chunksize=self.__chunk_size):
            for _, row in chunk.iterrows():
                seq = row['Sequence']
                if seq not in seen:
                    seen.add(seq)
                    seqs.append(seq)
        max_len = max([len(seq) for seq in seqs])
        targets = np.array(get_labels(in_file))
        with h5py.File(out_file, "w") as f:
            f.create_dataset('attributes', shape=(0, max_len, 20), maxshape=(None, None, None))
            f.create_dataset('labels', data=targets)
        i = 0
        while i < len(seqs):
            if i + self.__chunk_size < len(seqs):
                data_encodings = np.array([one_hot_seq(seq, max_len) for seq in seqs[i:i + self.__chunk_size]])
            else:
                data_encodings = np.array([one_hot_seq(seq, max_len) for seq in seqs[i:]])
            with h5py.File(out_file, "a") as f:
                f["attributes"].resize((f["attributes"].shape[0] + data_encodings.shape[0]), axis=0)
                f["attributes"][-data_encodings.shape[0]:] = data_encodings
            i += self.__chunk_size


if __name__ == "__main__":
    df = pd.DataFrame({
        "id": [1, 1, 2, 2, 2, 3, 4, 5, 5], 
        "go_id": ["a", "b", "c", "d", "a", "d", "e", "a", "e"]
    })
    print(encode_functions(df))