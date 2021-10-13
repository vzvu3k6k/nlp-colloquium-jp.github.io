---
layout: talk
date: 2021-09-29 12:30:00+0900
date_em: false
time_em: true
inline: false
name: 坂口慶祐
affiliation: Allen Institute for AI
bio: "Keisuke Sakaguchi is a research scientist at the Allen Institute for AI (AI2). His research focuses on 1) commonsense knowledge acquisition and reasoning, 2) robust and efficient methods for natural language processing, and 3) NLP applications for educational purposes."
website: https://keisuke-sakaguchi.github.io/
topic: "proScript: Partially Ordered Scripts Generation"
abstract: "Scripts – prototypical event sequences describing everyday activities – have been shown to help understand narratives by providing expectations, resolving ambiguity, and filling in unstated information. However, to date they have proved hard to author or extract from text. In this work, we demonstrate for the first time that pre-trained neural language models can be finetuned to generate high-quality scripts, at varying levels of granularity, for a wide range of everyday scenarios (e.g., bake a cake). To do this, we collect a large (6.4k) crowdsourced partially ordered scripts (named proScript), that is substantially larger than prior datasets, and develop models that generate scripts by combining language generation and graph structure prediction. We define two complementary tasks: (i) edge prediction: given a scenario and unordered events, organize the events into a valid (possibly partial-order) script, and (ii) script generation: given only a scenario, generate events and organize them into a (possibly partial-order) script. Our experiments show that our models perform well (e.g., F1=75.7 on task (i)), illustrating a new approach to overcoming previous barriers to script collection. We also show that there is still significant room for improvement toward human level performance. Together, our tasks, dataset, and models offer a new research direction for learning script knowledge."
display: true
---

[[動画]](https://youtu.be/BNDVf5gNt1w) [[スライド]](https://www.slideshare.net/keisks/emnlp-2021-proscript) [[論文]](https://arxiv.org/abs/2104.08251) (Findings of EMNLP 2021)
