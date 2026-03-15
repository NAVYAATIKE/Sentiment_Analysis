#import all libraries
import streamlit as st
import pandas as pd
from transformers import pipeline


#page config
st.set_page_config(
    page_title="Sentiment Analyzer",
    layout="wide"
)

#title and desc
st.title("AI Sentiment Analysis Application")
st.write("Welcome to Sentiment Analysis AI! This app uses **LLM to detect the sentiment of customer reviews.**")


#load model(cache for performance enhancement)
@st.cache_resource
def load_sentiment_model():
    model = pipeline("text-classification", model="lxyuan/distilbert-base-multilingual-cased-sentiments-student")
    return model


#spinner
with st.spinner("Loading AI model....Please wait....."):
    sentiment_pipeline = load_sentiment_model()


#main interface
tab1, tab2 = st.tabs(["Analyze the Text", "Analyze the CSV Dataset"])


#tab 1
with tab1:
    st.header("Analyze the single review")

    user_input = st.text_area(
        "Please enter customer review:",
        "The service and the product was just amazing, I loved it"
    )

    if st.button("Analyze Sentiment"):

        if user_input:
            result = sentiment_pipeline(user_input)

            label = result[0]["label"]
            score = result[0]["score"]

            st.success(f"Sentiment: **{label}**")
            st.info(f"Confidence score: **{score:.2f}**")

        else:
            st.warning("Please enter some text value to analyze the sentiment")


#tab2
with tab2:

    st.header("Analyze the Dataset (CSV)")

    uploaded_file = st.file_uploader(
        "Upload CSV file with customer reviews",
        type=["csv"]
    )

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)

        st.write("### Preview of your data")
        st.dataframe(df.head())

        text_column = "review_text"

        if text_column in df.columns:

            if st.button("Analyze the entire dataset"):

                st.write("Analyzing... this might take a few moments")

                df["AI_Sentiment"] = df[text_column].apply(
                    lambda x: sentiment_pipeline(str(x))[0]["label"]
                )

                st.write("### Analysis Completed!")
                st.dataframe(df[[text_column, "AI_Sentiment"]].head(10))

                #bar chart
                st.write("### Sentiment Distribution")
                sentiment_counts = df["AI_Sentiment"].value_counts()
                st.bar_chart(sentiment_counts)

                #download csv file
                csv = df.to_csv(index=False).encode("utf-8")

                st.download_button(
                    label="Download the sentiment data",
                    data=csv,
                    file_name="customer_sentiment_10_records",
                    mime="text/csv"
                )

        else:
            st.error(f"Could not find the column '{text_column}' in your CSV file.")
            