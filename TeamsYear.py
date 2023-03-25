import streamlit as st
import pandas as pd

rows = pd.read_csv('https://raw.githubusercontent.com/MarosFeher/Streamlit/main/TeamsYearCSV.csv', sep= ';', header = 0)


#vyber prveho pola z riadku (nazov mesta), "set" vyberie len unikatne, "sorted" ich zoradi abecedne
team = list(sorted(set(rows.iloc[:, 0])))

table = pd.DataFrame(rows)
#table.rename(columns={0: 'Olympic Team', 1: 'Year', 2: 'Athletes', 3: 'Medals Won', 4: 'Medal-Winning Percentage'}, inplace= True)
table.columns = ['Olympic Team', 'Year', 'Athletes', 'Medals Won', 'Medal-Winning Percentage']
table['Year'] = table['Year'].astype(int)
table.index = pd.RangeIndex(start=1, stop=1+len(table), step=1)

st.header('Olympic Performance by Team/Country and Year :trophy:')
select_team = st.multiselect('Select team or country: ', team)

#pokial bude vybrana krajina, vytvori iba tabulku s danou krajinou. Pokial nebude tak vytvori celu tabulku
if select_team:
    try:
        selected_rows = table[table['Olympic Team'].isin(select_team)]
        st.dataframe(selected_rows)
    except Exception as e:
        st.error(f"Error occurred: {e}")
else:
    st.dataframe(table)




