---
layout: talk
date: 2024-12-04 12:00:00+0900
time_em: false
inline: false
name: 森下皓文
name_en: Terufumi Morishita
affiliation: 日立製作所
bio: 日立製作所・中央研究所・先端AIイノベーションセンターの研究者(自然言語処理・機械学習)です．「LLMに論理推論を教えるためのコーパス生成技術」や「アンサンブル学習の性能を決定づける要因を情報理論的に解明する」というような研究を，行ってきています．それ以前は，東京大学大学院・理学系研究科・物理学専攻にて，村山斉特任教授の元で素粒子物理学を研究していました．「暗黒物質(ダークマター)の候補として超対称性理論が予言する，ウィーノ粒子の探索」というテーマです．
website: https://morisht.github.io/MorishT/
topic: LLMに論理推論を教えられるか？ - 人工コーパスを用いたアプローチ
abstract: 近年登場した大規模言語モデル(LLM)は，広範な課題を巧みに解決し，人工知能「人間のように考える機械」の実現へと道を切り拓きました．しかしながらLLMは，事前学習時に暗記した「知識」の流用によって既存課題はよく解けるものの，「推論」を用いて真に未知なる課題を解くことは苦手とします．例えば「過去年度のコーディング試験は解けるが，最新年度は解けない」「算数の有名問題をそのまま出題すれば解けるが，数字を変えると解けない」等です．これに対して我々は，推論の中でも最も基本的な演繹推論をLLMに教えることを目差し，「演繹推論を模擬したサンプルを大量に自動生成し学習させる」というアプローチを進めてきています．良質なサンプルを用意するため，記号論理学や先行研究での経験的知見に基づく確固たるサンプル設計指針を設け，プログラムによって(=ルールベースで)サンプルを生成します．できあがったサンプル群 - FLDコーパス (Formal Logic Deduction Corpus) - での学習により，最先端のLLM(LLaMA-3.1-70B)の推論能力を向上させることができました．本トークでは，ICML(2023)・LREC-COLING(2024)・NeurIPS(2024)の論文を中心に，このアプローチを紹介します．
display: true
---
[[動画]](https://www.youtube.com/watch?v=AJPvSueaHWI) [[スライド]](https://speakerdeck.com/morishtr/nlpkorokiumu-llmnilun-li-tui-lun-wojiao-erareruka-ren-gong-kopasuwoyong-itaapuroti) [[論文1]](https://arxiv.org/abs/2411.12498) (NeurIPS 2024) [[論文2]](https://aclanthology.org/2024.lrec-main.832/) (LREC-COLING 2024) [[論文3]](https://proceedings.mlr.press/v202/morishita23a.html) (ICML 2023)
