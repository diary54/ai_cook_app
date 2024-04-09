import torch.nn as nn
import torchvision.models as models
import tensorflow as tf
import numpy as np

def transform_image(img):
    # 画像の前処理を定義する
    img = img.resize((224, 224)) 
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    img_array = np.transpose(img_array, (0, 3, 1, 2))

    return img_array

class Net(nn.Module):

    def __init__(self):
        super().__init__()

        self.feature = models.resnet50(pretrained=True)
        for param in self.feature.parameters():
            param.requires_grad = False
        self.fc = nn.Linear(1000, 12) 

    def forward(self, x):
        h = self.feature(x)
        h = self.fc(h)
        return h

    