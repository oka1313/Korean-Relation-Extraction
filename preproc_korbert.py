import sys
import csv

f = open('./ko_re_data/train.tsv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f, delimiter='\t')

f = open('./ko_re_data/train_ds_morp_tagged.tsv', 'r', encoding='utf-8')
rdr = csv.reader(f, delimiter='\t')
first_line = 0
for line in rdr:
    relation = line[0]
    subject = line[1]
    object = line[2]
    sentence = line[3].strip()
    sentence = sentence.replace('<e1>', '処/SH')
    sentence = sentence.replace('<e2>', 'ṯ/SW')
    sentence = sentence.replace('</e1>', '叙/SH')
    sentence = sentence.replace('</e2>', 'ŏ/SW')
    sentence = sentence.replace('_', ' ')
                                            
    wr.writerow([relation, subject, object, sentence])

