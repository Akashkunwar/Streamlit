import pandas as pd
import streamlit as st

Rank = st.sidebar.number_input('Enter your Rank', 1, 100000000, step=1)
Rank = st.sidebar.slider('Adjust no. of Cluster', 0, Rank * 2, Rank)
uploaded_file = st.sidebar.file_uploader("Upload CSV file with GPS Coordinates")
csv = pd.read_csv('Demo.csv')
st.download_button(
    label="Download Sample CSV",
    data=csv.to_csv(),
    file_name='Demo.csv',
    mime='text/csv')

result = pd.DataFrame()
if Rank < 2:
    st.error("Please enter your Rank")
elif uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    try:
        result = df[(df['Opening Rank'] <= Rank) & (df['Closing Rank'] >= Rank)]
    except Exception as e:
        st.warning(f"Something went wrong! Contact Support. Error: {e}")
else:
    st.warning("Please Upload CSV")

if not result.empty:
    st.write(result)