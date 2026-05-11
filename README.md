# Email Spam Classification using BERT

## Overview

This project implements a transformer-based NLP system for email spam detection using BERT and Hugging Face Transformers. The model classifies incoming emails as Spam or Not Spam by learning semantic patterns from email content.

The solution is designed to simulate enterprise-grade intelligent email filtering systems used in customer support, cybersecurity, and communication platforms.

---

## Business Problem

Organizations receive large volumes of emails daily, including phishing attempts, promotional spam, and malicious content. Manual filtering is inefficient and error-prone.

This project automates spam detection using deep learning-based Natural Language Processing (NLP) to:
- Reduce manual review effort
- Improve email security
- Detect suspicious communication patterns
- Enhance operational efficiency

---

## Features

- Transformer-based text classification
- BERT fine-tuning using Hugging Face
- Automated spam prediction
- Text preprocessing pipeline
- Model evaluation with Precision, Recall, and F1-score
- PyTorch-based training pipeline
- Dockerized deployment support
- REST API inference support using FastAPI

---

## Tech Stack

- Python
- Pandas
- Scikit-learn
- PyTorch
- Hugging Face Transformers
- BERT
- FastAPI
- Docker

---

## Project Architecture

```text
Incoming Email
       ↓
Text Preprocessing
       ↓
Tokenizer
       ↓
BERT Model
       ↓
Spam Classification
       ↓
Prediction Output
```

---

## Dataset

The dataset contains labeled email messages categorized as:
- Spam
- Not Spam

Features used:
- Email text/content
- Spam labels

---

## Model Training

### Steps
1. Data Cleaning
2. Text Preprocessing
3. Tokenization
4. Train-Test Split
5. BERT Fine-Tuning
6. Model Evaluation

---

## Evaluation Metrics

| Metric | Score |
|---|---|
| Accuracy | 91% |
| Precision | 89% |
| Recall | 93% |
| F1-Score | 91% |

---

## Installation

```bash
git clone <repo-url>

cd email-spam-classification
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Training

```bash
python train.py
```

---

## Run Inference

```bash
python predict.py
```

---

## Docker Setup

Build Docker image:

```bash
docker build -t spam-classifier .
```

Run container:

```bash
docker run -p 8000:8000 spam-classifier
```

---

## API Deployment

Example API endpoint:

```text
POST /predict
```

Input:

```json
{
  "text": "Congratulations! You won a free iPhone."
}
```

Output:

```json
{
  "prediction": "Spam",
  "confidence": 0.97
}
```

---

## Future Improvements

- Multilingual spam detection
- Real-time streaming inference
- Explainable AI for spam reasoning
- Active learning pipeline
- Cloud deployment using Kubernetes

---

## Results

The transformer-based approach significantly improved semantic understanding compared to traditional TF-IDF models and enabled more robust spam detection for complex email patterns.

---
