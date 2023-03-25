import streamlit as st
import pandas as pd

def Home():
    st.write("# Welcome to my project page 👋")


    st.sidebar.header("Top 10 medalists")
    st.sidebar.button('TOP10')
    st.sidebar.success("Select a project above.")

    st.header('hello')
    st.write('https://marosfehertop10athletes.streamlit.app/')
    st.write('https://marosfeher-streamlit-teamsyear-i1k4fe.streamlit.app/')

def TOP10():
    import streamlit as st
    import pandas as pd

    rows = pd.read_csv('https://raw.githubusercontent.com/MarosFeher/Streamlit/main/top10medalistsCSV.csv', sep= ';')

    # Print results.
    st.title(":orange[TOP 10 BEST MEDALISTS]")

    print(rows)

    df = pd.DataFrame(rows)
    df.columns = ['Athlete', 'Sport', 'Medals']
    df.index = pd.RangeIndex(start=1, stop=1+len(df), step=1)
    st.dataframe(df)


page_names_to_funcs = {
    "Homepage" : Home,
    "TOP 10 Medalists": TOP10
}

demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()




