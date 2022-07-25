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
|Python |3.10|    
|Docker|20.x| 
|Owlready2|0.3| 
|Fastapi|0.3|
|Bentoml|0.3|
|Tensorflow|2|

# Build 

Use `make` to build the docker-containers for the ontology service and the decision engine:

```bash
pipenv shell
make docker-build
```


