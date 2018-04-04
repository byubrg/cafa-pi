import pandas as pd
import numpy as np

def trim_go_id(go_id):
    return go_id.replace("GO:", "")

def df_from_fasta(path, taxon_id=None):
    names = []
    seqs = []
    seq = ""
    with open(path, "r") as infile:
        for line in infile:
            line = line.strip()
            if ">" in line:
                # This means we have a new sequence
                names.append(line[1:])
                if seq != "":
                    seqs.append(seq)
                    seq = ""
            else:
                seq += line
        # Add the last sequence
        seqs.append(seq)
    df = pd.DataFrame({"CAFA_ID": names, "Sequence": seqs})
    if taxon_id is None:
        df["Taxon_ID"] = path.split("/")[-1].split(".")[0]
    else:
        df["Taxon_ID"] = taxon_id
    return df

def df_from_tsv(path):
    df = pd.read_table(path, header=None, names=["CAFA_ID", "GO_ID", "Ontology"])
    df["GO_ID"] = df["GO_ID"].apply(trim_go_id)
    return df

def reorder_cols(merged_df):
    return merged_df[["CAFA_ID", "Taxon_ID", "Sequence", "GO_ID", "Ontology"]]

def join(fasta_df, tsv_df):
    df = fasta_df.merge(tsv_df, on="CAFA_ID", how="inner")
    return reorder_cols(df)

def load_all():
    fasta = df_from_fasta("./data/raw/CAFA3_training_data/uniprot_sprot_exp.fasta")
    tsv = df_from_tsv("./data/raw/CAFA3_training_data/uniprot_sprot_exp.txt")
    return join(fasta, tsv)

if __name__ == "__main__":
    df = load_all()
    # print(df)
    df.to_csv("./data/parsed/cafa3.csv", index=False)