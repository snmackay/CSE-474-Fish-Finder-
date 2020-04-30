import numpy as np
import torch
from torch import nn
from torch import optim
import torch.nn.functional as F
from torchvision import datasets, transforms, models
import torchvision.transforms as transforms
import io
import json
from PIL import Image

model = torch.load('model.pth', map_location=torch.device('cpu'))
def main():
    model.eval()
    data_dir = '../MLProj_1/jpeg/'
    with open(data_dir+'jpeg.jpg', 'rb') as f:
        image_bytes = f.read()
        tensor = transform_image(image_bytes=image_bytes)
    print(tensor)
    print("Prediction: " + str(get_prediction(image_bytes)))

def transform_image(image_bytes):
    my_transforms = transforms.Compose([transforms.Resize(224), transforms.ToTensor()])
    image = Image.open(io.BytesIO(image_bytes))
    return my_transforms(image).unsqueeze(0)


def get_prediction(image_bytes):
    tensor = transform_image(image_bytes=image_bytes)
    outputs = model.forward(tensor)
    _, y_hat = outputs.max(1)
    predicted_idx = str(y_hat.item())
    return predicted_idx


if __name__ == '__main__':
    main()
