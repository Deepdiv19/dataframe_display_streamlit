import streamlit as st
import pandas as pd
import numpy as np
df = pd.read_csv(r"C:\Users\ADMIN\Downloads\Iris.csv")
st.dataframe(df)