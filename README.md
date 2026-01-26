# ParsTranslit

This repository will contain the code, data, and models for the ParsTranslit project upon publication.

Our preprint ["ParsTranslit: Truly Versatile Tajik-Farsi Transliteration"](https://arxiv.org/abs/2510.07520) describes our training process and results, with our evaluation demonstrating our model's superior performance compared to all other available models.

# Bi-directional Tajik-Farsi Transliteration Model

# ParsText v2 (no overlaps)
Included within the released data will be an updated version of the ParsText corpus for the paper entitled ["ParsText: A Digraphic Corpus for Tajik-Farsi Transliteration"](https://doi.org/10.31234/osf.io/xdf2w). 

This filtered version does not include the previously-included BBC articles, as it was discovered that [another dataset](https://github.com/stibiumghost/tajik-to-persian-transliteration) contained a more complete set of articles with which ours overlap. Their paper describing their model and dataset is [here](https://elar.urfu.ru/handle/10995/140361) (in Russian). 

However, we also include two new datasets, most notably the first Tajik-Farsi named entity dataset drawn from the ParaNames Wikipedia corpus and an aligned version of the Masnavi.


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
@inproceedings{merchant-tang-2024-parstext,
    title = "{P}ars{T}ext: A Digraphic Corpus for {T}ajik-{F}arsi Transliteration",
    author = "Merchant, Rayyan  and
      Tang, Kevin",
    editor = "Gorman, Kyle  and
      Prud'hommeaux, Emily  and
      Roark, Brian  and
      Sproat, Richard",
    booktitle = "Proceedings of the Second Workshop on Computation and Written Language (CAWL) @ LREC-COLING 2024",
    month = may,
    year = "2024",
    address = "Torino, Italia",
    publisher = "ELRA and ICCL",
    url = "https://aclanthology.org/2024.cawl-1.1/",
    pages = "1--7",
    abstract = "Despite speaking dialects of the same language, Persian speakers from Tajikistan cannot read Persian texts from Iran and Afghanistan. This is due to the fact that Tajik Persian is written in the Tajik-Cyrillic script, while Iranian and Afghan Persian are written in the Perso-Arabic script. As the formal registers of these dialects all maintain high levels of mutual intelligibility with each other, machine transliteration has been proposed as a more practical and appropriate solution than machine translation. Unfortunately, Persian texts written in both scripts are much more common in print in Tajikistan than online. This paper introduces a novel corpus meant to remedy that gap: ParsText. ParsText contains 2,813 Persian sentences written in both Tajik-Cyrillic and Perso-Arabic manually collected from blog pages and news articles online. This paper presents the need for such a corpus, previous and related work, data collection and alignment procedures, corpus statistics, and discusses directions for future work."
}
```
