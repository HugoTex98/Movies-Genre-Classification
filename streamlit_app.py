import streamlit as st

st.title("Simple Text Submission App")

# Text input
user_input = st.text_area("Please enter your text below:")

# Submit button
if st.button("Submit"):
    if user_input.strip() != "":
        st.success("Well done! Text received!")
    else:
        st.warning("Please enter some text before submitting.")
