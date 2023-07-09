![image](https://user-images.githubusercontent.com/52251022/233434198-54d7e335-6c33-4385-89ed-03d3ff0c406e.png)

### Cite
```
@article{CHHETRI2023120955,
title = {Toward improving prediction accuracy and user-level explainability using deep learning and knowledge graphs: A study on cassava disease},
journal = {Expert Systems with Applications},
pages = {120955},
year = {2023},
issn = {0957-4174},
doi = {https://doi.org/10.1016/j.eswa.2023.120955},
url = {https://www.sciencedirect.com/science/article/pii/S0957417423014574},
author = {Tek Raj Chhetri and Armin Hohenegger and Anna Fensel and Mariam Aramide Kasali and Asiru Afeez Adekunle},
keywords = {Explainable AI (XAI), Agricultural sustainability, Knowledge graphs, Deep learning, Cassava},
abstract = {Food security is currently a major concern due to the growing global population, the exponential increase in food demand, the deterioration of soil quality, the occurrence of numerous diseases, and the effects of climate change on crop yield. Sustainable agriculture is necessary to solve this food security challenge. Disruptive technologies, such as of artificial intelligence, especially, deep learning techniques can contribute to agricultural sustainability. For example, applying deep learning techniques for early disease classification allows us to take timely action, thereby helping to increase the yield without inflicting unnecessary environmental damage, such as excessive use of fertilisers or pesticides. Several studies have been conducted on agricultural sustainability using deep learning techniques and also semantic web technologies such as ontologies and knowledge graphs. However, the three major challenges remain: (i) the lack of explainability of deep learning-based systems (e.g. disease information), especially to non-experts like farmers; (ii) a lack of contextual information (e.g. soil or plant information) and domain-expert knowledge in deep learning-based systems; and (iii) the lack of pattern learning ability of systems based on the semantic web, despite their ability to incorporate domain knowledge. Therefore, this paper presents the work on disease classification, addressing the challenges as mentioned earlier by combining deep learning and semantic web technologies, namely ontologies and knowledge graphs. The findings are: (i) 0.905 (90.5%) prediction accuracy on large noisy dataset; (ii) ability to generate user-level explanations about disease and incorporate contextual and domain knowledge; (iii) the average prediction latency of 3.8514 s on 5268 samples; (iv) 95% of users finding the explanation of the proposed method useful; and (v) 85% of users being able to understand generated explanations easily–show that the proposed method is superior to the state-of-the-art in terms of performance and explainability and is also suitable for real-world scenarios.}
}
```
 
### Softwares
|Libraries|Version|  
|---|---| 
|[Python](https://www.python.org) |3.10|    
|[Docker](https://www.docker.com)|20.10| 
|[Flake8](https://flake8.pycqa.org/en/latest/index.html)|4.0.1| 
|[FastAPI](https://fastapi.tiangolo.com)|0.75.1|
|[Owlready2](https://owlready2.readthedocs.io/en/v0.37/)|0.37|
|[Tensorflow](https://www.tensorflow.org)|2.x|
|[BentoML](https://docs.bentoml.org/en/latest/)|1.0.0a7|
|[Build](https://pypa-build.readthedocs.io/en/latest/)|0.7.0|
|[Pandas](https://pandas.pydata.org)|1.4.2|
|[Tqdm](https://tqdm.github.io)|4.64.0|

## Build 
# System (Training & Testing)

|Node Type|  Nodes | Cores/Node |  memory/Node |GPUs|
|-----|---------|-------|------------|--------------|
|GPU  |1     | 28 × Skylake     | 384 GB     |4 × Nvidia Tesla V100 |

# Build 

Use `make` to build the docker-containers for the ontology service and the decision engine:

```bash
  pipenv shell
  make docker-build
```

You can load the provided checkpoint for our best training result as a bentoml model:

```bash
cd vision-model
python3 checkpoint_to_bento_model.py
```

## Run

In order to run the complete application you will need to start the image classifier 
on a gpu enabled node with bentoml:

```bash
cd vision-model
bentoml serve ./service.py:svc --host 0.0.0.0
```

Make sure to correctly configure the service hostnames and image tags in `docker-compose.yml` 
and run the decision engine and ontology service with:

```
docker-compose up
```

## Training

To train the image classifier yourself download the [dataset](https://www.kaggle.com/datasets/tahsin/cassava-leaf-disease-merged) and 
follow the script `vision/training.py`.


