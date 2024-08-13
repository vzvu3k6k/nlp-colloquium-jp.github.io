---
layout: talk
date: 2024-08-07 12:00:00+0900
time_em: false
inline: false
name: 松原崇
name_en: Takashi Matsubara
affiliation: 北海道大学
bio: 北海道大学 大学院情報科学研究院 教授．2015年に大阪大学 大学院基礎工学研究科より博士（工学）を取得．2015年から神戸大学 大学院システム情報学研究科 助教，2020年から大阪大学 大学院基礎工学研究科 准教授を経て，2024年より現職．2021年 日本科学技術振興機構（JST） 戦略的創造研究推進事業さきがけ（PRESTO）研究者など．
website: https://tksmatsubara.github.io/ja/
topic: 命題論理に基づくガイダンスによるユーザの意図に忠実な画像生成拡散モデル
abstract: 本発表では，CVPR2024でHighlightに選ばれたPredicated Diffusionを紹介します．拡散モデルは高品質で多様な画像生成を可能にします．しかし，テキストに基づく生成では，しばしばテキストの意図を正確に捉えることに失敗します．例えば，指定した物体を生成しなかったり，形容詞が意図しない物体を誤って修飾してり，物体間の所有関係を見落としたりということが発生します．そこでPredicated Diffusionは，テキストに加えてユーザの意図を表現する統一的なフレームワークを提供します．このフレームワークでは，ユーザの意図を述語論理を用いた命題として表現し，アテンションマップのピクセルをファジィ論理として扱うことで両者を結びつけ，命題をより満たすように画像生成過程を誘導するような損失関数を提供します．人間の評価者と訓練済みマルチモーダルモデルにより，Predicated Diffusionは類似した手法に比べて，よりテキストへの忠実性と高い画像品質を実現することが示されました．
display: true
---

[[動画]](https://youtu.be/gg0fKVq5HUo)[[スライド]](https://tksmatsubara.github.io/ja/projects/sueyoshi2023/) [[論文]](https://openaccess.thecvf.com/content/CVPR2024/html/Sueyoshi_Predicated_Diffusion_Predicate_Logic-Based_Attention_Guidance_for_Text-to-Image_Diffusion_Models_CVPR_2024_paper.html) (CVPR 2024)
