---
layout: talk
date: 2022-07-27 12:00:00+0900
inline: false
name: 藤沼祥成
affiliation: "AWS AI [*Work done at Univ. of Colorado Boulder]"
bio: Yoshinari Fujinuma obtained his PhD at University of Colorado Boulder, where he was advised by Jordan Boyd-Graber, Katharina Kann, and Michael J. Paul. His PhD research includes analysis and improvement on cross-lingual models.
website: https://akkikiki.github.io/
topic: "Match the Script, Adapt if Multilingual: Analyzing the Effect of Multilingual Pretraining on Cross-lingual Transferability*"
abstract: "Pretrained multilingual models enable zero-shot learning even for unseen languages, and that performance can be further improved via adaptation prior to finetuning. However, it is unclear how the number of pretraining languages influences a model’s zero-shot learning for languages unseen during pretraining. To fill this gap, we ask the following research questions: (1) How does the number of pretraining languages influence zero-shot performance on unseen target languages? (2) Does the answer to that question change with model adaptation? (3) Do the findings for our first question change if the languages used for pretraining are all related? Our experiments on pretraining with related languages indicate that choosing a diverse set of languages is crucial. Without model adaptation, surprisingly, increasing the number of pretraining languages yields better results up to adding related languages, after which performance plateaus. In contrast, with model adaptation via continued pretraining, pretraining on a larger number of languages often gives further improvement, suggesting that model adaptation is crucial to exploit additional pretraining languages."
display: true
---

[[動画]](https://youtu.be/BjRMbqE6oPA) [[スライド]](https://akkikiki.github.io/assets/pdf/acl2022_slides.pdf) [[論文]](https://aclanthology.org/2022.acl-long.106/) (ACL 2022)
