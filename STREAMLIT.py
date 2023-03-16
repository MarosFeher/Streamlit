import streamlit as st
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

rows = run_query("SELECT * FROM maros.top10_medailists;")

# Print results.
st.title(":orange[TOP 10 BEST MEDALISTS]")

col1, col2, col3 = st.columns(3)
with col1:
    st.subheader(":blue[Athlete]:man-running:")
    for row in rows:
        st.text(row[0])
with col2:
   st.subheader(":red[Sport]:football:")
   for row in rows:
       st.text(row[1])
with col3:
   st.subheader(":green[Medals in total]:sports_medal:")
   for row in rows:
       st.text(row[2])







