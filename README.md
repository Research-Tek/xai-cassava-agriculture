# Towards an Explainable AI System Using Deep Learning and Knowledge Graphs: A Case Study on Agricultural Sustainability
### Abstract 
Food security is currently a major concern due to the growing global population, the exponential increase in food demand, the deterioration of soil quality, the occurrence of numerous diseases, and the effects of climate change on crop yield. Sustainable agriculture is necessary to solve this food security issue. Disruptive technologies, such as artificial intelligence, especially, deep learning (DL) techniques can contribute to agricultural sustainability. For example, applying DL techniques for early disease classification allows us to take timely action, thereby helping to increase the yield without inflicting unnecessary environmental damage, such as excessive use of fertilizers or pesticides. Several studies have been conducted on agricultural sustainability using DL techniques and also semantic web technologies such as ontologies and knowledge graphs (KGs). However, the three major challenges remain: (i) the lack of explainability of DL-based systems, especially to non-experts like farmers; (ii) a lack of contextual information (e.g., soil or plant information) and domain-expert knowledge in DL-based systems; and (iii) the lack of pattern learning ability of systems based on the semantic web, despite their ability to incorporate domain knowledge. Therefore, we present our work on disease classification, addressing the challenges as mentioned earlier by combining DL and semantic web technologies, namely ontologies and KGs. The experimental outcome of our work demonstrates that the proposed method is advantageous in terms of both performance and explainability.

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

# Build 

Use `make` to build the docker-containers for the ontology service and the decision engine:

```bash
  pipenv shell
  make docker-build
```


