---
layout: post
date: 2021-05-26 12:00:00+0900
inline: true
name: 安永迪弘
affiliation: Stanford University
bio: Michihiro Yasunaga is a 2nd-year PhD student in Computer Science at Stanford University, advised by Percy Liang and Jure Leskovec. His research interest is in natural language processing and machine learning. His recent work focuses on learning from various modalities of data, such as text, programs and graphs. He received his B.S. from Yale University in 2019.
website: https://michiyasunaga.github.io/
topic: Reasoning with Language Models and Knowledge Graphs for Question Answering
abstract: "Question answering systems need to access relevant knowledge and reason over it effectively. In this talk, we consider answering questions using knowledge from pre-trained language models (LMs) and knowledge graphs (KGs). This problem presents two major challenges: given a QA context (question and answer choices), methods need to (i) identify relevant knowledge from large KGs, and (ii) perform joint reasoning over the QA context and KG. We present a new model, QA-GNN, which addresses the above challenges through two innovations: (i) relevance scoring, where we use LMs to estimate the importance of KG nodes relative to the given QA context, and (ii) joint reasoning, where we connect the QA context and KG to form a joint graph, and mutually update their representations through graph neural networks. We experiment with QA-GNN on commonsense and science question answering tasks, and show its improvement over existing LM or KG-based models."
display: true
---

[[paper]](https://arxiv.org/abs/2104.06378) (NAACL 2021)
