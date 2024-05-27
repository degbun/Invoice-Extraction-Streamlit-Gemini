import google.generativeai as genai

def initialize_model(model_name="gemini-pro-vision"):
    """
    Initializes the generative model.

    Args:
        model_name (str): The name of the model to initialize. Default is "gemini-pro-vision".

    Returns:
        GenerativeModel: An instance of the initialized generative model.
    """
    model = genai.GenerativeModel(model_name)
    return model

def get_image_bytes(uploaded_image):
    """
    Converts the uploaded image into bytes.

    Args:
        uploaded_image: The uploaded image file.

    Returns:
        list: A list containing the mime type and data of the image.

    Raises:
        FileNotFoundError: If no image file is uploaded.
    """
    if uploaded_image is not None:
        image_bytes = uploaded_image.getvalue()
        image_info = [
            {
                "mime_type": uploaded_image.type,
                "data": image_bytes
            }
        ]
        return image_info
    else:
        raise FileNotFoundError("Upload Valid image file!")

def get_response(model, model_behavior, image, prompt):
    """
    Generates a response from the model based on the provided image and prompt.

    Args:
        model: The initialized generative model.
        model_behavior (str): Instructions for the model's behavior.
        image (list): The image data in bytes.
        prompt (str): The prompt for the model.

    Returns:
        str: The generated response from the model.
    """
    response = model.generate_content([model_behavior, image[0], prompt])
    return response.text