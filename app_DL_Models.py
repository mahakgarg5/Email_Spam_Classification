# import streamlit as st
# import pickle
# import string
# import nltk
# from nltk.corpus import stopwords
# from nltk.stem.porter import PorterStemmer
# stop_words = set(stopwords.words('english'))
# ps = PorterStemmer()

# def transform_text(text):
#     text = text.lower()
#     text = nltk.word_tokenize(text)
    
#     y = []
#     for i in text:
#         if i.isalnum():
#             y.append(i)
    
#     text = y[:]
#     y.clear()
    
#     for i in text:
#         if i not in stopwords.words('english') and i not in string.punctuation:
#             y.append(i)
            
#     text = y[:]
#     y.clear()
    
#     for i in text:
#         y.append(ps.stem(i))
    
            
#     return " ".join(y)

# tokenizer = pickle.load(open('tokenizer.pkl','rb'))
# model = pickle.load(open('model_bert.pkl','rb'))

# st.title("Email/SMS Spam classifier")

# input_mail = st.text_input('Enter the message')

# predict = st.button('Predict')

# if predict:
#     # 1. Preprocess
#     transformed_mail = transform_text(input_mail)
#     # 2. Vectorize
#     vector_input = tokenizer.transform([transformed_mail])
#     # 3. Predict
#     result = model.predict(vector_input)[0]
#     # 4. Display
#     if result==1:
#         st.header("Spam")
#     else:
#         st.header("Not Spam")

