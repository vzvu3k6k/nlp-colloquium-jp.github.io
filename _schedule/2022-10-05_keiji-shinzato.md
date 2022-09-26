---
layout: talk
date: 2022-10-05 10:00:00+0900
time_em: true
inline: false
name: 新里圭司
affiliation: "Rakuten Institute of Technology Americas"
bio: "Rakuten Institute of Technology Americas, Lead Scientist. 京都大学大学院情報学研究科 特任助教、特定研究員を経て、2011年に楽天技術研究所入所。2018年より現職。商品属性の抽出、レビュー解析、商品と製品のマッチングなどe-commerceに特化した自然言語処理技術の研究開発に従事。2006年北陸先端科学技術大学院大学情報科学研究科 博士後期課程修了。博士（情報科学）。"
website: https://sites.google.com/site/shinzatokeiji/home?authuser=0
topic: "Simple and Effective Knowledge-Driven Query Expansion for QA-Based Product Attribute Extraction"
abstract: "A key challenge in attribute value extraction (AVE) from e-commerce sites is how to handle a large number of attributes for diverse products. Although this challenge is partially addressed by a question answering (QA) approach which finds a value in product data for a given query (attribute), it does not work effectively for rare and ambiguous queries. We thus propose simple knowledge-driven query expansion based on possible answers (values) of a query (attribute) for QA-based AVE. We retrieve values of a query (attribute) from the training data to expand the query. We train a model with two tricks, knowledge dropout and knowledge token mixing, which mimic the imperfection of the value knowledge in testing. Experimental results on our cleaned version of AliExpress dataset show that our method improves the performance of AVE (+ 6.08 macro F1), especially for rare and ambiguous attributes (+ 7.82 and+ 6.86 macro F1, respectively)."
display: true
---

[[論文]](https://aclanthology.org/2022.acl-short.25/)
