---
layout: talk
date: 2024-01-24 12:00:00+0900
inline: false
name: 山田祐太朗
name_en: Yutaro Yamada
affiliation: Yale University
bio: PhD student at Yale University
website: https://runopti.github.io/
topic: When are Lemons Purple? The Concept Association Bias of Vision-Language Models
abstract: Large-scale vision-language models such as CLIP have shown impressive performance on zero-shot image classification and image-to-text retrieval. However, such performance does not realize in tasks that require a finer-grained correspondence between vision and language, such as Visual Question Answering (VQA). We investigate why this is the case, and report an interesting phenomenon of vision-language models, which we call the Concept Association Bias (CAB), as a potential cause of the difficulty of applying these models to VQA and similar tasks. We find that models with CAB tend to treat input as a bag of concepts and attempt to fill in the other missing concept crossmodally, leading to an unexpected zero-shot prediction. We demonstrate CAB by showing that CLIP's zero-shot classification performance greatly suffers when there is a strong concept association between an object (e.g. eggplant) and an attribute (e.g. color purple). We also show that the strength of CAB predicts the performance on VQA. We observe that CAB is prevalent in vision-language models trained with contrastive losses, even when autoregressive losses are jointly employed. However, a model that solely relies on autoregressive loss seems to exhibit minimal or no signs of CAB.
display: true
---
[[動画]](https://youtu.be/WUUla16GzwI) [[スライド]](https://runopti.github.io/doc/NLP_colloquium_presentation_Jan24.pdf) [[論文]](https://arxiv.org/abs/2212.12043) (EMNLP 2023)
