# ParsTranslit

This repository contains the code, data, and models for the ParsTranslit project.

Transliterate.py contains example inference code for our transliteration model using ctranslate2.

# Bi-directional Tajik-Farsi Transliteration Model

# ParsText (filtered)
Included within the released data will be a filtered version of the corpus for the paper entitled ["ParsText: A Digraphic Corpus for Tajik-Farsi Transliteration"](https://doi.org/10.31234/osf.io/xdf2w). 

This filtered version only includes the manually-collected blog posts, and does not include the previously-included BBC articles, as it was discovered that [another dataset](https://github.com/stibiumghost/tajik-to-persian-transliteration) contained a more complete set of articles with which ours overlap.


# Cite Us!
If you use or reference ParsTranslit, please cite:
```
@inproceedings{merchant-tang-2026-parstranslit,
    title = "{P}ars{T}ranslit: Truly Versatile {T}ajik-{F}arsi Transliteration",
    author = "Merchant, Rayyan  and
      Tang, Kevin",
    editor = "Demberg, Vera  and
      Inui, Kentaro  and
      Marquez, Llu{\'i}s",
    booktitle = "Findings of the {A}ssociation for {C}omputational {L}inguistics: {EACL} 2026",
    month = mar,
    year = "2026",
    address = "Rabat, Morocco",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2026.findings-eacl.73/",
    doi = "10.18653/v1/2026.findings-eacl.73",
    pages = "1431--1443",
    ISBN = "979-8-89176-386-9",
    abstract = "As a digraphic language, the Persian language utilizes two written standards: Perso-Arabic in Afghanistan and Iran, and Tajik-Cyrillic in Tajikistan. Despite the significant similarity between the dialects of each country, script differences prevent simple one-to-one mapping, hindering written communication and interaction between Tajikistan and its Persian-speaking ``siblings''. To overcome this, previously-published efforts have investigated machine transliteration models to convert between the two scripts. Unfortunately, most efforts did not use datasets other than those they created, limiting these models to certain domains of text such as archaic poetry or word lists. A truly usable transliteration system must be capable of handling varied domains, meaning that suck models lack the versatility required for real-world usage. The contrast in domain between data also obscures the task{'}s true difficulty. We present a new state-of-the-art sequence-to-sequence model for Tajik-Farsi transliteration trained across all available datasets, and present two datasets of our own. Our results across domains provide clearer understanding of the task, and set comprehensive comparable leading benchmarks. Overall, our model achieves chrF++ and Normalized CER scores of 87.91 and 0.05 from Farsi to Tajik and 92.28 and 0.04 from Tajik to Farsi. Our model, data, and code are available at https://github.com/merchantrayyan/ParsTranslit."
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
