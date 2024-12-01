import streamlit as st
import pandas as pd

st.title('🤖 Machine Learning Application')

st.info('This is an application that builds a machine learning model!')


with st.expander('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df
