import csv

sentence_data = list(csv.reader(open("ko_re_data/filtered_sentence.csv", 'r', encoding='utf-8')))
wr = csv.writer(open("ko_re_data/filtered_sentence_True.csv", 'w', encoding='utf-8', newline=''))

for line in sentence_data:
    sentence = line[0]
    relation = line[1]

    if relation == "True":
        wr.writerow([sentence, relation])

