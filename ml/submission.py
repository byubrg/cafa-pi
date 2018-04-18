import sys

# Filename Format
def create_outFile_name(model, taxon, go):
    outFile_name = "BYU-BRG_" + model + "_" + taxon + "_" + go + ".txt"
    return outFile_name

# File Header
def create_header(model, keyword):
    header = "AUTHOR\tBYU-BRG\nMODEL\t" + model + "\nKEYWORDS\t" + keyword + "\n"
    return header

# Create dictionary
def create_dictionary(file):
    predictions_dict = {}
    for line in file:
        line = line.strip()
        column = line.split("\t")
        cafa = column[0]
        prob = column[1]
        predictions_dict[cafa] = prob
    return predictions_dict

# Predictions Format {cafa-id: probability}
def format_predictions(my_dict):
    prediction = ""
    for cafa in my_dict:
        prediction += cafa + "\t" + my_dict[cafa] + "\n"
    return prediction


if __name__ == "__main__":
    model_no = sys.argv[2]
    taxon_id = sys.argv[3]
    go_id = sys.argv[4]
    key_words = sys.argv[5]

    prediction_file = open(sys.argv[1], 'r')
    predictions = create_dictionary(prediction_file)
    prediction_file.close()

    outFile = open(create_outFile_name(model_no, taxon_id, go_id),'w')
    outFile.write(create_header(model_no, key_words))
    outFile.write(format_predictions(predictions))
    outFile.write("END")
    outFile.close()
