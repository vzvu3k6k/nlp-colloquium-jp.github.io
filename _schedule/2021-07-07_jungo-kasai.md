---
layout: post
date: 2021-07-07 12:00:00+0900
inline: true
name: 笠井淳吾
affiliation: University of Washington
bio: "Jungo Kasai is a rising fourth-year PhD student at the Paul G. Allen School of Computer Science & Engineering of the University of Washington, Seattle, advised by Noah A. Smith. He works on natural language processing and machine learning. His research interests include machine translation, language generation, multilingual natural language processing, and structured prediction."
website: https://homes.cs.washington.edu/~jkasai/
topic: "Deep Encoder, Shallow Decoder: Reevaluating Non-autoregressive Machine Translation"
abstract: "Much recent effort has been invested in non-autoregressive neural machine translation, which appears to be an efficient alternative to state-of-the-art autoregressive machine translation on modern GPUs. In contrast to the latter, where generation is sequential, the former allows generation to be parallelized across target token positions. Some of the latest non-autoregressive models have achieved impressive translation quality-speed tradeoffs compared to autoregressive baselines. In this work, we reexamine this tradeoff and argue that autoregressive baselines can be substantially sped up without loss in accuracy. Specifically, we study autoregressive models with encoders and decoders of varied depths. Our extensive experiments show that given a sufficiently deep encoder, a single-layer autoregressive decoder can substantially outperform strong non-autoregressive models with comparable inference speed. We show that the speed disadvantage for autoregressive baselines compared to non-autoregressive methods has been overestimated in three aspects: suboptimal layer allocation, insufficient speed measurement, and lack of knowledge distillation. Our results establish a new protocol for future research toward fast, accurate machine translation."
display: true
---

[[動画]](https://youtu.be/rxkXohKUthg) [[スライド]](https://www.slideshare.net/JungoKasai/deep-encoder-shallow-decoder-reevaluating-nonautoregressive-machine-translation) [[論文]](https://arxiv.org/abs/2006.10369) (ICLR 2021)

