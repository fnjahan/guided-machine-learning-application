import streamlit as st
import pandas as pd

st.title('🤖 Machine Learning Application')

st.info('This is an application that builds a machine learning model!')

# creates a dropdown with text 'Data' and shows 'Raw data' and csv file when clicked on drop down
with st.expander('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df

st.write('**X**')
X = df.drop('species', axis=1)
X
