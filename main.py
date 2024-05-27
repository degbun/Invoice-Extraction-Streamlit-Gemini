import os
import streamlit as st
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv
from src.utils import initialize_model, get_image_bytes, get_response

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the Streamlit app
def main():
    st.set_page_config(page_title="Invoice Extractor")
    st.header("Invoice Extractor")

    # Initialize session state for history
    if 'history' not in st.session_state:
        st.session_state.history = []

    uploaded_image = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])

    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption="Your image", use_column_width=True)

        prompt = st.text_input("Enter your prompt", key="prompt", placeholder="e.g.,  Give me a table for particulars and price lists.")
        submit = st.button("Submit")

        model = initialize_model("gemini-pro-vision")

        if submit and prompt:
            image_info = get_image_bytes(uploaded_image)
            model_behavior = """
            You are an expert who understands invoice overall structures and has deep knowledge of it.
            We will upload the invoice image and you have to answer the question based on the information 
            present in the invoice image. If the question is related to something that's not on the image just say: 
            "this information is not present on the image."
            """
            response = get_response(model, model_behavior, image_info, prompt)

            # Store the result in the session state history
            st.session_state.history.append({"prompt": prompt, "response": response})

            # Display the response
            st.subheader("Response")
            st.write(response)
        elif submit:
            st.error("Please enter a valid prompt!")
    else:
        st.info("Please upload an image file to proceed.")

    # Display history
    if st.session_state.history:
        st.subheader("History")
        for idx, entry in enumerate(st.session_state.history):
            st.write(f"**Prompt {idx + 1}:** {entry['prompt']}")
            st.write(f"**Response:** {entry['response']}")

if __name__ == "__main__":
    main()
