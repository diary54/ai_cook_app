import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transforms


# 画像前処理（転移学習用正規化追加）
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225]),
])

def transform_image(img):
    """
    PIL.Image -> 正規化済み Tensor (1, C, H, W)
    """
    return transform(img).unsqueeze(0)


# 軽量モデル ResNet18 + fc 512->12
class Net(nn.Module):
    def __init__(self, num_classes=12):
        super().__init__()
        self.model = models.resnet18(
            weights=models.ResNet18_Weights.DEFAULT
        )
        # 出力層をクラス数に変更
        self.model.fc = nn.Linear(512, num_classes)

    def forward(self, x):
        return self.model(x)



    