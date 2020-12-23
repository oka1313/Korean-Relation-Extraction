import pickle
import sys
import csv

csv.field_size_limit(sys.maxsize)

input_csv = sys.argv[1]
input_tsv = sys.argv[2]

#with open("./ko_re_data/relation_dict_50.pkl", 'rb') as f:
#    rel_ind = pickle.load(f)

sentence_data = list(csv.reader(open(input_csv, 'r', encoding='utf-8')))
f = open(input_tsv, 'w', encoding='utf-8', newline='')
wr = csv.writer(f, delimiter='\t')

# csvwriter = csv.writer(open('../../data/kaist/test_65.csv', 'w', encoding='utf-8'))

# rel_ind = ["/people/deceased_person/place_of_death", "/people/person/place_of_birth", "/people/person/place_lived", "per:origin"]

print_list = []
remove_count = 0
for line in sentence_data:
    sentence = line[0]
    relation = line[1]
    gsid = ""#line[2]
    parid = ""#line[3]
    docid = ""#line[4]

    #if relation not in rel_ind:
    #    remove_count = remove_count + 1
    #    continue

    if sentence.find("<e1>") == -1 or sentence.find("<e2>") == -1:
        continue

    e1 = sentence[sentence.find("<e1>") + 4:sentence.find("</e1>")]
    e2 = sentence[sentence.find("<e2>") + 4:sentence.find("</e2>")]

    sentence = sentence.replace("  ", " ")
    sentence = sentence.replace("  ", " ")

    sentence = sentence.replace("[", "")
    sentence = sentence.replace("]", "")

    # sentence = sentence.replace("<e1>", "")
    # sentence = sentence.replace("<e2>", "")
    # sentence = sentence.replace("</e1>", "")
    # sentence = sentence.replace("</e2>", "")

    # print(relation, e1, e2, sentence, gsid, parid, docid)

    wr.writerow([relation, e1, e2, sentence, gsid, parid, docid])
    # wr.writerow(['NA', e1, e2, sentence, gsid, parid, docid])
    # csvwriter.writerow([sentence, relation])

print(len(sentence_data))
print(remove_count)
f.close()
