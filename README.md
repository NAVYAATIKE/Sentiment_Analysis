
# AI Sentiment Analysis Application

An interactive **AI-powered Sentiment Analysis Web Application** built using Python, NLP, and Streamlit.
This application analyzes customer reviews and determines whether the sentiment is **Positive, Negative, or Neutral** using a pretrained **DistilBERT transformer model** from Hugging Face.

The project demonstrates how **Natural Language Processing (NLP)** and **Transformer-based models** can be integrated into a real-world web application for analyzing customer feedback.

---

# Project Overview

Customer feedback plays an important role in understanding user satisfaction.
This project provides a simple and interactive way to analyze customer reviews using an AI model.

The application allows users to:

* Analyze sentiment for a **single customer review**
* Upload a **CSV dataset of reviews**
* Perform **bulk sentiment analysis**
* Visualize sentiment distribution
* Download the analyzed dataset

---

# Features

• Sentiment analysis for single text input
• Upload CSV dataset for bulk sentiment analysis
• Automatic sentiment classification using DistilBERT
• Displays sentiment label with confidence score
• Sentiment distribution visualization with bar charts
• Download analyzed dataset as CSV
• Simple and interactive UI using Streamlit

---

# Tech Stack

**Programming Language**

* Python

**Libraries & Frameworks**

* Streamlit
* Pandas
* Transformers (Hugging Face)

**Model Used**

* DistilBERT Multilingual Sentiment Model

---

# Project Structure

```
Sentiment-Analysis-App
│
├── app.py                # Main Streamlit application
├── README.md             # Project documentation
└── sentiment_analysis.csv    # Example dataset (optional)
```

---

# How the Application Works

The sentiment analysis pipeline follows these steps:

1. User enters text or uploads a dataset.
2. The input text is tokenized using the transformer tokenizer.
3. The DistilBERT model processes the tokens.
4. The model predicts the sentiment class.
5. The result is displayed with a confidence score.

For datasets, the model analyzes each review and adds a new column containing the predicted sentiment.

---

# Installation

Clone the repository:

```bash
git clone https://github.com/your-username/sentiment-analysis-app.git
```

Navigate to the project folder:

```bash
cd sentiment-analysis-app
```

Install required dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in your browser.

---

# Example Use Cases

* Customer feedback analysis
* Product review sentiment analysis
* Social media comment analysis
* Survey response analysis

---

# Future Improvements

* Support for multiple sentiment models
* Real-time API integration
* Advanced visualization dashboards
* Deployment on cloud platforms

---

# Learning Outcomes

This project helped in understanding:

* Transformer-based NLP models
* Hugging Face Transformers library
* Building interactive AI web applications using Streamlit
* Handling and analyzing text datasets with Pandas

---

# Author

NAVYA ATIKE


# Screenshots
---Analyzing the text-----
![alt text](<Screenshot 2026-03-13 161250-1.png>)
![alt text](<Screenshot 2026-03-13 160943-1.png>)
---Analyzing the dataset-----
![alt text](<Screenshot 2026-03-13 161259.png>)
![alt text](<Screenshot 2026-03-13 161051.png>)
![alt text](<Screenshot 2026-03-13 161139.png>)
![alt text](<Screenshot 2026-03-13 161214.png>)

# Sample dataset 
[text](../../../Downloads/customer_sentiment_dataset.csv)
