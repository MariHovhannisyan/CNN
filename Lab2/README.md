### **[CIFAR-10 Image Classification](https://github.com/MariHovhannisyan/CNN/blob/master/Lab2/lab2_CNN.ipynb)**

This project uses a pre-trained ResNet18 model with transfer learning to classify images from the CIFAR-10 dataset. It includes data augmentation, custom training loops, and performance visualization.

---

## Model Overview

- **Architecture**: Pre-trained ResNet18 from `torchvision.models`
- **Fine-tuning**:
  - Shallow layers are frozen
  - Only `layer3`, `layer4`, and the `fc` layers are trained
- **Final layer**: Replaced with `Dropout + Linear(10)` to match CIFAR-10 classes

---

## Features

- Data Augmentation:
  - Random crop, horizontal flip, resize
- Normalization for faster convergence
- Label smoothing for regularization
- Cosine annealing learning rate scheduler
- Train/validation loss and accuracy tracking
- GPU support (automatically uses CUDA if available)

---

## Evaluation Metrics

- Accuracy (%)
- Training and validation loss per epoch
- Real-time visualization of learning curves