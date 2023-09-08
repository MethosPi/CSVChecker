import pandas as pd
import csv
import streamlit as st
import os
import matplotlib.pyplot as plt

# Crea la directory "temp" se non esiste già
directory = "temp"
if not os.path.exists(directory):
    os.makedirs(directory)

st.title('CSV Check')

# Create a sidebar menu
sidebar = st.sidebar
sidebar.header('Menu')
uploaded_file = sidebar.file_uploader("Upload")

if uploaded_file is not None:
    try:
        delimiter = None

        # Let the user choose the delimiter
        delimiter_option = st.selectbox("Select the delimiter", [',', ';', '|','\t',])

        if delimiter_option == ',':
            delimiter = ','
        elif delimiter_option == ';':
            delimiter = ';'
        elif delimiter_option == '|':
            delimiter = '|'
        elif delimiter_option == '\t':
            delimiter = '\t'

        st.write(f'Selected delimiter: {delimiter}')

        if delimiter:
            df = pd.read_csv(uploaded_file, delimiter=delimiter)
            st.write(f'The delimiter is {delimiter}')

            if st.button('Show first 10 rows'):
                st.write('First 10 rows:')
                st.write(df.head(10))

            if st.button('Show number of rows and columns'):
                st.write(f'Rows: {df.shape[0]}')
                st.write(f'Columns: {df.shape[1]}')

            if st.button('Show column data types'):
                st.write('Column data types:')
                st.write(df.dtypes)

            if st.button('Show duplicates'):
                duplicates = df.duplicated().sum()
                st.write(f'Duplicate rows: {duplicates}')

            # Aggiungi pulsante per statistiche descrittive
            if st.button('Descriptive Statistics'):
                st.write('Descriptive statistics for numeric columns:')
                st.write(df.describe())

            # Aggiungi la possibilità di cercare e filtrare dati
            st.subheader('Search and Filter Data')
            search_criteria = st.text_input('Enter search criteria:')
            filter_button = st.button('Filter Data')

            if filter_button:
                filtered_df = df[df.apply(lambda row: any(search_criteria.lower() in str(row[col]).lower() for col in df.columns), axis=1)]
                
                if not filtered_df.empty:
                    st.write('Filtered Data:')
                    st.write(filtered_df)
                else:
                    st.write('No matching data found.')

    except Exception as e:
        st.write(f'Error reading the CSV file,: {e}. Please try changing the delimiter.')



