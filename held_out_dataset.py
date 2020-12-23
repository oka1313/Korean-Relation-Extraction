import csv
import random

train_original = "ko_re_data/train_filter_all.tsv"

train_tsv = "ko_re_data/train_filter.tsv"
dev_tsv = "ko_re_data/dev_filter.tsv"
test_tsv = "ko_re_data/test_filter.tsv"

f = open(train_original, 'r', encoding='utf-8')
sentence_data = list(csv.reader(f, delimiter='\t'))
train_sentence_set = []
for line in sentence_data:
    relation = line[0]
    subject = line[1]
    object = line[2]
    sentence = line[3]
    train_sentence_set.append([relation, subject, object, sentence])

f.close()

print(len(train_sentence_set))

random.shuffle(train_sentence_set)

total_len = len(train_sentence_set)
unit_len = total_len // 10

print(unit_len)

new_train_sentence_set = train_sentence_set[:unit_len * 8]
dev_sentence_set = train_sentence_set[unit_len * 8:unit_len * 9]
test_sentence_set = train_sentence_set[unit_len * 9:]

print(len(new_train_sentence_set), len(dev_sentence_set), len(test_sentence_set))


f = open(train_tsv, 'w', encoding='utf-8', newline='')
wr = csv.writer(f, delimiter='\t')
for line in new_train_sentence_set:
    wr.writerow(line)

f.close()


f = open(dev_tsv, 'w', encoding='utf-8', newline='')
wr = csv.writer(f, delimiter='\t')
for line in dev_sentence_set:
    wr.writerow(line)

f.close()

f = open(test_tsv, 'w', encoding='utf-8', newline='')
wr = csv.writer(f, delimiter='\t')
for line in test_sentence_set:
    wr.writerow(line)

f.close()