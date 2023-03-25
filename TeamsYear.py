import streamlit as st
import pandas as pd
import mysql.connector

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

conn = init_connection()

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * FROM maros.teams_year_playerscount;")

#vyber prveho pola z riadku (nazov mesta), "set" vyberie len unikatne, "sorted" ich zoradi abecedne
team = list(sorted(set([i[0] for i in rows])))

table = pd.DataFrame(rows)
table.rename(columns={0: 'Olympic Team', 1: 'Year', 2: 'Athletes', 3: 'Medals Won', 4: 'Medal-Winning Percentage'}, inplace= True)
table['Year'] = table['Year'].astype(int)
table.index = pd.RangeIndex(start=1, stop=1+len(table), step=1)

st.header('Olympic Performance by Team/Country and Year :trophy:')
select_team = st.multiselect('Select team or country: ', team)

#pokial bude vybrana krajina, vytvori iba tabulku s danou krajinou. Pokial nebude tak vytvori celu tabulku
while select_team:
    try:
        for selected in select_team:
            st.dataframe(table.loc[table['Olympic Team'].isin([selected])])
        break
    except:
        break
while not select_team:
    st.dataframe(table)
    break




