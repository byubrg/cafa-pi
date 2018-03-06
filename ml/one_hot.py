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
    pass

def encode_functions(df, id_col="id", function_col="go_id"):
    functions = sorted(list(set(df[function_col])))
    func_dict = {func: i for i, func in enumerate(functions)}
    ids = sorted(list(set(df[id_col])))
    id_dict = {id_: i for i, id_ in enumerate(ids)}
    encodings = np.zeros((len(ids), len(functions)))
    for i, row in df.iterrows():
        encodings[id_dict[row[id_col]], func_dict[row[function_col]]] = 1.0
    return encodings
    
if __name__ == "__main__":
    df = pd.DataFrame({
        "id": [1, 1, 2, 2, 2, 3, 4, 5, 5], 
        "go_id": ["a", "b", "c", "d", "a", "d", "e", "a", "e"]
    })
    print(encode_functions(df))