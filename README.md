# Chicken Disease Classification

Deep learning–based web application for identifying chicken diseases from fecal images using TensorFlow, Flask, and transfer learning with VGG16.

---

## Project Overview

This project classifies chicken fecal images into the following categories:

- Healthy
- Coccidiosis

The application uses a pretrained VGG16 convolutional neural network with transfer learning for image classification. A Flask-based web interface allows users to upload images and receive predictions instantly.

The project was developed to understand:

- Deep learning workflows
- Transfer learning concepts
- CNN image classification
- Image preprocessing techniques
- Flask integration with machine learning models
- Modular Python project structure
- End-to-end ML application development

---

## Tech Stack

- Python
- TensorFlow / Keras
- VGG16
- Flask
- NumPy
- HTML/CSS
- Git
- VS Code

---

## Features

- Chicken disease image classification
- Transfer learning using VGG16
- Flask web application
- Image upload and prediction system
- Modular project structure
- Trained model integration
- Localhost deployment support
- Interactive frontend UI

---

## Project Structure

```text
Chicken-Disease-Classification/
│
├── artifacts/
│   └── training/
│       └── model.h5
│
├── config/
│   └── config.yaml
│
├── src/
│   └── cnnClassifier/
│       ├── components/
│       ├── config/
│       ├── constants/
│       ├── entity/
│       ├── pipeline/
│       └── utils/
│
├── static/
│   └── uploads/
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── app.py
├── main.py
├── params.yaml
├── requirements.txt
├── setup.py
└── README.md
```

---

## Workflow

```text
Data Collection
→ Data Preprocessing
→ Model Preparation
→ Model Training
→ Evaluation
→ Prediction
→ Flask Integration
```

---

## Transfer Learning Model

The model uses:

- VGG16 pretrained on ImageNet
- Frozen convolutional base layers
- Custom classification head
- TensorFlow preprocessing pipeline
- Data augmentation techniques

---

## Model Performance

| Metric | Value |
|--------|--------|
| Validation Accuracy | ~88% |

---

## Run Locally

### Clone Repository

```bash
git clone https://github.com/DevHotchandani/Chicken-Disease-Classification.git
```

### Move Into Project Directory

```bash
cd Chicken-Disease-Classification
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install Local Package

```bash
pip install -e .
```

### Run Application

```bash
python app.py
```

### Open In Browser

```text
http://127.0.0.1:8080
```

---



## Author

**Dev Hotchandani**