import numpy as np
import pandas as pd

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

def read_csv(path):
    print(path)

    
if __name__ == "__main__":
    print(one_hot("A"))
    print(one_hot("M"))
    print(one_hot_seq("ACDE", 6))
    print(read_csv('cafa-pi/example/train.csv'))