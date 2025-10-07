import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title("Exploratory Data Analysis App")

# Upload dataset
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.write("### Dataset Preview")
    st.write(df.head())

    st.write("### Summary Statistics")
    st.write(df.describe())

    st.write("### Missing Values")
    st.write(df.isnull().sum())

    st.write("### Correlation Heatmap")
    try:
        numeric_df = df.select_dtypes(include=['float64', 'int64'])  # only numeric columns
        if numeric_df.shape[1] > 1:  # only if more than 1 numeric column
            fig, ax = plt.subplots()
            sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", ax=ax)
            st.pyplot(fig)
        else:
            st.write("Not enough numeric columns to create a heatmap.")
    except Exception as e:
        st.write("Error generating heatmap:", e)