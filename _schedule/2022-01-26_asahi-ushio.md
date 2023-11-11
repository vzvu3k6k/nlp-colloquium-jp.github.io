---
layout: talk
date: 2022-01-26 21:00:00+0900
time_em: true
inline: false
name: 潮旭
affiliation: Cardiff University 
bio: Asahi Ushio is a Ph.D student in the School of Computer Science and Informatics at Cardiff University, co-advised by Jose Camacho-Collados and Steven Schockaert. He studies natural language processing (NLP), focusing on language model probing and application of language model in tasks such as named-entity recognition (NER) and question generation (QG). In 2021, he did research internships at Amazon supervised by Danushka Bollegala, and Snapchat co-supervised by Francesco Barbieri and Leonardo Neves. Before joining Cardiff University, he had been a full-time research engineer at Cogent Labs from 2018 to 2020. Visit his personal website for more info https://asahiushio.com
website: https://asahi417.github.io/
topic: Toward a Better Understanding of Relational Knowledge in Language Models
abstract: Language model pretraining plays a significant role in natural language processing nowadays, yet we are still far from fully understanding the mechanism of language models. In this talk, I will present our research about relational knowledge in language models, which is one of the important aspects to understand the ability of language models but less studied than others objective such as factual knowledge or syntactic analysis. In short, relational knowledge can be regarded as a capacity to predict the relation among concepts, and utilize it to make a better decision in downstream tasks. In our first work [1], we point out that the current state-of-the-art language models are not capable of solving a simple word analogy task, and our second work [2] presents a finetuning framework to distill the relational knowledge from language models that establishes the best performance in two tasks, which require relation understanding (even better than GPT-3). The series of our researches indicate that language models actually acquire relational knowledge to some extent at the pretraining phase, but we need a specific methodology such as the finetuning scheme presented in our work [2] to extract such knowledge.
display: true
---
[[動画]](https://youtu.be/ZeOXRgtfu1E) [[スライド1]](https://www.slideshare.net/asahiushio1/202105-acl-bert-is-to-nlp-what-alexnet-is-to-cv-can-pretrained-language-models-identify-analogies) [[論文1]](https://aclanthology.org/2021.acl-long.280/)
 (ACL 2021)  [[スライド2]](https://www.slideshare.net/asahiushio1/202111-emnlp-distilling-relation-embeddings-from-pretrained-language-models) [[論文2]](https://aclanthology.org/:wq2021.emnlp-main.712/) (EMNLP 2021)
