import pickle
import sys
import csv

input_csv = sys.argv[1]
input_tsv = sys.argv[2]

#with open("./ko_re_data/relation_dict_50.pkl", 'rb') as f:
#    rel_ind = pickle.load(f)

sentence_data = list(csv.reader(open(input_csv, 'r', encoding='utf-8')))
f = open(input_tsv, 'w', encoding='utf-8', newline='')
wr = csv.writer(f)

# csvwriter = csv.writer(open('../../data/kaist/test_65.csv', 'w', encoding='utf-8'))

rel_ind = ["/people/deceased_person/place_of_death", "/people/person/place_of_birth", "/people/person/place_lived", "per:origin"]

print_list = []
remove_count = 0
for line in sentence_data:
    sentence = line[0]
    relation = line[1]
    gsid = ""#line[2]
    parid = ""#line[3]
    docid = ""#line[4]

    if relation not in rel_ind:
        remove_count = remove_count + 1
        continue

    wr.writerow([sentence, relation, "", "", ""])

print(len(sentence_data))
print(remove_count)
f.close()
