import streamlit as st
import spacy
import pandas as pd
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lsa import LsaSummarizer
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import subprocess

from textblob import TextBlob

# --- GENERAL SETTINGS ---
favicon = "https://res.cloudinary.com/dvz16ceua/image/upload/v1738438460/favicon_rhnsk6.png"
PAGE_TITLE = "MPDSIR | NLP Playground"

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title=PAGE_TITLE, page_icon=favicon, layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
    section[data-testid="stSidebar"] { width: 300px !important; flex-shrink: 0 !important; }
    .stButton button { width: 100%; background-color: #4CAF50; color: white; }
    .stButton button:hover { background-color: #45a049; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Define SpacyTokenizer class
class SpacyTokenizer:
    def __init__(self, language="en"):
        self.nlp = spacy.load("en_core_web_sm")

    def to_sentences(self, text):
        doc = self.nlp(text)
        return [sent.text for sent in doc.sents]  # Split into sentences

    def to_words(self, text):
        doc = self.nlp(text)
        return [token.text for token in doc if not token.is_stop and token.is_alpha]  # Return words excluding stop words and punctuation



# Load spaCy model for NLP tasks
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")



# Set title
st.title("NLP Playground")
st.write("Explorez l'analyse de sentiment, le résumé de texte, la reconnaissance des entités nommées, l'extraction de mots-clés et la génération de nuages de mots . Explore Sentiment Analysis, Text Summarization, Named Entity Recognition, Keyword Extraction, and Word Cloud Generation!")

# User input text
user_input = st.text_area("Entrez votre texte :", placeholder="Type or paste your text here...")

# Sidebar options
# Options dans la barre latérale
with st.sidebar:
    st.header("Choisissez une fonctionnalité")
    options = st.multiselect(
        "Que voulez-vous analyser ?",
        ["Analyse de Sentiment", "Résumé de Texte", "Reconnaissance des Entités Nommées", "Extraction de Mots-Clés", "Nuage de Mots"],
        default=["Analyse de Sentiment"]
    )

# 🔹 Analyse de sentiment (Utilisation de spaCy)

if "Analyse de Sentiment" in options:
    st.subheader("Analyse de Sentiment")
    if user_input:
        blob = TextBlob(user_input)
        sentiment_score = blob.sentiment.polarity  # Get the polarity score

        sentiment = "Neutre 😐"
        if sentiment_score > 0:
            sentiment = "Positif 😊"
        elif sentiment_score < 0:
            sentiment = "Négatif 😠"

        st.write(f"**Sentiment :** {sentiment}")
        st.write(f"**Score de polarité :** {sentiment_score:.2f}")
        st.bar_chart(pd.DataFrame({"Polarité": [sentiment_score]}, index=["Sentiment"]))
    else:
        st.warning("Veuillez entrer un texte pour l'analyse de sentiment !")



# 🔹 Résumé de texte (Utilisation du tokenizer spaCy)
if "Résumé de Texte" in options:
    st.subheader("Résumé de Texte")
    if user_input:
        parser = PlaintextParser.from_string(user_input, SpacyTokenizer())
        summarizer = LsaSummarizer()
        summary = summarizer(parser.document, 3)  # Limite à 3 phrases

        st.write("**Résumé :**")
        for sentence in summary:
            st.write(f"- {str(sentence)}")
    else:
        st.warning("Veuillez entrer un texte à résumer !")


# 🔹 Reconnaissance des entités nommées (NER) avec spaCy
if "Reconnaissance des Entités Nommées" in options:
    st.subheader("Reconnaissance des Entités Nommées")
    if user_input:
        doc = nlp(user_input)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        st.write("**Entités trouvées :**")
        st.dataframe(pd.DataFrame(entities, columns=["Entité", "Catégorie"]))
    else:
        st.warning("Veuillez entrer un texte pour la reconnaissance des entités nommées !")


# 🔹 Extraction de mots-clés (Utilisation de spaCy)
if "Extraction de Mots-Clés" in options:
    st.subheader("Extraction de Mots-Clés")
    if user_input:
        def extract_keywords(text, top_n=5):
            doc = nlp(text.lower())
            words = [token.text for token in doc if token.is_alpha and not token.is_stop]
            word_freq = Counter(words)
            return [word for word, _ in word_freq.most_common(top_n)]

        keywords = extract_keywords(user_input)
        st.write("**Principaux mots-clés :**")
        for i, keyword in enumerate(keywords, 1):
            st.write(f"{i}. {keyword}")
    else:
        st.warning("Veuillez entrer un texte pour extraire des mots-clés !")


# 🔹 Génération de nuage de mots
if "Nuage de Mots" in options:
    st.subheader("Nuage de Mots")
    if user_input:
        wordcloud = WordCloud(width=800, height=400, background_color="white").generate(user_input)
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        st.pyplot(plt)
    else:
        st.warning("Veuillez entrer un texte pour générer un nuage de mots !")