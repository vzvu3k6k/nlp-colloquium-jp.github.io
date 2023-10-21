---
layout: talk
date: 2023-09-13 12:00:00+0900
inline: false
name: <a href="https://www.kecl.ntt.co.jp/icl/lirg/members/nagata/index-j.html">永田昌明</a><sup>1</sup>, <a href="https://yukiar.github.io/index_jp.html">荒瀬由紀</a><sup>2</sup>
affiliation: <sup>1</sup>NTTコミュニケーション科学基礎研究所, <sup>2</sup>大阪大学
bio: "<sup>1</sup>1987年京都大学大学院工学研究科修士課程修了．同年，日本電信電話株式会社入社．現在，コミュニケーション科学研究所 上席特別研究員．工学博士．機械翻訳，自然言語処理の研究に従事．<br><sup>2</sup>She is an associate professor at the Graduate School of Information Science and Technology, Osaka University, Japan. After obtaining my PhD in Information Science from Osaka University (2010), She worked for Microsoft Research Asia, where she started NLP research that continues to captivate me to this day. My research interests focus on paraphrasing and NLP technology for language education and healthcare."
topic: 単語アラインメントの最前線
abstract: "<sup>1</sup>お互いに翻訳になっている異なる言語の文の対において、お互いに翻訳になっている語句の対を同定することを単語対応と呼ぶ。単語対応は、歴史的に機械翻訳の研究から始まったので、ふつう「単語対応」といえば「二言語単語対応」(bilingual word alignment)を指し、同じ言語の文対の単語対応は「単言語単語対応」(monolingual word alignment)と呼ぶ。
近年、SpanAlign, SimAlign, AWESOMEなどの訓練済み多言語モデルを用いた単語対応法が提案され、それ以前の統計的機械翻訳モデルに基づく単語対応の精度を大きく上回った。永田らが提案した言語横断スパン予測に基づく教師あり単語対応SpanAlignは、人手で作成した単語対応の正解データが約300文対あれば世界最高精度を達成する。しかし、正解データを用意することが難しい場合には、教師なし単語対応SimAlignや、対訳文データを教師信号とする半教師あり単語対応AWESOMEの方が使いやすい。
そこで我々は、SpanAlignにおける単語対応の正解データの制約を緩め、必ずしも対訳文対ではなく、部分的に注釈を持ち、誤りを含みうる単語対応データを教師信号とする弱教師あり単語対応事前訓練法WSPAlignを考案した。Wikipediaの言語間リンクや訓練済み多言語モデルの単語埋め込みを利用して訓練データを作成して事前訓練を行ったところ、教師なし単語対応ではSimAlignを上回り、教師あり単語対応ではSpanAlignを上回って世界最高精度を更新した。
<br><sup>2</sup>Monolingual word alignment, which identifies semantically corresponding words in a sentence pair, has been actively studied as a crucial technique for modelling semantic relationships between sentences, such as for paraphrase identification and textual entailment recognition. Remarkably, the alignment information has been recently recognized as valuable cues for interpreting model predictions with application to quality estimation and hallucination detection. Despite years of dedicated research, challenges still persist in many-to-many and null alignment, which constitutes an *unbalanced* word alignment problem. In this talk, we show that the optimal transport (OT) based methods are natural and sufficiently powerful approaches to unbalanced word alignment without tailor-made techniques. We provide a comprehensive analysis that unveils the characteristics of different OT problems on unbalanced word alignment across diverse null alignment ratios."
display: true
---
[[スライド1]](https://www.kecl.ntt.co.jp/icl/lirg/members/nagata/talk/230913nlp-colloquium_nagata.pdf) [[論文1]](https://aclanthology.org/2023.acl-long.621/) (ACL 2023)
[[スライド2]](https://speakerdeck.com/yukiar/13-unbalanced-optimal-transport-for-unbalanced-word-alignment) [[論文2]](https://aclanthology.org/2023.acl-long.219/) (ACL 2023)
