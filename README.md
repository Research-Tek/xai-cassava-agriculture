# Towards an Explainable Artificial Intelligence Using Deep Learning and Knowledge Graphs: A Study on Cassava Disease
### Abstract 
Food security is currently a major concern due to the growing global population, the exponential increase in food demand, the deterioration of soil quality, the occurrence of numerous diseases, and the effects of climate change on crop yield. Sustainable agriculture is necessary to solve this food security issue. Disruptive technologies, such as artificial intelligence, especially, deep learning (DL) techniques can contribute to agricultural sustainability. For example, applying DL techniques for early disease classification allows us to take timely action, thereby helping to increase the yield without inflicting unnecessary environmental damage, such as excessive use of fertilisers or pesticides. Several studies have been conducted on agricultural sustainability using DL techniques and also semantic web technologies such as ontologies and knowledge graphs (KGs). However, the three major challenges remain: (i) the lack of explainability of DL-based systems (e.g. disease information), especially to non-experts like farmers; (ii) a lack of contextual information (e.g. soil or plant information) and domain-expert knowledge in DL-based systems; and (iii) the lack of pattern learning ability of systems based on the semantic web, despite their ability to incorporate domain knowledge. Therefore, we present our work on disease classification, addressing the challenges as mentioned earlier by combining DL and semantic web technologies, namely ontologies and KGs. The experimental outcome of our work demonstrates that the proposed method, which incorporates contextual information and domain knowledge using KGs when combined with DL, is advantageous in terms of performance compared to the state-of-the-art and also in terms of explainability.

### Authors
- Tek Raj Chhetri
- Armin Hohenegger
- Anna Fensel
- Kasali Mariam Aramide
- Asiru Afeez Adekunle

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


