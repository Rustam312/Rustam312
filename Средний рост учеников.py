url = '/Users/rustam/Desktop/dataset_3380_5.txt'


with open(url, 'r') as f:
    p = f.readlines()
    d = {a: [] for a in range(1, 11 + 1)}
    p = [p[id].replace('\n', '').split('\t') for id, el in enumerate(p)]

    p=[[int(i[0]),i[1], int(i[2])]  for i in p]
    for c in p:
        if c[0] in d:
            d[c[0]].append(c[2])
        else:
            d[c[0]] = [c[2]]
    for key in sorted(d.keys()):
        if d[key]:
            print(key, sum(d[key])/float(len(d[key])))
        else:
            print(key, '-')