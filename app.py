import streamlit as st
import pandas as pd

st.set_page_config(page_title="Telecom Billing Analyser", layout="wide")

st.title("📞 Telecom Billing Analyser")

uploaded_file = st.file_uploader("Upload Telecom Billing CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("📄 Preview of Uploaded Data:")
    st.dataframe(df.head())

