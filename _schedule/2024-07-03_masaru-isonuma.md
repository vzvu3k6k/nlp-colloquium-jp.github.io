---
layout: talk
date: 2024-07-03 18:00:00+0900
time_em: true
inline: false
name: 磯沼大
name_en: Masaru Isonuma
affiliation: University of Edinburgh
bio: エジンバラ大学 日本学術振興会海外特別研究員。2021年東京大学大学院工学系研究科博士課程修了。東京大学大学院工学系研究科特任研究員及び特任助教を経て、2023年より現職。
website: https://www.isonuma.com/
topic: Unlearning Traces the Influential Training Data of Language Models
abstract: ある言語モデルの高い能力を発揮させ、かつ有害な生成を抑えるには、その原因となる学習データの特定が不可欠です。理想的には、あるデータを除いて学習したモデルと全データを学習したモデルを比較することでその学習データの影響を測ることができますが（leave-dataset-out）、計算コストが膨大になり現実的ではありません。本トークでは、学習データを除く代わりに、学習済モデルからデータを逆学習してその影響を測るUnTracという手法について説明します。UnTracは極めて単純で、勾配上昇法で学習データを忘却させ、逆学習後のモデルの性能が悪化するほどその学習データの影響が大きいと推定します。更により効率的な方法として、学習済モデルから評価データを逆学習し学習データで評価するUnTrac-Invという手法を導入し、UnTracを近似できることを示します。本トークではこれらの手法の着想に至った経緯や、逆学習とleave-dataset-outの関係、既存の学習データ影響推定手法との関係についてお話ししたいと思います。
display: true
---

[[動画]](https://youtu.be/LDUQi84yC84) [[スライド]](https://speakerdeck.com/misonuma/nlpkorokiumu-ni-xue-xi-niyoruyan-yu-moderunojie-xi) [[論文]](https://arxiv.org/abs/2401.15241) (ACL 2024)