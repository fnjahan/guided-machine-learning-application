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

st.write('**Y**')
Y = df.species
Y

with st.expander('Data Visualization'):
  st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color='species')


# Data preparation
with st.sidebar:
  st.header('Input features')
  island = st.selectbox('Island', ('Biscoe', 'Dream', 'Torgerson'))
  gender = st.selectbox('Gender', ('male', 'female'))
  bill_length_mm = st.slider('Bill length (mm)', 32.1, 59.6, 43.9)


  
