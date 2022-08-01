from typing import Dict

import bentoml
from bentoml.io import Image, JSON
import numpy as np
from PIL.Image import Image as PILImage
from pydantic import BaseModel
import albumentations as A
from albumentations.pytorch import ToTensorV2

labels = [
    'cassava_bacterial_blight',
    'cassava_brown_streak_disease',
    'cassava_green_mottle',
    'cassava_mosaic_disease',
    'healthy',
]


class Prediction(BaseModel):
    disease_prediction: Dict[str, float]


cassava_runner = bentoml.pytorch.load_runner("cassava_volo_d2_384:xvl4pbqoiwwcvygv")

svc = bentoml.Service(
    name="cassava_classifier",
    runners=[
        cassava_runner,
    ],
)


def softmax(x):
    return np.exp(x)/sum(np.exp(x))


def preprocess_image(image: PILImage) -> "np.ndarray":
    image = np.array(image, dtype=np.float32)
    transform =  A.Compose([
        A.Resize(384, 384),
        A.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225],
        ),
        ToTensorV2(),
    ])
    image = transform(image=image)['image']
    print(type(image))
          
    return image


@svc.api(input=Image(), output=JSON(pydantic_model=Prediction))
async def predict_image(f: PILImage) -> "np.ndarray":
    assert isinstance(f, PILImage)
    arr = preprocess_image(f)
    pred = await cassava_runner.async_run(arr)
    pred = softmax(pred)
    print(pred)
    
    disease_vector = {label: pred[i] for i, label in enumerate(labels)}

    return Prediction(disease_prediction=disease_vector).dict()
