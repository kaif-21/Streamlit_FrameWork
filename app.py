import streamlit as st
import pandas as pd
import numpy as np

#  Title of the aplication
st.title("hello kaifu")


# display a simple text
st.write("this is the simple text")

df=pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [5,6,7,8]
})

# display the dataframe
st.write("here the dataframe")
st.write(df)

# create a line chart

chart_data=pd.DataFrame(

    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)