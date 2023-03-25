import streamlit as st
import pandas as pd

rows = pd.read_csv('https://raw.githubusercontent.com/MarosFeher/Streamlit/main/top10medalistsCSV.csv', sep= ';')

# Print results.
st.title(":orange[TOP 10 BEST MEDALISTS]")

print(rows)

df = pd.DataFrame(rows)
df.columns['Athlete', 'Sport', 'Medals']
df.index = pd.RangeIndex(start=1, stop=1+len(df), step=1)
st.table(df)



