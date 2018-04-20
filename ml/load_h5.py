import h5py
from .embeddings import one_hot_seq, AMINOS
from time import time
import numpy as np

def unique_index_dict(path: str, column: str, sep: str=","):
    d = {}
    with open(path, "r") as infile:
        column_index = get_column_index(infile, column)
        current_ix = 0
        for line in infile:
            seq = list_from_line(line)[column_index]
            if seq in d:
                continue
            d[seq] = current_ix
            current_ix += 1
    return d

def get_column_index(infile, column: str, sep: str=","):
    """
    Get the header as a list
    """
    return list_from_line(infile.readline()).index(column)

def list_from_line(line: str, sep: str=','):
    return line.rstrip('\n').split(sep)

def max_seq_length(path: str, column: str="Sequence"):
    m = 0
    with open(path, "r") as infile:
        col_ix = get_column_index(infile, column)
        for line in infile:
            seq = list_from_line(line)[col_ix]
            l = len(seq)
            m = max([l, m])
    return m

def store_sequence_embeddings(sequences: dict, h5_path: str, max_len: int=None):
    print(f"Storing sequences in {h5_path}")
    start_time = time()
    # We will be creating a N_seqs x Max-Length x N_aminos hdf5 dataset
    # Get n_seqs
    n_seqs = len(sequences)
    # Get maxlength
    if max_len == None:
        max_len = max([len(seq) for seq in sequences])
    # Get n_aminos
    n_aminos = len(AMINOS)
    # Make the dataset
    f = h5py.File(h5_path, "a")
    try:
        del f['embeddings/sequence']
    except KeyError:
        pass
    seq_embeddings = f.require_dataset("embeddings/sequence", (n_seqs, max_len, n_aminos), "f")
    # Fill the dataset
    for i, (seq, index) in enumerate(sequences.items()):
        if len(seq) > max_len:
            seq = seq[:max_len]
        embed = one_hot_seq(seq, max_size=max_len)
        seq_embeddings[index] = embed
        if i % 100 == 0:
            print(f"Saved {i+1}/{n_seqs} sequences", end="\r")
    print(f"\nFinished. Stored {n_seqs} sequences in {time()-start_time} seconds.")
    f.close()

def store_binary_labels(csv_path: str, h5_path: str, ids_of_interest: set, sequences: dict=None, dataset_name=""):
    dataset_name = "/".join(["labels/binary", dataset_name])
    if sequences == None:
        sequences = unique_index_dict(csv_path, "Sequence")
    # Get a list of binary labels
    with open(csv_path, "r") as infile:
        labels = np.zeros((len(sequences), 2))
        # Set everything to [0, 1], and then set interesting ones to [1, 0]
        labels[:, 1] = 1.0
        header = infile.readline().rstrip('\n').split(',')
        seq_col = header.index("Sequence")
        id_col = header.index("GO_ID")
        for line in infile:
            items = list_from_line(line)
            seq = items[seq_col]
            go_id = items[id_col]
            if go_id in ids_of_interest:
                seq_ix = sequences[seq]
                labels[seq_ix] = [1.0, 0.0]
    # Make an HDF5 dataset and store the stuff
    f = h5py.File(h5_path, "a")
    try:
        del f[dataset_name]
    except KeyError:
        pass
    f[dataset_name] = labels
    f.close()

def store_multi_hot_labels(csv_path: str, h5_path: str):
    print(f"Storing multi-hot labels in {h5_path}")
    start_time = time()
    # Get a dict - {GO_ID: index, "GO:0080044": 0, ...}
    go_id_ixs = unique_index_dict(csv_path, "GO_ID")
    # Get the sequence -> index dict
    seq_ixs = unique_index_dict(csv_path, "Sequence")
    # Make an HDF5 dataset of shape N_Seqs X N_GO_IDs
    f = h5py.File(h5_path, "a")
    try:
        del f['labels/multi_hot']
    except KeyError:
        pass
    multi_hot = f.require_dataset("labels/multi_hot", (len(seq_ixs), len(go_id_ixs)), "f")
    # Fill it up
    with open(csv_path, "r") as infile:
        header = infile.readline().rstrip('\n').split(',')
        seq_col = header.index("Sequence")
        id_col = header.index("GO_ID")
        for i, line in enumerate(infile):
            items = list_from_line(line)
            seq_ix = seq_ixs[items[seq_col]]
            go_id_ix = go_id_ixs[items[id_col]]
            multi_hot[seq_ix, go_id_ix] = 1.0
            if i % 100 == 0:
                print(f"Recorded {i+1} labels", end="\r")
    print(f"\nFinished. Stored {i} labels in {time()-start_time} seconds.")
    f.close()


if __name__ == "__main__":
    csv_path = "./data_acquisition/all_training_data_final.csv"
    h5_path = "./data/parsed/all_train.h5"
    seq_ixs = unique_index_dict(csv_path, "Sequence")
    max_len = max_seq_length(csv_path)
    store_sequence_embeddings(seq_ixs, h5_path)
    store_binary_labels(csv_path, h5_path, {"0005634"})
    store_multi_hot_labels(csv_path, h5_path)