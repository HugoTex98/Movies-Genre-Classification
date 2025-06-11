import streamlit as st

st.title("Movie Genre Detector 🎥🪄")

st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)

# Centered image using markdown and HTML
st.markdown(
    """
    <div style='text-align: center;'>
        <img src='https://tse1.mm.bing.net/th/id/OIP.eGuC1u0PxIsyphTNSAUGhAHaHa?rs=1&pid=ImgDetMain' height='350' width='350'/>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)

st.markdown(
    "<h4 style='margin-top: 30px;'>Please enter your movie synopsis:</h4>",
    unsafe_allow_html=True
)

# Text box
user_input = st.text_area("", placeholder="Insert text here ...", height=150)

# Submit button
if st.button("Submit"):
    if user_input.strip() != "":
        st.success("Well done! Text received!")
    else:
        st.warning("Please enter some text before submitting.")
