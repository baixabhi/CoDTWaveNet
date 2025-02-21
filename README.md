# CoDTWaveNet

## Overview
This project focuses on chest radiology analysis using a deep learning model. The goal is to achieve high accuracy while keeping the model lightweight.

## Dataset
- The dataset contains chest radiology images.
- Preprocessing includes resizing, normalization, and augmentation.

## Model
- The model has **0.01686M parameters**.
- Achieved **99.50% accuracy**.
- Uses **Dual Tree Wavelet Transformation** for feature enhancement.

## Training Pipeline
1. **Data Preprocessing**: Image resizing, normalization, and augmentation.
2. **Model Training**: Using a lightweight deep learning model.
3. **Evaluation**: Measuring accuracy, loss, and computational efficiency.

## Issues Faced
- Handling class imbalance.
- Reducing computational complexity while maintaining accuracy.

## Future Improvements
- Optimize the model for **edge devices**.
- Experiment with different **wavelet transformations**.
- Improve generalization with more diverse datasets.

## How to Run
```bash
# Clone the repository
git clone https://github.com/your-repo/chest-radiology.git
cd chest-radiology

# Install dependencies
pip install -r requirements.txt

# Run the training script
python train.py
```
