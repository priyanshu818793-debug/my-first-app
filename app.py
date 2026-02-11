import streamlit as st 
st.title("hello world")
st.write("python me frontant banana kitna asan hai")
st.balloons()
if st.button("type here"):
    st.balloons()
age=st.slider("what is your age",0,100,10)
st.write(f"your age {age} years")    
