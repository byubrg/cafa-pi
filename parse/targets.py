import pandas as pd
import os.path
from cafa3 import df_from_fasta

def make_path(taxon):
    return "./data/large/targetFiles/target.{}.fasta".format(taxon)

if __name__ == "__main__":
    taxa = ["208963", "237561"]
    paths = [make_path(taxon) for taxon in taxa]
    for taxon in taxa:
        if not os.path.isfile(make_path(taxon)):
            raise FileNotFoundError(
                "Couldn't find the training data.  "
                "Make sure you're running this script from the "
                "project root, and if that doesn't work, "
                "try running `bash data_acquisition/Scripts/"
                "download_test_data.sh`.")
    for taxon, path in zip(taxa, paths):
        df = df_from_fasta(path, taxon_id=taxon)
        df["NCBI_Locus_Tag"] = df.apply(
            lambda row: row["CAFA_ID"].split(" ")[-1], axis=1)
        df["CAFA_ID"] = df.apply(
            lambda row: row["CAFA_ID"].split(" ")[0], axis=1)
        df = df[["CAFA_ID", "Taxon_ID", "Sequence", "NCBI_Locus_Tag"]]
        df.to_csv("./data/parsed/target.{}.csv".format(taxon), index=False)