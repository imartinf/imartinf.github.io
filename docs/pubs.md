# Publications

## 2023

### Exploring Video Transformers and Automatic Segment Selection for Memorability Prediciton

Martín-Fernández, I., Esteban-Romero, S., Bellver-Soler, J., Gil-Martín, M., & Fernández-Martínez, F. (2023). Exploring Video Transformers and Automatic Segment Selection for Memorability Prediction.

**Abstract**:
This paper summarises THAU-UPM’s approach and results from the MediaEval 2023 Predicting Video Memorability task. Focused on the generalisation subtask, our work leverages a pre-trained Video Vision Transformer (ViViT), fine-tuned on memorability-related data, to model temporal and spatial relationships in videos. We propose novel, annotator-independent automatic segment selection methods grounded in visual saliency. These methods identify the most relevant video frames prior to conducting memorability score estimation. This selection process is implemented during both training and evaluation phases. Our study demonstrates the effectiveness of fine-tuning the ViViT model compared to a scratchtrained baseline, emphasising the importance of pre-training for predicting memorability. However, the model shows comparable sensitivity to both saliency-based and naive segment selection methods, suggesting that fine-tuning may harness similar benefits from various video segments. These results underscore the robustness of our approach but also signal the need for ongoing research.

``` title="Bibtex"
@article{martin2023exploring,
  title={Exploring Video Transformers and Automatic Segment Selection for Memorability Prediction},
  author={Mart{\'\i}n-Fern{\'a}ndez, Iv{\'a}n and Esteban-Romero, Sergio and Bellver-Soler, Jaime and Gil-Mart{\'\i}n, Manuel and Fern{\'a}ndez-Mart{\'\i}nez, Fernando},
  year={2023}
}
```
### Video Memorability Prediction From Jointly-learnt Semantic and Visual Features

Iván Martín-Fernández, Ricardo Kleinlein, Cristina Luna-Jiménez, Manuel Gil-Martín, and Fernando Fernández-Martínez. 2023. Video Memorability Prediction From Jointly-learnt Semantic and Visual Features. In Proceedings of the 20th International Conference on Content-based Multimedia Indexing (CBMI '23). Association for Computing Machinery, New York, NY, USA, 178–182. https://doi.org/10.1145/3617233.3617260

**Abstract**:
The memorability of a video is defined as an intrinsic property of its visual features that dictates the fraction of people who recall having watched it on a second viewing within a memory game. Still, unravelling what are the key features to predict memorability remains an obscure matter. This challenge is addressed here by fine-tuning text and image encoders using a cross-modal strategy known as Contrastive Language-Image Pre-training (CLIP). The resulting video-level data representations learned include semantics and topic-descriptive information as observed from both modalities, hence enhancing the predictive power of our algorithms. Our proposal achieves in the text domain a significantly greater Spearman Rank Correlation Coefficient (SRCC) than a default pre-trained text encoder (0.575 ± 0.007 and 0.538 ± 0.007, respectively) over the Memento10K dataset. A similar trend, although less pronounced, can be noticed in the visual domain. We believe these findings signal the potential benefits that cross-modal predictive systems can extract from being fine-tuned to the specific issue of media memorability.

``` title="Bibtex"
@inproceedings{10.1145/3617233.3617260,
author = {Mart\'{\i}n-Fern\'{a}ndez, Iv\'{a}n and Kleinlein, Ricardo and Luna-Jim\'{e}nez, Cristina and Gil-Mart\'{\i}n, Manuel and Fern\'{a}ndez-Mart\'{\i}nez, Fernando},
title = {Video Memorability Prediction From Jointly-learnt Semantic and Visual Features},
year = {2023},
isbn = {9798400709128},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3617233.3617260},
doi = {10.1145/3617233.3617260},
booktitle = {Proceedings of the 20th International Conference on Content-Based Multimedia Indexing},
pages = {178–182},
numpages = {5},
keywords = {pre-training, media memorability, cross-modal, CLIP},
location = {<conf-loc>, <city>Orleans</city>, <country>France</country>, </conf-loc>},
series = {CBMI '23}
}
```


