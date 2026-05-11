import streamlit as st
# st.write("App Started")
import torch

from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification
)
# st.write("Imports Done")
# -----------------------------
# Load Saved BERT Model
# -----------------------------
MODEL_PATH = "bert_sms_classifier"
# st.write("Loading Tokenizer")
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
# st.write("Tokenizer Loaded")
# st.write("Loading Model")
model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_PATH,
    local_files_only=True
)
# st.write("Model Loaded")
# Set model to evaluation mode
model.eval()

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(
    page_title="Spam Classifier",
    page_icon="📩"
)

st.title("📩 Email / SMS Spam Classifier")
st.write("Built using DistilBERT Transformer")

input_mail = st.text_area(
    "Enter your message",
    height=150
)

predict = st.button("Predict")

# -----------------------------
# Prediction
# -----------------------------
if predict:

    if input_mail.strip() == "":
        st.warning("Please enter a message.")

    else:

        # Tokenize input text
        inputs = tokenizer(
            input_mail,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=128
        )

        # Prediction
        with torch.no_grad():

            outputs = model(**inputs)

            prediction = torch.argmax(
                outputs.logits,
                dim=1
            ).item()

        # Display Result
        if prediction == 1:

            st.error("🚨 Spam Message")

        else:

            st.success("✅ Not Spam")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("Transformer-based Spam Detection using DistilBERT")