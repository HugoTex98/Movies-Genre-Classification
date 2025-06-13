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

# Upload .txt file
uploaded_file = st.file_uploader("Or upload a .txt file", type=["txt"])

# Read file content if uploaded
file_text = ""
if uploaded_file is not None:
    file_text = uploaded_file.read().decode("utf-8")

# Submit button
if st.button("Submit"):
    # Determine source of input
    if user_input.strip():
        processed_text = user_input.strip()
        st.success("Text from text area received!")
    elif uploaded_file is not None:
        processed_text = file_text
        if processed_text:
            st.success("Text from uploaded file received!")
        else:
            st.warning("Uploaded file is empty.")
            processed_text = None
    else:
        st.warning("Please enter some text or upload a .txt file.")
        processed_text = None

    # Process if there is valid text
    if processed_text:
        # Example: display the processed text
        st.markdown("### Movie Synopsis Genre is:")
        st.write(processed_text)
