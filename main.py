import streamlit as st
import pandas as pd

st.title("welcome to home")
st.header("content")
st.subheader("description")

dataset = pd.read_csv("customers-100.csv")

st.dataframe(dataset)

name = st.text_input("enter your name :")
fname =st.text_input("enter your father name:")
adr = st.text_area("enter your text:")
classdata = st.selectbox("enter your class :",(1,2,3,4,5))

button = st.button("done")
if button:
    st.markdown(f"""
            name : {name}
            father name : {fname}
            address : {adr}
            class : {classdata}""")
    
                                                                        