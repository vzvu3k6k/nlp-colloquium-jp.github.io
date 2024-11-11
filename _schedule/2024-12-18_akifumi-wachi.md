---
layout: talk
date: 2024-12-18 12:00:00+0900
time_em: false
inline: false
name: 和地瞭良
name_en: Akifumi Wachi
affiliation: LINEヤフー株式会社
bio: IBM東京基礎研究所を経てLINEヤフー株式会社で勤務。強化学習の理論と応用の研究に従事。とくに、安全性に関する制約条件を課した強化学習の理論解析、および言語モデルのセーフティアライメントなどの実応用に興味がある。著書（共著）に『強化学習から信頼できる意思決定へ』。博士（情報工学）。
website: https://akifumi-wachi-4.github.io/website/jp.html
topic: Stepwise Alignment for Constrained Language Model Policy Optimization
abstract: 安全性と信頼性は、大規模言語モデル (LLM) の負の側面を抑制しながらその恩恵を享受するための必須の要件です。この課題を解決するために「アライメント」と呼ばれる技術が盛んに研究されており、Reinforcement Learning from Human Feedback (RLHF) や Direct Preference Optimization (DPO) などが主要技術として用いられています。しかしながら、RLHF や DPO は、人間による選好ラベルが一次元の報酬関数に基づいていているという暗黙の仮定をとっており、人間の複雑な評価基準を表現することが困難である、という欠点がありました。私達の NeurIPS 2024 の論文では、言語モデルのアライメントを、安全制約の下で報酬（有用性）を最大化する方策最適化問題として定式化し、Stepwise Alignment for Constrained Policy Optimization（SACPO）というアルゴリズムを提案しました。SACPOは、「報酬と安全性の両方を考慮した言語モデルは報酬のみに関してアライメントした言語モデルから直接獲得できる」という理論的裏付けに基づいています。この理論をもとに、SACPOは、DPOなどのシンプルで強力なアライメント手法を適用しながら、それぞれの指標に対して言語モデルを段階的にアライメントします。SACPOは、実装の簡便さ・安定性・計算効率などの利点があるほか、アルゴリズムやデータセットの柔軟性という最大の特徴を有しています。さらに、SACPO とモデルマージを組み合わせた、実用的な派生手法 (P-SACPO) についても解説します。最後に、SACPOが、7Bクラスの言語モデルのファインチューニングタスクにおいて、既存手法よりも報酬（有用性）と安全性（無害性）の両方で優位な結果が得られた、という実験結果を紹介します。
display: true
---

[[論文]](https://arxiv.org/abs/2404.11049) (NeurIPS 2024)
