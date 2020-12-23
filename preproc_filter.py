import pickle
import sys
import csv

csv.field_size_limit(sys.maxsize)

input_csv = sys.argv[1]
input_tsv = sys.argv[2]

#with open("./ko_re_data/relation_dict_50.pkl", 'rb') as f:
#    rel_ind = pickle.load(f)

sentence_data = list(csv.reader(open(input_csv, 'r', encoding='utf-8'), delimiter='\t'))
f = open(input_tsv, 'w', encoding='utf-8', newline='')
wr = csv.writer(f, delimiter='\t')

# csvwriter = csv.writer(open('../../data/kaist/test_65.csv', 'w', encoding='utf-8'))

# rel_ind = ["/people/deceased_person/place_of_death", "/people/person/place_of_birth", "/people/person/place_lived", "per:origin"]

print_list = []
remove_count = 0
for line in sentence_data:
    relation = line[0]
    e1 = line[1]
    e2 = line[2]
    sentence = line[3]

    wr.writerow(["True", e1, e2, sentence, "", "", ""])

print(len(sentence_data))
print(remove_count)
f.close()
