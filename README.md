# A Comparative Analysis of Toxic Span Detection using Attention-based, Named Entity Recognition, and Ensemble Models

Detecting which parts of a sentence contributes to that sentence's toxicity&mdash;rather than providing a sentence-level verdict of hatefulness&mdash;would increase the interpretability of models and allow human moderators to better understand the outputs of the system. This repository contains our team's, *UTNLP*, codes and results. We test multiple models and contextual embeddings and report the best setting out of all. The experiments start with keyword-based models and are followed up by attention-based, named entity-based, transformers-based, and ensemble models. Our best approach, an ensemble model, achieves an F1 of 0.684 in SemEval 2021 Task 5 evaluation phase.

## models that was used in experiments

This repository contains codes for following models and methods:

- base methods:
    - keyword based method: a list of toxic words was collected and each word in sentence was annotated if that word was in toxic words list.
    
    - sentiment based method: for each word in sentence if the word have negative sentiment that word was annotated as toxic.
    
    - random: some numbers as index of toxic characters are randomly selected and are taken as toxic characters.

- attention based model
    - BERT with attention: BERT-base used as word embedding and output of BERT layer goes through Attention layer that compute single vector for sentence (usually called attention with context) then the vector goes through 3 dense layer to classify each sentence in to toxic or non-toxic. if a sentence is toxic, then scores of attention for sentence is extracted and with some of token are annotated as toxic.

- NER models: Named entity recognition is a natural language processing method for information extraction from unstructured text data such as e-mails, newspapers, blogs, etc. we used this method to annotate part of sentence as toxic. there are 3 labels that we annotate each word with them, toxic, non-toxic, padding. Conditional random fields (CRFs) are a class of statistical modeling methods often applied in pattern recognition and machine learning and used for structured prediction. Whereas a classifier predicts a label for a single sample without considering "neighboring" samples, a CRF can take context into account. we combine word embeddings and CRF to use this model for toxic span detection.
    
    - BERT based: the following models use BERT as embedding:
        - BERT-base with CRF    
        - BERT-base with LSTM and CRF
    
    - Electra based: the following models use Electra as embedding:
        - Electra-base with CRF
        - Electra-base with LSTM and CRF

    - RoBERTa based: the following models use RoBERTa as embedding:
        - RoBERTa-base with CRF
        - RoBERTa-base with LSTM and CRF

- ensemble methods: combination of results of RoBERTa, BERT and Electra with CRF was used to get better results.
    - intersection of characters that are selected by each model.
    - union of characters that are selected by each model.
    - vote of characters that are selected by each models. the vote means that each character that is in results of at least 2 models, would be selected.

## Evaluation

The the results of evaluation phase of competition are reported in this table.

| model | F1 |
|-------|----|
|Attention|0.609|
|BERT + CRF|0.672|
|Electra + CRF|0.658|
|RoBERTa + CRF|0.667|
|Ensemble(union)|0.619|
|Ensemble(vote)|0.681|
|**Ensemble(intersection)**|**0.684**|
