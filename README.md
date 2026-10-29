
# Fake News Detection Using LSTM

A deep learning project that classifies news text as **Fake News** or **Real News** using a Long Short-Term Memory (LSTM) neural network.

## 🚀 Live Demo

Try the deployed application here:

**[Open Fake News Detector](https://fake-news-detection-lstm-vfbjngtwhbpco79xstg9ep.streamlit.app/)**

## 📌 Project Overview

This project uses Natural Language Processing (NLP) and an LSTM-based deep learning model to analyze news text and predict whether it resembles fake or real news based on patterns learned from the training dataset.

## 🛠️ Technologies Used

- Python
- TensorFlow and Keras
- Natural Language Processing (NLP)
- LSTM (Long Short-Term Memory)
- Pandas and NumPy
- Streamlit
- Git and GitHub

## 📊 Model Performance

| Metric | Result |
|---|---:|
| Test Accuracy | 95.50% |
| Test Loss | 0.1122 |
| Training Epochs | 3 |

**Test dataset:** 4,427 news articles.

## ⚙️ Project Workflow

1. Load and combine fake and real news datasets.
2. Clean and prepare the news text and labels.
3. Split the dataset into training, validation, and testing sets.
4. Convert text into numerical sequences using Keras TextVectorization.
5. Train an LSTM-based deep learning model.
6. Evaluate the model on unseen test data.
7. Deploy the trained model using Streamlit.

## 💻 Run Locally

Clone the repository:

```bash
git clone https://github.com/KanchanNanda/fake-news-detection-lstm.git
cd fake-news-detection-lstm
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## ⚠️ Limitations

- Predictions are based on patterns learned from the training dataset.
- Dataset bias and writing style may affect predictions.
- A prediction is not proof that a news article is authentic or false.
- Important claims should be verified using reliable sources.

## 📸 Screenshots

### Fake News Prediction
![Fake News Prediction](screenshots/fake-news-result.png)

### Real News Prediction
![Real News Prediction](screenshots/real-news-result.png)

## 👩‍💻 Author

**Kanchan Nanda**

GitHub: [KanchanNanda](https://github.com/KanchanNanda)

