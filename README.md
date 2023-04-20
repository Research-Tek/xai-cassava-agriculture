![image](https://user-images.githubusercontent.com/52251022/233434198-54d7e335-6c33-4385-89ed-03d3ff0c406e.png)

Code in support for the publication.
 
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


