import pandas as pd
import matplotlib as plt
import seaborn as sns
import streamlit as st


def main():
    st.title("Hey there ! I am Santanu Haldar.\nThis is my streamlit app for ecom business.")
    st.sidebar.title("Upload your file")
    uploaded_file = st.sidebar.file_uploader("Upload your own file", type = ['csv', 'xlsx'])

    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'):
                data = pd.read_csv(uploaded_file)
            else :
                data = pd.read_excel(uploaded_file)

                st.sidebar.success("File uploaded Successfully")
                st.subheader("Data Overview")
                st.dataframe(data.head())
                st.subheader("Basic information of data")
                st.write("Shape of the data", data.shape)
                st.write("Columns in the data", data.columns)
                st.write("Missing value",data.isnull().sum())

                st.subheader("I will show you stats of the data")
                st.write(data.describe())
        except:
            print("Let me handle.")


if __name__== "__main__":
    main()
