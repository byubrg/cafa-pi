#! /anaconda/bin/python3
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

def get_labels(one_hot):
    labels = []
    for cafa_id in one_hot:
        labels.append(one_hot[cafa_id])
    return labels

print(get_labels(go_id_onehot("/Users/kimballhill/BYUBRG/cafa-pi/data/example/train_fake.csv")[1]))