# Not-A-Relation Filtering using BERT Fine-tuning

## Introduction
It is based on [BERT](https://github.com/google-research/bert) model. 
<br>We use "BERT-Base, Multilingual Cased" model for Korean.
<br>We share training/test data, script, and a little modified source code in this repository.
<br>You can download a [BERT](https://github.com/google-research/bert) and [MODEL](https://storage.googleapis.com/bert_models/2018_11_23/multi_cased_L-12_H-768_A-12.zip), then easily combine to adjust a Korean RE model.

## How to use
Train: ``sentence_classifier.sh``
<br>&nbsp;BERT_BASE_DIR: BERT Language Model, ``multi_cased_L-12_H-768_A-12``
<br>&nbsp;KORE_DIR: Dataset path
<br>&nbsp;TRAINED_CLASSIFIER: Path to trained model (save)
```
  --do_lower_case=False \    # boolean, lower case or not in BERT language model
  --task_name=STFL \         # String, task name (KORE: Korean Relation Extraction)
  --do_train=true \          # boolean, train or not
  --do_eval=true \           # boolean, evaluation or not
  --data_dir=$KORE_DIR/ \    # String, data file (train, dev, test) path
  --vocab_file=$BERT_BASE_DIR/vocab.txt \    # String, BERT language model vocabulary path
  --bert_config_file=$BERT_BASE_DIR/bert_config.json \   # String, BERT config file path
  --init_checkpoint=$BERT_BASE_DIR/bert_model.ckpt \     # String, BERT model check point path
  --max_seq_length=128 \     # Integer, max input sequence length
  --train_batch_size=16 \    # Integer, batch size
  --learning_rate=2e-5 \     # Double, learning rate
  --num_train_epochs=30.0 \   # Integer, train epoches
  --output_dir=trained_model/sentence_filtering/ \       # String, Path to trained model (save)
  --output_csv=ko_re_data/output.csv # String, Path to evaluation result
```
Test: ``sentence_prediction.sh``

### How to run
``preproc_filter.py [INPUT_CSV] [OUTPUT_TSV]``
<br>and<br>
Set train/dev/test file path in ``class StflProcessor - run_classifier.py`` 
<br>and<br>
``sentence_classifier.sh`` or ``sentence_prediction.sh``
<br>and<br>
``postproc_NA.py``
<br>and<br>
Use ``ko_re_data/filtered_sentence_True.csv`` file

### Data Example
```
NA	썰전	대한민국	종합편성채널 JTBC ‘<e1>썰전</e1> ’이 예능심판자 코너를 통해 아역배우 김동현_(1984년) 군과 함께 <e2>대한민국</e2> 아역스타들을 분석하는 시간을 가졌다.
```
TSV format; relation, subject, object, and sentence with two entities
<br>and<br>
```
"구한말에는 갑신정변 으로 피신했다가 귀국, <e1>독립협회</e1> 활동, 독립신문 <e2>발행인</e2> 과 제2대 독립신문 (獨立新聞社) 사장 등으로 활동했으며 만민공동회 의 최고 지도력 로서 강연, 계몽활동과 민권운동과 민중의 참정권 요구 운동·개혁운동에 참여했고, 서재필 이 강제추방된 이후 <e1>독립협회</e1> 와 반청계몽운동 활동을 지도했으나, 후에 친일 인사로 변절하였다.",NA,,,,0.8557533
<e1>GRP_레코드</e1> ()는 <e2>미국</e2> 의 레코드 회사이다.,True
```
Output CSV format; sentence with two entities, relation (NA or True), score


## Licenses
* `CC BY-NC-SA` [Attribution-NonCommercial-ShareAlike](https://creativecommons.org/licenses/by-nc-sa/2.0/)
* If you want to commercialize this resource, [please contact to us](http://mrlab.kaist.ac.kr/contact)

## Publisher
[Machine Reading Lab](http://mrlab.kaist.ac.kr/) @ KAIST

## Acknowledgement
This work was supported by Institute for Information & communications Technology Promotion(IITP) grant funded by the Korea government(MSIT) (2013-0-00109, WiseKB: Big data based self-evolving knowledge base and reasoning platform)
