import streamlit as st

st.title("Movie Genre Detector 🎥🪄")

# Centered image using markdown and HTML
st.markdown(
    """
    <div style='text-align: center;'>
        <img src='https://tse1.mm.bing.net/th/id/OIP.eGuC1u0PxIsyphTNSAUGhAHaHa?rs=1&pid=ImgDetMain' height='350' width='350'/>
    </div>
    """,
    unsafe_allow_html=True
)

# Text input
user_input = st.text_area("Please enter your movie synopsis:")

# Submit button
if st.button("Submit"):
    if user_input.strip() != "":
        st.success("Well done! Text received!")
    else:
        st.warning("Please enter some text before submitting.")