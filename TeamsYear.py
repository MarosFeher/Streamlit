import streamlit as st
import pandas as pd

rows = pd.read_csv('https://raw.githubusercontent.com/MarosFeher/Streamlit/main/TeamsYear2CSV.csv', sep= ';', header = 0)


#vyber prveho pola z riadku (nazov mesta), "set" vyberie len unikatne, "sorted" ich zoradi abecedne
team = list(sorted(set(rows.iloc[:, 0])))

pd.options.display.float_format = '{:.1f}%'.format
table = pd.DataFrame(rows)
table.columns = ['Olympic Team', 'Year', 'Athletes', 'Medals Won', 'Medal-Winning Percentage (%)']
table['Year'] = table['Year'].astype('str')
table['Medal-Winning Percentage (%)'] = table['Medal-Winning Percentage (%)'].astype('float')
table.index = pd.RangeIndex(start=1, stop=1+len(table), step=1)

st.header('Olympic Performance by Team/Country and Year :trophy:')
select_team = st.multiselect('Select team or country: ', team)

group = st.checkbox('All data in one table')

if not group:
#pokial bude vybrana krajina, vytvori iba tabulku s danou krajinou. Pokial nebude tak vytvori celu tabulku
    while select_team:
        try:
            for selected in select_team:
                st.dataframe(table.loc[table['Olympic Team'].isin([selected])],use_container_width=st.session_state.use_container_width)
            break
        except:
            break
    else:
        st.dataframe(table,use_container_width=st.session_state.use_container_width)
else:
    if select_team:
        selected_rows = table[table['Olympic Team'].isin(select_team)]
        st.dataframe(selected_rows,use_container_width=st.session_state.use_container_width)
    else:
        st.dataframe(table,use_container_width=st.session_state.use_container_width)




