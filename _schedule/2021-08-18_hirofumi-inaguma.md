---
layout: post
date: 2021-08-18 12:00:00+0900
inline: true
name: 稲熊寛文
affiliation: 京都大学
bio: 2016年 京都大学工学部情報学科卒業．2018年 京都大学大学院情報学研究科修士課程修了．現在，同大学院博士後期課程にて音声認識・音声翻訳に関する研究に従事．
website: http://sap.ist.i.kyoto-u.ac.jp/members/inaguma/
topic: Non-autoregressive modeling for end-to-end speech translation
abstract: ソース言語の音声からターゲット言語の翻訳文を直接生成するend-to-end音声翻訳タスクにおいて，推論速度を改善するため非自己回帰モデルについて検討する．テキスト入力の機械翻訳と違い，音声翻訳では入力に無音区間が存在し，かつ系列長が長いため，ターゲット文の系列長をあらかじめ正確に推定するのは一般的に困難である．そこで本研究では，非自己回帰デコーダとエンコーダを共有する補助自己回帰デコーダを導入して同時学習を行い，推論時に後者を用いてリスコアリングを行うフレームワークを提案する．非自己回帰モデルとして，conditional masked langauge model (CMLM)とconnectionist temporal classification (CTC)について検討する．また，CMLMの翻訳精度を改善する学習方法を提案する．さらに，エンコーダのアーキテクチャとしてTransformerとConformerを比較検討する．補助トピックとして，系列レベル知識蒸留のend-to-end音声翻訳タスクにおける有用性および双方向系列レベル知識蒸留への拡張や，非自己回帰型の中間音声認識デコーダを導入したtwo-pass end-to-endモデルについても触れる．
display: true
---

[[論文1]](https://arxiv.org/abs/2010.13047) (ICASSP 2021) [[論文2]](https://arxiv.org/abs/2104.06457) (NAACL 2021)
