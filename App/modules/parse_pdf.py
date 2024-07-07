from langchain_community.document_loaders import PyMuPDFLoader
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re
import string


def load_pdf(file_path):
    loader = PyMuPDFLoader(file_path)
    data = loader.load()
    return data


def clean_text(text):
    # Remove special characters (customize as needed)
    special_characters = "○●•◦"
    text = re.sub(f"[{re.escape(special_characters)}]", "", text)

    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Remove numbers
    text = re.sub(r'\d+', '', text)

    # Remove extra whitespace
    text = " ".join(text.split())

    # Convert text to lowercase
    text = text.lower()

    # Remove stopwords (optional)
    stop_words = set(stopwords.words('english'))
    text = " ".join(word for word in text.split() if word not in stop_words)

    # Stemming (optional)
    ps = PorterStemmer()
    text = " ".join(ps.stem(word) for word in text.split())

    return text


def get_full_resume_text(file_path):
    resume_pages = load_pdf(file_path)
    resume_text = ""

    for page in resume_pages:
        resume_text += page.page_content
        resume_text += "\n\n"

    resume_text = clean_text(resume_text)

    return resume_text


def process_pdf(file):
    return get_full_resume_text(file.name)
