"""
Add a header & clean some bad lines from the training data.
"""

import numpy as np

in_path = "./data_acquisition/all_training_data_final.csv"
out_path = "./data/parsed/training.csv"
columns = [
    "CAFA_ID",
    "Sequence",
    "Organism",
    "GO_ID",
]
AMINOS = set('ACDEFGHIKLMNPQRSTVWY')

with open(in_path, "r") as infile:
    with open(out_path, "w") as outfile:
        outfile.write(",".join(columns) + "\n")
        for line in infile:
            items = line.rstrip('\n').split(',')
            if len(items) != len(columns):
                continue
            # Toss it if there's no GO ID
            if items[3] == "":
                continue
            # Remove stuff that looks wrong...
            items[1] = items[1].replace("*", "").replace("GOISM", "").replace("GO", "").replace("ABC", "")
            # Replace stuff that could be OK based on https://www.ddbj.nig.ac.jp/ddbj/code-e.html
            items[1] = items[1].replace("B", "N").replace("Z", "E").replace("U", "C").replace("O", "K").replace("J", "L")
            # According to https://www.ncbi.nlm.nih.gov/books/NBK21581/, L, S, K, & E are most common,
            # so we'll just replace Xs with one of them at random.
            # It would probably actually be better to set probabilities over all aminos based on
            # abundance in our target data.
            items[1] = items[1].replace("X", np.random.choice(list("LSKE")))
            # If we don't have any sequence left, we'll get rid of the row.
            if len(items[1]) < 10:
                continue
            # Rename it if there's no name
            if items[0] == "":
                items[0] == "Unknown"
            if len(set(items[1]) - AMINOS) != 0:
                print(set(items[1]) - AMINOS)
            outfile.write(",".join(items) + "\n")