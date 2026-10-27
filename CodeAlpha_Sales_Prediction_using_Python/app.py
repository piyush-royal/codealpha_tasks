
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

st.set_page_config(
    page_title="Sales Prediction",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Sales Prediction Using Python")
st.write("Explore advertising data and analyze its relationship with sales.")

csv_path = Path(__file__).parent / "advertising.csv"

try:
    df = pd.read_csv(csv_path)

    st.subheader("Dataset Preview")
    st.dataframe(df.head(10), use_container_width=True)

    st.subheader("Dataset Information")
    col1, col2 = st.columns(2)
    col1.metric("Total Rows", df.shape[0])
    col2.metric("Total Columns", df.shape[1])

    st.subheader("Summary Statistics")
    st.dataframe(df.describe(), use_container_width=True)

    numeric_cols = df.select_dtypes(include="number").columns.tolist()

    if len(numeric_cols) >= 2:
        x_col = st.selectbox(
            "Select X-axis",
            numeric_cols,
            index=0
        )
        y_col = st.selectbox(
            "Select Y-axis",
            numeric_cols,
            index=len(numeric_cols) - 1
        )

        fig, ax = plt.subplots()
        ax.scatter(df[x_col], df[y_col])
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        ax.set_title(f"{y_col} vs {x_col}")
        st.pyplot(fig)
        plt.close(fig)
    else:
        st.info("Not enough numeric columns to create a scatter plot.")

except FileNotFoundError:
    st.error("CSV file not found. Check the exact filename and location.")
except Exception as e:
    st.error(f"Unable to load dataset: {e}")
