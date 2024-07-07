from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load the Hugging Face model and tokenizer
model_name = "ahmedheakl/bert-resume-classification"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)


def classify_text(text):
    inputs = tokenizer(text, return_tensors="pt",
                       truncation=True, padding=True)
    outputs = model(**inputs)
    probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
    predicted_class = torch.argmax(probabilities).item()
    return predicted_class
