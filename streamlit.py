import streamlit as st
st.write("khurram")
st.title ("this is title")
st.header ("header")
st.subheader("sub :blue[header]")
st.code ("x = 2", language="python")
st.write("(x=y)^2")
st.latex ("(x=y)^2")

btn_value = st.button("Click the ok")
text= " i love pakistan"

st.download_button(data=text,label="download CV")

st.text_input("Enter text here")

#if st.buttton("add two number"):
#    st.session

#st.header("Bottion")
#if st.buttion ("check now"):
#    st.session_state[]
