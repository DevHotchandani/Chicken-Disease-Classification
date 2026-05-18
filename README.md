# Chicken Disease Classification

Deep learning–based web application for identifying chicken diseases from fecal images using TensorFlow, Flask, and transfer learning with VGG16.

---

# Project Overview

This project predicts whether a chicken fecal image belongs to one of the following categories:

- Healthy
- Coccidiosis

The application uses a pretrained VGG16 convolutional neural network combined with transfer learning for image classification. A Flask-based web interface allows users to upload images and receive predictions instantly.

The project was developed to understand:

- Deep learning workflows
- Transfer learning concepts
- CNN-based image classification
- Image preprocessing techniques
- Flask integration with machine learning models
- Modular Python project architecture
- End-to-end ML application development

---

# Tech Stack

- Python
- TensorFlow / Keras
- VGG16
- Flask
- NumPy
- HTML/CSS
- Git
- VS Code

---

# Features

- Chicken disease image classification
- Transfer learning using VGG16
- Flask web application
- Image upload and prediction system
- Trained model integration
- Modular project structure
- Localhost deployment support
- Interactive user interface

---

# Project Structure

```text
Chicken-Disease-Classification/
│
├── artifacts/
├── config/
├── research/
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
├── templates/
├── app.py
├── main.py
├── params.yaml
├── requirements.txt
├── setup.py
└── README.md
```

---

# Workflow

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

# Transfer Learning Model

The model uses:

- VGG16 pretrained on ImageNet
- Frozen convolutional base layers
- Custom classification head
- TensorFlow image preprocessing pipeline
- Data augmentation techniques

---

# Model Performance

Validation Accuracy:

```text
~88%
```

---

# Web Application

The Flask application allows users to:

- Upload chicken fecal images
- Run disease predictions
- View classification results instantly

Run locally:

```bash
python app.py
```

Open in browser:

```text
http://127.0.0.1:8080
```

---

# Installation

Clone repository:

```bash
git clone https://github.com/DevHotchandani/Chicken-Disease-Classification.git
```

Move into project directory:

```bash
cd Chicken-Disease-Classification
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install local package:

```bash
pip install -e .
```

Run application:

```bash
python app.py
```
---

# Author

Dev Hotchandani