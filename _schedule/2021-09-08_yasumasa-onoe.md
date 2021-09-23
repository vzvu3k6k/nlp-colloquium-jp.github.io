---
layout: talk
date: 2021-09-08 12:30:00+0900
time_em: true
inline: false
name: 尾上康雅
affiliation: The University of Texas at Austin
bio: Yasumasa Onoe is a PhD student in Computer Science at the University of Texas at Austin, advised by Greg Durrett. His recent research includes entity analysis tasks such as fine-grained entity typing, entity linking (named entity disambiguation), and effective entity representations (e.g., box embeddings). Currently, he is interested in how to teach machines common sense about real-world entities.
website: https://www.cs.utexas.edu/~yasumasa/
topic: Modeling Fine-Grained Entity Types with Box Embeddings
abstract: Neural entity typing models typically represent entity types as vectors in a high-dimensional space, but such spaces are not well-suited to modeling these types' complex interdependencies. We study the ability of box embeddings, which represent entity types as d-dimensional hyperrectangles, to represent hierarchies of fine-grained entity type labels even when these relationships are not defined explicitly in the ontology. Our model represents both types and entity mentions as boxes. Each mention and its context are fed into a BERT-based model to embed that mention in our box space; essentially, this model leverages typological clues present in the surface text to hypothesize a type representation for the mention. Soft box containment can then be used to derive probabilities, both the posterior probability of a mention exhibiting a given type and the conditional probability relations between types themselves. We compare our approach with a strong vector-based typing model, and observe state-of-the-art performance on several entity typing benchmarks. In addition to competitive typing performance, our box-based model shows better performance in prediction consistency (predicting a supertype and a subtype together) and confidence (i.e., calibration), implying that the box-based model captures the latent type hierarchies better than the vector-based model does.
display: true
---

[[スライド]](https://speakerdeck.com/yasumasaonoe/modeling-fine-grained-entity-types-with-box-embeddings) [[論文]](https://arxiv.org/abs/2101.00345) (ACL2021)
