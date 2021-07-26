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

also character level prediction results could be fined in [evaluation](https://github.com/alirezasalemi7/SemEval2021-Toxic-Spans-Detection/tree/master/evaluation) directory.

## How to train models?

The procedure of trining models is straight but needs following materials.

### Data

We used following datasets to train our models:

- Main Task Dataset (Toxic Spans): this dataset was released for competition and could be downloaded from [this link.](https://github.com/ipavlopoulos/toxic_spans)

- Jigsaw Unintended Bias in Toxicity Classification Dataset: this dataset was used to train Attention-based models and could be downloaded from [this link.](https://www.kaggle.com/c/jigsaw-unintended-bias-in-toxicity-classification/data)

- Toxic words list: this dataset contains some hate words and used for base methods in experiments and could be downloaded from [this link.](https://www.kaggle.com/nicapotato/bad-bad-words)

### Codes

[models](https://github.com/alirezasalemi7/SemEval2021-Toxic-Spans-Detection/tree/master/models) directory contains notebooks to train each model from scratch and all you need is to run this notebooks. this codes also save some checkpoints of trained model for later use. to load checkpoints use following code:

```
model.load_weights('address to checkpoint')
```

also it should be noted that `model` is keras model.

## Citation

If you use this code, please consider citing our paper:


```
@inproceedings{salemi-etal-2021-utnlp,
    title = "{UTNLP} at {S}em{E}val-2021 Task 5: A Comparative Analysis of Toxic Span Detection using Attention-based, Named Entity Recognition, and Ensemble Models",
    author = "Salemi, Alireza  and
      Sabri, Nazanin  and
      Kebriaei, Emad  and
      Bahrak, Behnam  and
      Shakery, Azadeh",
    booktitle = "Proceedings of the 15th International Workshop on Semantic Evaluation (SemEval-2021)",
    month = aug,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.semeval-1.136",
    pages = "995--1002",
    abstract = "Detecting which parts of a sentence contribute to that sentence{'}s toxicity{---}rather than providing a sentence-level verdict of hatefulness{---} would increase the interpretability of models and allow human moderators to better understand the outputs of the system. This paper presents our team{'}s, UTNLP, methodology and results in the SemEval-2021 shared task 5 on toxic spans detection. We test multiple models and contextual embeddings and report the best setting out of all. The experiments start with keyword-based models and are followed by attention-based, named entity- based, transformers-based, and ensemble models. Our best approach, an ensemble model, achieves an F1 of 0.684 in the competition{'}s evaluation phase.",
}
```

