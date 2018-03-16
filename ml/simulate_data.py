import pandas as pd
import random
from .embeddings import AMINOS

def generate_protein(min_len=25, max_len=50, insert=""):
    """
    @param insert: A string to insert into the generated protein.
        May be a string or list of strings.  If a list, the multiple
        strings are not guaranteed to not overlap.
    """
    length = random.randint(min_len, max_len)
    generated = "".join(random.choice(AMINOS) for _ in range(length))
    if isinstance(insert, str):
        insert = [insert]
    for x in insert:
        for char in x:
            assert char in AMINOS, \
                "Couldn't insert `{x}`. Character `{char}` is not a valid amino acid.".format(x=x, char=char)
        generated = insert_string(generated, x)
    return generated

def generate_proteins(num, min_len=25, max_len=50, insert=""):
    """
    Like `generate_protein()`, but generates a list of proteins.
    """
    return [generate_protein(min_len, max_len, insert) for _ in range(num)]

def insert_string(seq, insert):
    insert_ix = random.randint(0, len(seq) - len(insert))
    return seq[:insert_ix] + insert + seq[insert_ix+len(insert):]

def generate_ids(proteins):
    ids = []
    unique_ids = {}
    cur_id = 1
    for protein in proteins:
        if protein in unique_ids:
            ids.append(unique_ids[protein])
        else:
            ids.append(cur_id)
            unique_ids[protein] = cur_id
            cur_id += 1
    return ids

def generate_dataframe(seq1="KITTEN", name1="cat", seq2="DADDY", name2="dad", num_each=10, min_len=25, max_len=50):
    first = generate_proteins(num_each, min_len, max_len, seq1)
    second = generate_proteins(num_each, min_len, max_len, seq2)
    both = generate_proteins(num_each, min_len, max_len, [seq1, seq2])
    neither = generate_proteins(num_each, min_len, max_len, "")
    proteins = first + second + both + both + neither
    labels = [name1] * num_each + [name2] * num_each + \
             [name1] * num_each + [name2] * num_each + [""] * num_each
    cafa_ids = generate_ids(proteins)
    df = pd.DataFrame({"CAFA_ID": cafa_ids, "GO_ID": labels, "Sequence": proteins})
    df["Taxon_ID"] = "simulated"
    df = df.sort_values(by=["CAFA_ID", "GO_ID"])
    df = df[["CAFA_ID", "Taxon_ID", "Sequence", "GO_ID"]]
    return df

if __name__ == "__main__":
    # Set seed so we get the same data each time.
    random.seed(0)
    seq1 = "KITTEN"
    name1 = "cat"
    seq2 = "DADDY"
    name2 = "dad"
    num_each = 1000
    min_len = 25
    max_len = 500
    df = generate_dataframe(seq1, name1, seq2, name2, num_each, min_len, max_len)
    df.to_csv("./data/example/train_simulated.csv", index=False)