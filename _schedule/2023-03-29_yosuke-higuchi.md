---
layout: talk
date: 2023-03-29 12:00:00+0900
inline: false
name: 樋口陽祐
affiliation: 早稲田大学
bio: 早稲田大学大学院 基幹理工学研究科 情報理工・情報通信専攻 博士課程 在籍
website: https://yosukehiguchi.github.io/
topic: End-to-End Speech Recognition with Pre-trained Masked Language Model
abstract: End-to-End音声認識では、音声からテキストへの直接変換を、単一の深層ニューラルネットワークを用いて実現することを目的とする。このとき、正確なテキストを生成するには出力単語間の依存性をいかに捉えるかが鍵となるが、これを音声情報から抽出するのは容易でない。ある発話音声に対して「あめ」という音を認識するだけでは不十分であり、その音が「雨」と「飴」のどちらを意図しているのかについても、文脈に応じて推定する必要がある。本発表では、汎用言語モデルであるBERTから得られる文脈情報を音声処理の過程に明示的に組み込むことで、End-to-End音声認識の精度が向上することを示す。また、汎用言語モデルと音声認識で扱われるテキストの違い（語彙の違い、句読点や大文字・小文字の有無など）を解消するための手法を検討し、それによる改善効果についても紹介する。
display: true
---

[[動画]](https://youtu.be/nOI7ibU9JXM) [[スライド]](https://drive.google.com/file/d/1vcRZP0TW3bV73QnhxJpAMOv6eOfm8Cb9/view?usp=share_link) [[論文1]](https://aclanthology.org/2022.findings-emnlp.402) (Findings of EMNLP 2022) [[論文2]](https://arxiv.org/abs/2211.00792) (ICASSP 2023)

