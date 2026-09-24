---
titulo: Research
antetitulo: Publications and thesis
entradilla: First-author papers and selected collaborations. Everything else lives on Google Scholar.
descripcion: Publications on video memorability, persuasion strategies and social perception.
nav: Research
orden: 2
---

I model **subjective perception** in multimedia: memorability, persuasion strategies and
social perception. The list below covers first-author papers and selected collaborations.
For everything else, see my
[Google Scholar profile](https://scholar.google.com/citations?user=1eHvsbsAAAAJ&hl=es).

## PhD thesis

### Modeling Subjective Perception in Multimedia with Large-Scale Multimodal Models

Universidad Politécnica de Madrid<!-- ← año de defensa y enlace al PDF, pendientes -->

Perceptual variables are annotated by people, and people disagree in ways that repeat.
The thesis argues that this disagreement is signal rather than noise, and builds
multimodal models for three tasks — memorability, persuasion and social perception —
around that idea.


## 2026

### Principled Evaluation of Multi-Label Persuasion in Advertisements with Large Vision-Language Models

**Iván Martín-Fernández**, Mihai Gabriel Constantin, Bogdan Ionescu, Manuel Gil-Martín, Fernando Fernández-Martínez
· *ACM TOMM* 22(7):1–27 · [10.1145/3788874](https://doi.org/10.1145/3788874)

Persuasion strategy detection treated as the multi-label problem it really is, with a principled
evaluation framework and input-agnostic baselines. Fine-tuning only the linear projector lifts
macro F1 on the image test set from **0.227** (best zero-shot) to **0.396**, and part of it
transfers to video; LoRA does not.

??? note "Abstract"

    The automatic detection of persuasive strategies in advertisements presents a uniquely multimodal challenge at the intersection of vision, language, and social cognition. While recent advances in Large Vision-Language Models (LVLMs) offer promising capabilities for such tasks, current approaches often rely on restrictive evaluation schemes that do not reflect the inherently multi-label nature of persuasive messaging. In this work, we reframe persuasion strategy detection as a genuine multi-label classification problem and propose a principled evaluation framework to enhance interpretability and robustness. We apply this approach to both image and video datasets, examine their characteristics, and introduce novel input-agnostic baselines that achieve macro F1 scores of 0.082 and 0.289 on the respective test sets. As part of this analysis, we study label co-occurrence patterns and dataset ambiguities, providing insights that inform both model interpretation and future dataset design. To assess the native capabilities of LVLMs, we benchmark three open source models—PaliGemma, PaliGemma2, and Qwen2.5-VL—on the image persuasion dataset. Under zero-shot conditions, we demonstrate that querying each strategy individually with a logit-based decision threshold outperforms guided text generation. The best-performing zero-shot model, Qwen2.5-VL, achieves a macro F1 score of 0.227 and a sample F1 score of 0.234 on the image test set, and 0.381 and 0.400 respectively on the video test set. We further explore and compare two lightweight fine-tuning strategies that update only small subsets of model parameters while keeping the remaining weights frozen: fine-tuning of the image-to-text tokens linear projection and Low Rank Adaptation (LoRA) of the language model. Linear projector fine-tuning yields a top macro F1 score of 0.396 on the image test set, marking a substantial improvement over zero-shot performance. To evaluate cross-modal generalization, we apply fine-tuned image models to the video dataset. Our experiments reveal that, while projection-based fine-tuning enables partial knowledge transfer from image to video (macro F1 = 0.416 on a testing subset), LoRA adaptation severely disrupts cross-modal performance (macro F1 = 0.189). Finally, we perform a per-strategy performance analysis, looking into annotator- and data-centric factors that may influence LVLM performance. These findings highlight the viability of open-weight LVLMs for fine-grained persuasion analysis and suggest efficient pathways for domain-specific adaptation under realistic resource constraints.

??? quote "BibTeX"

    ```bibtex
    @article{10.1145/3788874,
        author = {Mart\'{\i}n-Fern\'{a}ndez, Iv\'{a}n and Constantin, Mihai Gabriel and Ionescu, Bogdan and Gil-Mart\'{\i}n, Manuel and Fern\'{a}ndez-Mart\'{\i}nez, Fernando},
        title = {Principled Evaluation of Multi-Label Persuasion in Advertisements with Large Vision-Language Models},
        journal = {ACM Transactions on Multimedia Computing, Communications, and Applications},
        volume = {22},
        number = {7},
        pages = {1--27},
        year = {2026},
        publisher = {Association for Computing Machinery},
        doi = {10.1145/3788874}
    }
    ```

### A comprehensive study on contrastive pre-training and fine tuning of vision and text transformers for video memorability prediction

**Iván Martín-Fernández**, Sergio Esteban-Romero, Manuel Gil-Martín, Fernando Fernández-Martínez
· *Multimedia Tools and Applications* 85(1):30 · [10.1007/s11042-026-21260-3](https://doi.org/10.1007/s11042-026-21260-3)

FCLIP, a CLIP further pre-trained on memorability image–text pairs, compared fairly against
unimodal encoders of matched architecture and size. Its image encoders reach an SRCC of
**0.672** on Memento10k and its text encoders 0.632, both ahead of their unimodal baselines.

??? note "Abstract"

    Video memorability prediction has emerged as a key challenge for improving information retrieval, content design, and user engagement. Prior work has shown that semantic cues play a crucial role in determining memorability, with recent studies leveraging Contrastive Language-Image Pre-training (CLIP) encoders to incorporate semantic information. However, the specific improvements attributable to CLIP models remain unclear, as few studies systematically compare their performance against equivalent unimodal encoders or explore fine-tuning strategies. This work addresses that gap through a comprehensive, controlled evaluation of CLIP-based and unimodal encoders for video memorability prediction. We propose FCLIP, a domain-adapted extension of CLIP that undergoes additional contrastive pre-training on memorability-specific image-text pairs. Our experiments assess both feature extraction and supervised fine-tuning, ensuring fair comparisons across models with matched architecture and parameter count. Results show that FCLIP image encoders achieve a Spearman Rank Correlation Coefficient (SRCC) of 0.672 on the Memento10k dataset, significantly outperforming unimodal Vision Transformers. FCLIP text encoders similarly outperform unimodal baselines, reaching an SRCC of 0.632. These findings demonstrate that contrastive learning and domain adaptation substantially improve memorability prediction, highlighting the importance of semantic and multimodal pre-training in developing advanced content analysis systems.


??? quote "BibTeX"

    ```bibtex
    @article{10.1007/s11042-026-21260-3,
        author = {Mart{\'\i}n-Fern{\'a}ndez, Iv{\'a}n and Esteban-Romero, Sergio and Gil-Mart{\'\i}n, Manuel and Fern{\'a}ndez-Mart{\'\i}nez, Fernando},
        title = {A comprehensive study on contrastive pre-training and fine tuning of vision and text transformers for video memorability prediction},
        journal = {Multimedia Tools and Applications},
        volume = {85},
        number = {1},
        pages = {30},
        year = {2026},
        doi = {10.1007/s11042-026-21260-3}
    }
    ```

### A Case Study on Large Visual-Language Model Attention Explainability After Adaptation Using Persuasion Strategies in Advertisements

**Iván Martín-Fernández**, Mihai Gabriel Constantin, Bogdan Ionescu, Sergio Esteban-Romero, Fernando Fernández-Martínez, Manuel Gil-Martín
· *MMM 2026*, LNCS 16412, 103–116 · [10.1007/978-981-95-6950-2_8](https://doi.org/10.1007/978-981-95-6950-2_8)

Fine-tuning only PaliGemma's linear projector takes persuasion-strategy accuracy from 19.6% to
**66.0%**. The attention maps show why: sharper focus on image regions, less noise, and distinct
patterns for each strategy.

??? note "Abstract"

    Large Vision-Language Models (LVLMs) demonstrate impressive capabilities across multimodal tasks, yet their inner workings remain poorly understood, particularly in subjective domains that involve human perception. In this paper, we examine how attention patterns in LVLMs shift with task-specific adaptation, using the task of detecting persuasion strategies in advertisements as a case study. This task attempts to model 16 different techniques used to influence behavior or decision-making in marketing. In particular, we leverage PaliGemma to classify persuasion strategies by applying a score-based logit postprocessing approach. Under this setting, we compare zero-shot performance with fine-tuning of the linear projector that maps image features to the language embedding space, achieving 19.6% and 66.0% accuracy, respectively, on the test set of the Persuasion Strategies in Advertisements corpus. We perform an exhaustive model interpretability analysis to understand how this lightweight adaptation method influences downstream performance, showing that fine-tuning sharpens attention to image regions and reduces noise. Fine-tuning makes image token representations more task-specific, evidenced by distinct attention patterns across persuasion strategies. These findings motivate deeper exploration into LVLM interpretability.

??? quote "BibTeX"

    ```bibtex
    @inproceedings{10.1007/978-981-95-6950-2_8,
        author = {Mart{\'\i}n-Fern{\'a}ndez, Iv{\'a}n and Constantin, Mihai Gabriel and Ionescu, Bogdan and Esteban-Romero, Sergio and Fern{\'a}ndez-Mart{\'\i}nez, Fernando and Gil-Mart{\'\i}n, Manuel},
        title = {A Case Study on Large Visual-Language Model Attention Explainability After Adaptation Using Persuasion Strategies in Advertisements},
        booktitle = {MultiMedia Modeling},
        series = {Lecture Notes in Computer Science},
        volume = {16412},
        pages = {103--116},
        year = {2026},
        publisher = {Springer Nature Singapore},
        isbn = {978-981-95-6950-2},
        doi = {10.1007/978-981-95-6950-2_8}
    }
    ```

### Overview of The MediaEval 2026 Predicting Movie and Commercial Memorability Task

**Iván Martín-Fernández**, Aashutosh Ganesh, Mihai Gabriel Constantin, Claire-Hélène Demarty, Manuel Gil-Martín, Sebastian Halder, Bogdan Ionescu, Rukiye Savran Kiziltepe, Ana Matran-Fernandez, Alba G. Seco de Herrera
· MediaEval 2026, Predicting Movie and Commercial Memorability task · [PDF](https://2026.multimediaeval.com/paper6.pdf)

The 2026 edition of the task I co-organise: four subtasks spanning movie clips, EEG-based
recognition, commercials and brands, now with colour palettes and movie metadata among the features.

??? note "Abstract"

    This paper presents the 2026 edition of the MediaEval Predicting Movie and Commercial Memorability Task. Much like the previous edition, the benchmark is structured around four different subtasks: (1.1) predicting long-term memorability using a movie clip, (1.2) classifying successful recognition using participants EEG signals, (2.1) predicting long-term commercial video memorability and (2.2) predicting the brand memorability associated with a video clip. This edition builds upon previous years, introducing an expanded feature set that integrates colour palettes and movie metadata to enable modelling strategies that go beyond video characteristics.

??? quote "BibTeX"

    ```bibtex
    @inproceedings{martin2026overview,
        author = {Mart{\'\i}n-Fern{\'a}ndez, Iv{\'a}n and Ganesh, Aashutosh and Constantin, Mihai Gabriel and Demarty, Claire-H{\'e}l{\`e}ne and Gil-Mart{\'\i}n, Manuel and Halder, Sebastian and Ionescu, Bogdan and Savran Kiziltepe, Rukiye and Matran-Fernandez, Ana and Seco de Herrera, Alba G.},
        title = {Overview of The MediaEval 2026 Predicting Movie and Commercial Memorability Task},
        booktitle = {MediaEval'26: Multimedia Evaluation Workshop},
        address = {Amsterdam, Netherlands},
        year = {2026},
        url = {https://2026.multimediaeval.com/paper6.pdf}
    }
    ```

### Predicting Long-Term Movie Recall from EEG with Deep Models

**Iván Martín-Fernández**, Jaime León, Sergio Esteban-Romero, Manuel Gil-Martín, Fernando Fernández-Martínez
· MediaEval 2026, Predicting Movie and Commercial Memorability task · [PDF](https://2026.multimediaeval.com/paper19.pdf)

Lightweight CNNs, EEGNet and pre-trained SignalJEPA, subject-independent and subject-dependent.
The best official result, an AUC of **0.582**, comes from adapting SignalJEPA to each subject:
subject variability is still the bottleneck.

??? note "Abstract"

    This paper describes the THAU-UPM submissions to the MediaEval 2026 Predicting Movie and Commercial Memorability Task, focusing on EEG-based prediction of movie recall. We compare lightweight convolutional architectures, EEGNet, and pre-trained SignalJEPA representations under subject-independent and subject-dependent training regimes. Our results show that deep learning models can capture weak but meaningful signals from EEG, although performance remains below that of previous feature-based approaches. The best official test result is obtained with subject-dependent adaptation of pre-trained SignalJEPA features, reaching an AUC of 0.582 and suggesting that subject variability remains a major bottleneck for EEG-based recall prediction.

??? quote "BibTeX"

    ```bibtex
    @inproceedings{martin2026predicting,
        author = {Mart{\'\i}n-Fern{\'a}ndez, Iv{\'a}n and Le{\'o}n, Jaime and Esteban-Romero, Sergio and Gil-Mart{\'\i}n, Manuel and Fern{\'a}ndez-Mart{\'\i}nez, Fernando},
        title = {Predicting Long-Term Movie Recall from EEG with Deep Models},
        booktitle = {MediaEval'26: Multimedia Evaluation Workshop},
        address = {Amsterdam, Netherlands},
        year = {2026},
        url = {https://2026.multimediaeval.com/paper19.pdf}
    }
    ```

### A Review of Computational Memorability: A Benchmark Framework

Mihai Gabriel Constantin, Claire-Hélène Demarty, Camilo Fosco, Sebastian Halder, Graham Healy, Bogdan Ionescu, Stefan Valentin Luncanu, **Iván Martín-Fernández**, Ana Matran-Fernandez, Rukiye Savran Kiziltepe, Alan F. Smeaton, Liviu-Daniel Stefan, Lorin Sweeney, Alba García Seco de Herrera
· *International Journal of Computer Vision* 134(6):298 · [10.1007/s11263-026-02880-6](https://doi.org/10.1007/s11263-026-02880-6)

A review of the MediaEval Predicting Video Memorability benchmark across its 2018–2023 editions:
what it has taught the field, and what is still open — interpretability, and memorability that
is subjective and depends on context.

??? note "Abstract"

    One of the powers of visual media lies in its ability to create a lasting impression on the viewer's memory. In this digital age, where media is abundant and attention spans are fleeting, the task of predicting which content will stick in the viewer's mind has become a critical challenge in computer vision. Computational memorability seeks to address this by developing models that estimate how memorable a piece of media is likely to be. In this review we focus on the MediaEval Predicting Video Memorability benchmark, a recurring evaluation task that has run annually since 2018. This benchmark provides a unique and consistent framework for researchers to compare and refine their memorability prediction techniques using standardised datasets and metrics. Its reproducible framework has proven invaluable for tracking progress and fostering innovation in this rapidly evolving domain. We analyse the evolution of the benchmark across its 2018–2023 editions, discussing the challenges that still remain, such as the need for more interpretability in models and the difficulty of predicting subjective and context-dependent memorability. By analysing and synthesising the collective insights gained from this task, we endeavour to inspire new avenues of inquiry and drive progress towards a more comprehensive understanding of this topic.

??? quote "BibTeX"

    ```bibtex
    @article{10.1007/s11263-026-02880-6,
        author = {Constantin, Mihai Gabriel and Demarty, Claire-H{\'e}l{\`e}ne and Fosco, Camilo and Halder, Sebastian and Healy, Graham and Ionescu, Bogdan and Luncanu, Stefan Valentin and Mart{\'\i}n-Fern{\'a}ndez, Iv{\'a}n and Matran-Fernandez, Ana and Savran Kiziltepe, Rukiye and Smeaton, Alan F. and Stefan, Liviu-Daniel and Sweeney, Lorin and Garc{\'\i}a Seco de Herrera, Alba},
        title = {A Review of Computational Memorability: A Benchmark Framework},
        journal = {International Journal of Computer Vision},
        volume = {134},
        number = {6},
        pages = {298},
        year = {2026},
        doi = {10.1007/s11263-026-02880-6}
    }
    ```

### A Dataset with Bilingual TV Commands for Silent Speech Interfaces Using Electroencephalographic Signals

Mario Lobo-Alonso, **Iván Martín-Fernández**, I. Oropesa, Roberto Barra-Chicote, George Kontaxakis, Rubén San-Segundo
· *Scientific Data* · [10.1038/s41597-026-07745-8](https://doi.org/10.1038/s41597-026-07745-8)

TESSCCo: EEG recorded while five TV commands are spoken aloud and covertly, in English and
Spanish — **7,936** epochs, 11.02 hours, 32 channels.

??? note "Abstract"

    This paper introduces TESSCCo (TV-control EEG-based Silent Speech Command Corpus), a new dataset including electroencephalography (EEG) signals during Overt Speech (OS) and Covert Speech (CS) in different languages. The dataset comprises repetitions of five different commands pronounced covertly and overtly in English and Spanish from 21 healthy native Spanish speakers (13 male, 8 female, 23 ± 2 years old), while EEG and audio were recorded. In addition, 3 non-native healthy Spanish speakers were recorded under the same circumstances (3 male, 23.3 ± 0.6 years old). A total of 7936 available epochs (i.e., 11.02 hours of data) were recorded with a 32 channel, 256 Hz sampling rate Water based EEG device. The database was designed to maximize the number of different analysis involving EEG signals. The final number of epochs, as well as the statistical analysis (showing significance in Broca's and Wernicke's areas) and machine learning experiments (with subjects exceeding the chance level with basic machine learning models), show that this material is a valuable resource for research on future ways of communication.

??? quote "BibTeX"

    ```bibtex
    @article{10.1038/s41597-026-07745-8,
        author = {Lobo-Alonso, Mario and Mart{\'\i}n-Fern{\'a}ndez, Iv{\'a}n and Oropesa, I. and Barra-Chicote, Roberto and Kontaxakis, George and San-Segundo, Rub{\'e}n},
        title = {A Dataset with Bilingual TV Commands for Silent Speech Interfaces Using Electroencephalographic Signals},
        journal = {Scientific Data},
        year = {2026},
        doi = {10.1038/s41597-026-07745-8}
    }
    ```

### Quest for Insight: Contextual and Popularity Factors in Movie Memorability Prediction

Aashutosh Ganesh, **Iván Martín-Fernández**, Mirela Popa, Manuel Gil-Martín, Fernando Fernández-Martínez, Nava Tintarev
· MediaEval 2026, Predicting Movie and Commercial Memorability task · [PDF](https://2026.multimediaeval.com/paper24.pdf)

Is a clip memorable because the film is popular, or because you recognise it? Recognisability
matters; popularity and genre barely do.

??? note "Abstract"

    While the influence of visual factors on movie memorability has been extensively studied, the roles of film recognizability, genre, and popularity remain underexplored. In this Quest for Insight paper, we investigate these factors using the additional metadata provided in this edition of the MediaEval Memorability Task. We use the "neutral" and "typical" labels as indicators of whether a film can be recognized from a given clip. To approximate film popularity, we leverage user ratings from the MovieLens dataset, while genre-level analyses are conducted using the provided genre annotations. Our analysis reveals substantial differences between the memorability distributions of neutral and typical clips, suggesting that recognizability plays an important role in memorability prediction. In contrast, we find little to no correlation between film popularity and clip memorability. Similarly, memorability scores exhibit only limited variation across film genres. These findings suggest that neither popularity nor genre substantially influences movie-clip memorability, whereas the extent to which a film is recognizable from a clip may be a key factor in understanding what makes content memorable.

??? quote "BibTeX"

    ```bibtex
    @inproceedings{ganesh2026quest,
        author = {Ganesh, Aashutosh and Mart{\'\i}n-Fern{\'a}ndez, Iv{\'a}n and Popa, Mirela and Gil-Mart{\'\i}n, Manuel and Fern{\'a}ndez-Mart{\'\i}nez, Fernando and Tintarev, Nava},
        title = {Quest for Insight: Contextual and Popularity Factors in Movie Memorability Prediction},
        booktitle = {MediaEval'26: Multimedia Evaluation Workshop},
        address = {Amsterdam, Netherlands},
        year = {2026},
        url = {https://2026.multimediaeval.com/paper24.pdf}
    }
    ```


## 2025

### Parameter-Efficient Adaptation of Large Vision–Language Models for Video Memorability Prediction

**Iván Martín-Fernández**, Sergio Esteban-Romero, Fernando Fernández-Martínez, Manuel Gil-Martín
· *Sensors* 25(6):1661 · [10.3390/s25061661](https://doi.org/10.3390/s25061661)

QLoRA fine-tuning turns Qwen-VL from a language model into a memorability score regressor,
reaching a state-of-the-art SRCC of **0.744** on Memento10k.

??? note "Abstract"

    The accurate modelling of video memorability, or the intrinsic properties that render a piece of audiovisual content more likely to be remembered, will facilitate the development of automatic systems that are more efficient in retrieving, classifying and generating impactful media. Recent studies have indicated a strong correlation between the visual semantics of video and its memorability. This underscores the importance of developing advanced visual comprehension abilities to enhance model performance. It has been demonstrated that Large Vision–Language Models (LVLMs) demonstrate exceptional proficiency in generalist, high-level semantic comprehension of images and video, due to their extensive multimodal pre-training on a vast scale. This work makes use of the vast generalist knowledge of LVLMs and explores efficient adaptation techniques with a view to utilising them as memorability predictors. In particular, the Quantized Low-Rank Adaptation (QLoRA) technique is employed to fine-tune the Qwen-VL model with memorability-related data extracted from the Memento10k dataset. In light of existing research, we propose a particular methodology that transforms Qwen-VL from a language model to a memorability score regressor. Furthermore, we consider the influence of selecting appropriate LoRA hyperparameters, a design aspect that has been insufficiently studied. We validate the LoRA rank and alpha hyperparameters using 5-Fold Cross-Validation and evaluate our best configuration on the official testing portion of the Memento10k dataset, obtaining a state-of-the-art Spearman Rank Correlation Coefficient (SRCC) of 0.744. Consequently, this work represents a significant advancement in modelling video memorability through high-level semantic understanding.

??? quote "BibTeX"

    ```bibtex
    @article{s25061661,
        article-number = {1661},
        author = {Mart{\'\i}n-Fern{\'a}ndez, Iv{\'a}n and Esteban-Romero, Sergio and Fern{\'a}ndez-Mart{\'\i}nez, Fernando and Gil-Mart{\'\i}n, Manuel},
        doi = {10.3390/s25061661},
        issn = {1424-8220},
        journal = {Sensors},
        number = {6},
        title = {Parameter-Efficient Adaptation of Large Vision---Language Models for Video Memorability Prediction},
        volume = {25},
        year = {2025}
    }
    ```


## 2024

### Larger Encoders, Smaller Regressors: Label Dimensionality Reduction and Multimodal LLMs as Feature Extractors for Predicting Social Perception

**Iván Martín-Fernández**, Sergio Esteban-Romero, Jaime Bellver-Soler, Fernando Fernández-Martínez, Manuel Gil-Martín
· *MuSe'24* @ ACM Multimedia, 20–27 · [10.1145/3689062.3689083](https://doi.org/10.1145/3689062.3689083)

Frozen multimodal LLMs as feature extractors for 16 social-perception attributes — plus a
warning worth its own paper: the same Pearson coefficient can come from two very different
prediction sets, one of them far less variable than the other.

??? note "Abstract"

    Designing reliable automatic models for social perception can contribute to a better understanding of human behavior, enabling more trustworthy experiences in the multimedia on-line communication environment. However, predicting social attributes from video data remains challenging due to the complex interplay of visual, auditory, and linguistic cues. In this paper, we address this challenge by investigating the effectiveness of Multimodal Large Language Models (MM-LLMs) for feature extraction in the MuSe-Perception challenge. Firstly, our analysis of the novel LMU-ELP dataset has revealed high correlations between certain perceptual dimensions, motivating using a single regression model for all 16 social attributes to be predicted for a set of speakers appearing in recorded video clips. We demonstrate that dimensionality reduction through Principal Component Analysis (PCA) can be applied to the label space without a relevant performance loss. Secondly, by employing frozen MM-LLMs as feature extractors, we explore their ability to capture perception-related information. We extract sequence embeddings from the Qwen-VL and Qwen-Audio models and train a Multi-Layer Perceptron over the attention-pooled vectors for each one of the encoders, obtaining a mean Pearson correlation of 0.22 using the average predictions for both models. Our best result of 0.31 is achieved by training the same architecture over the baseline vit-ver and w2v-msp features, which motivates further exploration on how to effectively leverage advanced MM-LLMs as feature extractors. Lastly, a post hoc analysis of our results highlights the limitations of Pearson correlation for evaluating regression performance in this context. In particular, a similar Pearson coefficient can be obtained with two very different prediction sets displaying different levels of variability. We take this result as a call to action in exploring alternative metrics to assess the regression performance for the task.

??? quote "BibTeX"

    ```bibtex
    @inproceedings{10.1145/3689062.3689083,
        author = {Mart\'{\i}n-Fern\'{a}ndez, Iv\'{a}n and Esteban-Romero, Sergio and Bellver-Soler, Jaime and Fern\'{a}ndez-Mart\'{\i}nez, Fernando and Gil-Mart\'{\i}n, Manuel},
        title = {Larger Encoders, Smaller Regressors: Exploring Label Dimensionality Reduction and Multimodal Large Language Models as Feature Extractors for Predicting Social Perception},
        year = {2024},
        isbn = {9798400711992},
        publisher = {Association for Computing Machinery},
        address = {New York, NY, USA},
        doi = {10.1145/3689062.3689083},
        booktitle = {Proceedings of the 5th on Multimodal Sentiment Analysis Challenge and Workshop: Social Perception and Humor},
        pages = {20--27},
        series = {MuSe'24}
    }
    ```


## 2023

### Exploring Video Transformers and Automatic Segment Selection for Memorability Prediction

**Iván Martín-Fernández**, Sergio Esteban-Romero, Jaime Bellver-Soler, Manuel Gil-Martín, Fernando Fernández-Martínez
· MediaEval 2023, Predicting Video Memorability task · [CEUR-WS](https://ceur-ws.org/Vol-3658/paper25.pdf)

A pre-trained ViViT with annotator-independent segment selection based on visual saliency.
Fine-tuning clearly beats a scratch-trained baseline; the choice of segment, less so.

??? note "Abstract"

    This paper summarises THAU-UPM's approach and results from the MediaEval 2023 Predicting Video Memorability task. Focused on the generalisation subtask, our work leverages a pre-trained Video Vision Transformer (ViViT), fine-tuned on memorability-related data, to model temporal and spatial relationships in videos. We propose novel, annotator-independent automatic segment selection methods grounded in visual saliency. These methods identify the most relevant video frames prior to conducting memorability score estimation. This selection process is implemented during both training and evaluation phases. Our study demonstrates the effectiveness of fine-tuning the ViViT model compared to a scratch-trained baseline, emphasising the importance of pre-training for predicting memorability. However, the model shows comparable sensitivity to both saliency-based and naive segment selection methods, suggesting that fine-tuning may harness similar benefits from various video segments. These results underscore the robustness of our approach but also signal the need for ongoing research.

??? quote "BibTeX"

    ```bibtex
    @article{martin2023exploring,
        title = {Exploring Video Transformers and Automatic Segment Selection for Memorability Prediction},
        author = {Mart{\'\i}n-Fern{\'a}ndez, Iv{\'a}n and Esteban-Romero, Sergio and Bellver-Soler, Jaime and Gil-Mart{\'\i}n, Manuel and Fern{\'a}ndez-Mart{\'\i}nez, Fernando},
        year = {2023}
    }
    ```

### Video Memorability Prediction From Jointly-learnt Semantic and Visual Features

**Iván Martín-Fernández**, Ricardo Kleinlein, Cristina Luna-Jiménez, Manuel Gil-Martín, Fernando Fernández-Martínez
· *CBMI '23*, 178–182 · [10.1145/3617233.3617260](https://doi.org/10.1145/3617233.3617260)

Fine-tuning CLIP encoders on memorability raises SRCC in the text domain from
0.538 ± 0.007 to **0.575 ± 0.007** on Memento10k, with a milder trend in the visual domain.

??? note "Abstract"

    The memorability of a video is defined as an intrinsic property of its visual features that dictates the fraction of people who recall having watched it on a second viewing within a memory game. Still, unravelling what are the key features to predict memorability remains an obscure matter. This challenge is addressed here by fine-tuning text and image encoders using a cross-modal strategy known as Contrastive Language-Image Pre-training (CLIP). The resulting video-level data representations learned include semantics and topic-descriptive information as observed from both modalities, hence enhancing the predictive power of our algorithms. Our proposal achieves in the text domain a significantly greater Spearman Rank Correlation Coefficient (SRCC) than a default pre-trained text encoder (0.575 ± 0.007 and 0.538 ± 0.007, respectively) over the Memento10K dataset. A similar trend, although less pronounced, can be noticed in the visual domain. We believe these findings signal the potential benefits that cross-modal predictive systems can extract from being fine-tuned to the specific issue of media memorability.

??? quote "BibTeX"

    ```bibtex
    @inproceedings{10.1145/3617233.3617260,
        author = {Mart\'{\i}n-Fern\'{a}ndez, Iv\'{a}n and Kleinlein, Ricardo and Luna-Jim\'{e}nez, Cristina and Gil-Mart\'{\i}n, Manuel and Fern\'{a}ndez-Mart\'{\i}nez, Fernando},
        title = {Video Memorability Prediction From Jointly-learnt Semantic and Visual Features},
        year = {2023},
        isbn = {9798400709128},
        publisher = {Association for Computing Machinery},
        address = {New York, NY, USA},
        doi = {10.1145/3617233.3617260},
        booktitle = {Proceedings of the 20th International Conference on Content-Based Multimedia Indexing},
        pages = {178--182},
        series = {CBMI '23}
    }
    ```
