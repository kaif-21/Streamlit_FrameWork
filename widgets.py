import pandas as pd
import streamlit as st

st.title("streamlit text input")

name=st.text_input("Enter your name")
age=st.slider("Select your age:",0,100,25)

options=["choose:","python","java","c","c++","r","javascript"]
choice=st.selectbox("choose your favorite language",options)
st.write(f"Your favorite language is {choice}")

st.write(f"your age is {age}")


if name:
    st.write(f"hello, {name}")


data={
    'name':["kaif","jiya","virat","anushka"],
    'age':[21,20,35,34],
    'cite':["sikar","sikar","london","london"]
}

df=pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_file=st.file_uploader("choose a csv file",type="csv")
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)