# Invoice-Extraction-Streamlit-Gemini ![Status](https://img.shields.io/badge/status-stable-brightgreen) ![Python Version](https://img.shields.io/badge/python-3.10.12-blue) ![Streamlit Version](https://img.shields.io/badge/Streamlit-1.28.2-brightgreen) ![Jupyter](https://img.shields.io/badge/Jupyter-yes-brightgreen)
This project is a Streamlit application that utilizes Google Gemini to extract information from invoice images. 
It allows users to upload an invoice image, ask questions about the details of the invoice, and automatically extract relevant information from the image.

## Installation
To install and run this project, you need to follow these steps :

#### Step 0: Clone the project
- On Lunix/unbuntu
```bash
git clone https://github.com/degbun/Invoice-Extraction-Streamlit-Gemini.git
# enter in the cloned folder
cd Invoice-Extraction-Streamlit-Gemini

```


#### Step 1: Create a virtual environnement
- On Lunix/unbuntu
```bash
python3 -m venv venv
```
- On Windows
```bash
python -m venv venv
```

#### Step 2: Activate the a virtual environnement
- On Lunix/unbuntu
```bash
source venv/bin/activate
```
- On Windows
```bash
venv\Scripts\activate
```

#### Step 3: install the requirements

```bash
pip install -r requirements.txt
```

#### Step 4: run the app

```bash
streamlit run main.py
```






