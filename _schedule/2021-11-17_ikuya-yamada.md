---
layout: talk
date: 2021-11-17 12:00:00+0900
date_em: false
inline: false
name: 山田育矢
affiliation: 株式会社Studio Ousia
bio: "(株)Studio Ousiaを創業し，自然言語処理の研究開発に従事．2000年に(株)ニューロンを起業し，2005年に売却．その後，2007年に(株)Studio Ousiaを共同創業．理化学研究所AIP客員研究員．Kaggle Master．"
website: https://www.ikuya.net/index_ja.html
topic: "LUKE: Deep Contextualized Entity Representations with Entity-aware Self-attention"
abstract: "Entity representations are useful in natural language tasks involving entities. LUKE is a new pretrained contextualized representations of words and entities based on the bidirectional transformer. LUKE treats words and entities in a given text as independent tokens, and outputs contextualized representations of them. Our model is trained using a new pretraining task based on the masked language model of BERT. The task involves predicting randomly masked words and entities in a large entity-annotated corpus retrieved from Wikipedia. We also propose an entity-aware self-attention mechanism that is an extension of the self-attention mechanism of the transformer, and considers the types of tokens (words or entities) when computing attention scores. The proposed model achieves impressive empirical performance on a wide range of entity-related tasks. In particular, it obtains state-of-the-art results on five well-known datasets: Open Entity (entity typing), TACRED (relation classification), CoNLL-2003 (named entity recognition), ReCoRD (cloze-style question answering), and SQuAD 1.1 (extractive question answering)."
display: true
---
[[動画]](https://youtu.be/HyU5iSPe9jQ) [[スライド]](https://speakerdeck.com/ikuyamada/luke-at-nlpkorokiumu) [[論文]](https://arxiv.org/abs/2010.01057)  (EMNLP2020)
