"""
Simple script that loads a PyTorch checkpoint
and saves it as a bentoml model.
"""
import bentoml
import torch
import torch.nn as nn
import timm
from torchsummary import summary

PATH="./volo_d2_384_fold0_best.pth"

class CFG():
    target_size = 5

# ====================================================
# MODEL
# ====================================================
class CustomEfficientNet(nn.Module):
    def __init__(self, model_name="efficientnet", pretrained=False):
        super().__init__()
        self.model = timm.create_model(CFG.model_name, pretrained=pretrained)
        n_features = self.model.classifier.in_features
        self.model.classifier = nn.Linear(n_features, CFG.target_size)
        
    def forward(self, x):
        x = self.model(x)
        return x


class CustomResNext(nn.Module):
    def __init__(self, model_name='resnext50_32x4d', pretrained=False):
        super().__init__()
        self.model = timm.create_model(model_name, pretrained=pretrained)
        n_features = self.model.fc.in_features
        self.model.fc = nn.Linear(n_features, CFG.target_size)
        
    def forward(self, x):
        x = self.model(x)
        return x
            
class CustomVolo(nn.Module):
    def __init__(self, model_name='volo_d1_224', pretrained=False):
        super().__init__()
        self.model = timm.create_model(model_name, pretrained=pretrained)
        self.model.reset_classifier(num_classes=CFG.target_size)
        
    def forward(self, x):
        x = self.model(x)
        return x

checkpoint = torch.load(PATH)
model = CustomVolo("volo_d2_384", pretrained=True)
print("loading model")
model.load_state_dict(checkpoint['model'])
print("model loaded")
print("saving model")
tag = bentoml.pytorch.save(name="cassava_volo_d2_384", model=model)
print(tag)
print("finished")


