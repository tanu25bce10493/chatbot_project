# 🤖 AI-Powered Student Assistant Chatbot

## 📌 Overview

This project is an AI-powered chatbot designed to assist students with academic queries related to Artificial Intelligence and Machine Learning. It uses Natural Language Processing (NLP) and Machine Learning (ML) techniques to understand user input, classify intent, and generate relevant responses.

---

## 🎯 Problem Statement

Students often face difficulty in getting quick and accurate answers to academic queries. Faculty may not always be available, and searching through study materials can be time-consuming. This project addresses the problem by providing an intelligent chatbot that delivers instant academic assistance.

---

## 🎯 Objectives

* To design and develop an AI-based chatbot
* To apply NLP techniques for understanding user queries
* To implement Machine Learning algorithms for classification
* To provide a user-friendly and interactive interface

---

## 🚀 Features

* NLP-based intent recognition
* Machine Learning model using Logistic Regression
* TF-IDF vectorization for text processing
* Web-based chatbot using Flask
* Modern responsive chat interface
* Suggested queries for improved usability
* Real-time interaction

---

## 🛠️ Technologies Used

* **Programming Language:** Python
* **Framework:** Flask
* **Machine Learning:** Scikit-learn
* **Frontend:** HTML, CSS, JavaScript

---

## ⚠️ Important Note (Folder Structure Issue)

After extracting the project ZIP file, you may notice that a **nested folder with the same name is created** (e.g., `chatbot_project-main/chatbot_project/`).

👉 This can cause errors like:

* `requirements.txt not found`
* `model.pkl not found`

### ✅ Solution:

Make sure you navigate to the correct folder where the files actually exist.

Example:

```bash
cd chatbot_project
```

Then run:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Installation & Setup

### 1. Clone or extract the project

```bash
git clone <your-repo-link>
cd chatbot_project
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Train the model

```bash
python train.py
```

### 4. Run the application

```bash
python app.py
```

### 5. Open in browser

http://127.0.0.1:5000/

---

## 📊 How It Works

1. User enters a query
2. Text is processed using TF-IDF vectorization
3. Logistic Regression model predicts the intent
4. Appropriate response is selected from dataset
5. Response is displayed on the web interface

---

## 📁 Project Structure

chatbot_project/
│── app.py
│── train.py
│── intents.json
│── model.pkl
│── vectorizer.pkl
│── requirements.txt
│── README.md

├── templates/
│   └── index.html

├── static/
│   └── style.css

├── project_report/
│   ├── report.pdf
│   └── sample_output.png

---

## 📈 Results

The chatbot successfully responds to user queries related to AI and ML concepts. It provides quick and relevant answers, demonstrating the practical application of NLP and ML techniques.

---

## ⚠️ Limitations

* Limited dataset may affect accuracy
* Cannot handle complex or unseen queries effectively
* No deep contextual understanding

---

## 🔮 Future Enhancements

* Voice-based interaction
* Deep learning models (LSTM, Transformers)
* Deployment on cloud platforms
* Auto-learning chatbot

---

## 📚 References

1. Artificial Intelligence: A Modern Approach – Russell & Norvig
2. Machine Learning – Ethem Alpaydin
3. Scikit-learn Documentation
4. Flask Documentation

---

## 👨‍💻 Author

Student Project – Fundamentals in AI & ML

---
