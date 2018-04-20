import h5py
import numpy as np

class HDF5TargetDao(object):
    def __init__(self, h5_path:str):
        f = h5py.File(h5_path, "r")
        self.data = f['embeddings/sequence']
        self.n = self.data.shape[0]

class HDF5Dao(object):
    def __init__(self, h5_path: str, label_type: str="binary", pct_test: float=0.1):
        f = h5py.File(h5_path, "r")
        self.data = f['embeddings/sequence']
        self.n = self.data.shape[0]
        self.labels = f[f'labels/{label_type}']
        self.train_test_split(pct_test)
        self.__n_train_retrieved = 0

    def train_test_split(self, pct_test):
        n_test = int(pct_test * self.n)
        indices = np.array(range(self.n))
        np.random.shuffle(indices)
        self.test_indices = indices[:n_test]
        self.train_indices = indices[n_test:]

    def __batch(self, n:int, test_or_train:str):
        if test_or_train == "test":
            ixs = self.test_indices
        else:
            ixs = self.train_indices
        batch_ixs = sorted(np.random.choice(ixs, size=n, replace=False))
        x, y = self.data[batch_ixs,:,:], self.labels[batch_ixs]
        return x, y

    def get_batch_train(self, size=25):
        self.__n_train_retrieved += size
        return self.__batch(size, "train")

    def get_batch_test(self, size=25):
        return self.__batch(size, "test")

    @property
    def epochs(self):
        return self.__n_train_retrieved / self.n

if __name__ == "__main__":
    h5_path = "./data/parsed/cafa3/test.h5"
    dao = HDF5Dao(h5_path, label_type="multi_hot")
    for _ in range(100):
        x, y = dao.get_batch_train(100)
    print(dao.epochs)