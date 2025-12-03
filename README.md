# ParsTranslit

This repository will contain the code, data, and models for the ParsTranslit project upon publication.

Our preprint ["ParsTranslit: Truly Versatile Tajik-Farsi Transliteration"](https://arxiv.org/abs/2510.07520) describes our training process and results, with our evaluation demonstrating our model's superior performance compared to all other available models.

# Bi-directional Tajik-Farsi Transliteration Model

# ParsText v2 (no overlaps)
Included within the released data will be a curated/trimmed version of the ParsText corpus for the paper entitled ["ParsText: A Digraphic Corpus for Tajik-Farsi Transliteration"](https://doi.org/10.31234/osf.io/xdf2w). 

This filtered version only includes the manually-collected blog posts, and does not include the previously-included BBC articles, as it was discovered that [another dataset](https://github.com/stibiumghost/tajik-to-persian-transliteration) contained a more complete set of articles with which ours overlap.


# Cite Us!
If you use or reference ParsTranslit, please cite our preprint:
```
@misc{merchant2025parstranslittrulyversatiletajikfarsi,
      title={ParsTranslit: Truly Versatile Tajik-Farsi Transliteration}, 
      author={Rayyan Merchant and Kevin Tang},
      year={2025},
      eprint={2510.07520},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2510.07520}, 
}
```

If you use or reference ParsText, please cite our paper:

```
@InProceedings{MerchantTang_CAWL_Accepted_2024,
author = {Rayyan Merchant and Kevin Tang},
title = {{P}ars{T}ext: A Digraphic Corpus for {T}ajik-{F}arsi Transliteration},
booktitle = {{Proceedings of the Second Workshop on Computation and Written Language (CAWL 2024)}},
year = {2024},
editor = {Gorman, Kyle and Prud’hommeaux, Emily and Sproat, Richard and Roark, Brian},
note = {accepted (Preprint: \url{https://doi.org/10.31234/osf.io/xdf2w}},
publisher = {Association for Computational Linguistics},
month = {05},
pubstate = {forthcoming},
address = {Torino, Italia},
}
```
