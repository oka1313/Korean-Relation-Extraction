#!/usr/bin/env bash
source /home/sangha/anaconda3/bin/activate tensorflow
export BERT_BASE_DIR=multi_cased_L-12_H-768_A-12
export KORE_DIR=ko_re_data
export TRAINED_CLASSIFIER=trained_model/sentence_filtering

#python input_formatter.py $KORE_DIR/merged_file.csv $KORE_DIR/test_filter.tsv
cp $KORE_DIR/train_cr.tsv $KORE_DIR/test_filter.tsv

CUDA_VISIBLE_DEVICES=2 python run_classifier.py \
    --do_lower_case=False \
    --task_name=STFL \
    --do_predict=True \
    --data_dir=$KORE_DIR \
    --vocab_file=$BERT_BASE_DIR/vocab.txt \
    --bert_config_file=$BERT_BASE_DIR/bert_config.json \
    --init_checkpoint=$TRAINED_CLASSIFIER \
    --max_seq_length=128 \
    --output_dir=$KORE_DIR \
    --output_csv=filtered_train_set_cr.csv
