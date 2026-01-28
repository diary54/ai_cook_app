import torch
import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transforms


transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),  # (H, W, C) → (C, H, W), [0,1]
])

def transform_image(img):
    img = transform(img)
    img = img.unsqueeze(0)  # batch 次元追加
    return img

class Net(nn.Module):

    def __init__(self):
        super().__init__()

        self.feature = models.resnet50(weights=models.ResNet50_Weights.DEFAULT)
        for param in self.feature.parameters():
            param.requires_grad = False

        self.fc = nn.Linear(1000, 12)

    def forward(self, x):
        h = self.feature(x)
        h = self.fc(h)
        return h


    