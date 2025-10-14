import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page setup
st.set_page_config(page_title="EDA Dashboard", layout="wide")

# App title and intro
st.title("📊 Exploratory Data Analysis Dashboard")
st.markdown("""
This interactive dashboard allows you to perform a quick exploratory data analysis (EDA)
on any CSV dataset. Upload your file below to begin!
""")

# Upload section
uploaded_file = st.file_uploader("📁 Select a CSV file to upload", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    # Dataset preview
    st.header("👀 Data Preview")
    st.dataframe(df.head())

    # Dataset information
    st.header("📋 Basic Information")
    st.write(f"**Rows:** {df.shape[0]} | **Columns:** {df.shape[1]}")
    st.write("**Column Names:**", list(df.columns))

    # Summary statistics
    st.header("📈 Summary Statistics")
    st.write(df.describe())

    # Missing values
    st.header("⚠️ Missing Values Check")
    missing = df.isnull().sum()
    st.write(missing[missing > 0] if missing.sum() > 0 else "No missing values detected ✅")

    # Correlation heatmap
    st.header("🔗 Correlation Analysis")
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    
    if numeric_df.shape[1] > 1:
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)
    else:
        st.info("Not enough numeric columns to generate a correlation heatmap.")

    # Small insights summary
    st.header("📝 Quick Insights")
    st.markdown("""
    - Use the summary stats above to understand variable ranges and averages.  
    - The heatmap highlights relationships between numeric variables.  
    - Missing value counts can help decide if cleaning is needed.  
    - You can explore furthe
