import streamlit as st
import pandas as pd


url = pd.read_csv('https://raw.githubusercontent.com/MarosFeher/Streamlit/main/top10medalistsCSV.csv', sep= ';')

rows = pd.read_csv(url)

# Print results.
st.title(":orange[TOP 10 BEST MEDALISTS]")


#### PANDAS Dataframe - jednoducha tabulka
df = pd.DataFrame(rows)
df.rename(columns={0: 'Athlete', 1: 'Sport', 2: 'Medals'}, inplace= True)
df.index = pd.RangeIndex(start=1, stop=1+len(df), step=1)
st.table(df)



