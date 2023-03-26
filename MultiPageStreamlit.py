import streamlit as st

def Home():
    st.write("# Welcome to my project page! 👋")

    st.write('My name is **Maroš Fehér**.')
    st.write("I'm excited to share with you the project I've been working on.")
    st.write("For my **portfolio project**, I decided to work on a data set containing information on all Olympic players throughout the history of the **Olympic Games**.")
    st.write("Using **Python**, I extracted raw data from CSV file and loaded it into a local database server using **MySQL**. "
             "I then worked to understand the data set, identify inconsistencies and clean and pre-process the data. I split the data into multiple entity tables using SQL for follow-up data analysis.")
    st.write("In the data analysis phase of the project, I focused on various aspects and statistics, including top-performing countries, athletes and teams. "
             "I then created and stored views for all SQL queries for efficient data retrieval.")
    st.write("Finally, I visualized output data using **StreamLit**, which helped me to create lightweight, modern looking UI. "
             "Integration with **GitHub** also allowed me to make it accessible to the public.")
    st.write("This project allowed me to improve my skills in data analysis, database management and data visualization. "
             "I gained experience working with **large, complex data sets**. The project also helped me to perfect my problem-solving skills and analytical thinking, "
             "as I had to identify and resolve various issues and inconsistencies in the data.")
    st.write("**Skills and Tools Used**: "
             "Python programming, "
             "Data cleaning and pre-processing, "
             "MySQL database management, "
             "Data analysis, "
             "Data visualization with StreamLit.")

    st.sidebar.text('')
    st.sidebar.text('')
    st.sidebar.text('')
    st.sidebar.text('')
    st.sidebar.text('')


    st.sidebar.header('**Contact:**')
    st.sidebar.write(':e-mail:**E-Mail** - fehermaros@gmail.com')
    st.sidebar.write(':link:**Linked In** - https://www.linkedin.com/in/maros-feher-5b6b02263/')

    st.sidebar.header('About')
    st.sidebar.write("This project is a culmination of my efforts, passion and dedication. "
                     "But more than that, this project represents a new chapter in my career journey. "
                     "I'm eager to take the next step and begin working in IT, "
                     "applying my skills and knowledge to real-world problems and challenges.")
    st.sidebar.write('Feel free to explore :wink:')
    
    
def TOP10():
    import streamlit as st
    import pandas as pd

    rows = pd.read_csv('https://raw.githubusercontent.com/MarosFeher/Streamlit/main/top10medalistsCSV.csv', sep= ';')

    # Print results.
    st.title(":orange[TOP 10 BEST MEDALISTS]")

    st.caption("This table displays the Top 10 Olympic medalists of all time, based on the total number of medals earned across Summer Olympic Games. "
             "The table includes each athlete's name, the sport in which they competed, and the number of medals they earned.")
    st.write("")

    print(rows)

    df = pd.DataFrame(rows)
    df.columns = ['Athlete', 'Sport', 'Medals']
    df.index = pd.RangeIndex(start=1, stop=1+len(df), step=1)
    st.dataframe(df)

    st.sidebar.text('')
    st.sidebar.text('')
    st.sidebar.text('')

    st.sidebar.header("About")
    st.sidebar.write('This page is a demonstration of a simple dataframe.')
    

def TeamYear():
    import streamlit as st
    import pandas as pd

    rows = pd.read_csv('https://raw.githubusercontent.com/MarosFeher/Streamlit/main/TeamsYear2CSV.csv', sep=';',
                       header=0)

    # vyber prveho pola z riadku (nazov mesta), "set" vyberie len unikatne, "sorted" ich zoradi abecedne
    team = list(sorted(set(rows.iloc[:, 0])))

    pd.options.display.float_format = '{:.1f}%'.format
    table = pd.DataFrame(rows)
    table.columns = ['Olympic Team', 'Year', 'Athletes', 'Medals Won', 'Medal-Winning Percentage (%)']
    table['Year'] = table['Year'].astype('str')
    table['Medal-Winning Percentage (%)'] = table['Medal-Winning Percentage (%)'].astype('float')
    table.index = pd.RangeIndex(start=1, stop=1 + len(table), step=1)

    st.header(':orange[OLYMPIC PERFORMANCE BY TEAM/COUNTRY AND YEAR] :trophy:')
    st.caption("This table displays all of the teams that have competed in the Summer Olympic Games since 1936. "
             "The table includes the year in which each team competed, the name of the team, "
             "the number of athletes that competed for the team, the number of medals the team won, "
             "and the team's medal-winning percentage.")
    st.caption("This table contains Countries and also Team names")
    st.write("")
    st.write("")
    st.write("")

    st.sidebar.text('')
    st.sidebar.text('')
    st.sidebar.text('')
    st.sidebar.header('About')
    st.sidebar.write("This page contains large data set. Data can be filtered using StreamLits' multiselect. Then the data is displayed in Tables. Tables can be easily joined using CheckBox. ")


    select_team = st.multiselect('Select team or country: ', team)

    group = st.checkbox('All data in one table')

    if not group:
        # pokial bude vybrana krajina, vytvori iba tabulku s danou krajinou. Pokial nebude tak vytvori celu tabulku
        while select_team:
            try:
                for selected in select_team:
                    st.dataframe(table.loc[table['Olympic Team'].isin([selected])])
                break
            except:
                break
        else:
            st.dataframe(table)
    else:
        if select_team:
            selected_rows = table[table['Olympic Team'].isin(select_team)]
            st.dataframe(selected_rows)
        else:
            st.dataframe(table)

page_names_to_funcs = {
    "Homepage" : Home,
    "TOP 10 Medalists": TOP10,
    "Olympic Performance": TeamYear
}

st.sidebar.write('# **Choose project**:')
Project = st.sidebar.selectbox("", page_names_to_funcs.keys())
page_names_to_funcs[Project]()
