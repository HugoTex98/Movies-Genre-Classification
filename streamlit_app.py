import streamlit as st
import spacy
import joblib
import numpy as np
from pydantic import BaseModel

# --- Load SpaCy model and trained model ---
class UserInput(BaseModel):
    text: str

def load_models():
    nlp = spacy.load("en_core_web_md")
    model = joblib.load("model.pkl")
    return nlp, model

nlp, model = load_models()

def preprocess_and_vectorize(text: UserInput):
    """
    Input: synopsis text (string)
    Output: embeddings of the text
    """
    doc_nlp = nlp(text)
    filtered_tokens = [token.text for token in doc_nlp if not token.is_stop]
    if filtered_tokens:
        vector = nlp(" ".join(filtered_tokens)).vector
    else:
        vector = np.zeros(nlp.vocab.vectors_length)
    return vector.reshape(1, -1)  # Ensure 2D shape for sklearn

# --- Streamlit UI ---
st.title("Movie Genre Detector 🎥🪄")

st.markdown(
    "<p style='margin-top: 25px;'>This application receives a movie synopsis, through text or a .txt file, and retrives its genre. Currently it only supports movie synopsis from cult, dramatic and paranormal genres.</p>",
    unsafe_allow_html=True
)

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
    "<h4 style='margin-top: 25px;'>Please enter your movie synopsis:</h4>",
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
        # Prepare text for the model to predict
        input_vector = preprocess_and_vectorize(processed_text)

        prediction = model.predict(input_vector)

        # Display result
        st.markdown("### Movie Synopsis Genre is:")
        st.write(prediction[0])