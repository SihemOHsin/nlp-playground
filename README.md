# NLP Playground - Application Streamlit Pour MPDSIR AI projet

## Aperçu
Ce projet est une application Streamlit qui permet d'explorer diverses fonctionnalités de Traitement du Langage Naturel (NLP), notamment :

- **Analyse de Sentiments**
- **Résumé de Texte**
- **Reconnaissance d'Entités Nommées (NER)**
- **Extraction de Mots-Clés**
- **Génération de Nuage de Mots**

L'application est conçue pour être conviviale et interactive, ce qui en fait un excellent outil pour apprendre et expérimenter avec les techniques de NLP.

## Fonctionnalités

### 1. Analyse de Sentiments
- Analyse le sentiment du texte saisi (**Positif, Négatif ou Neutre**).
- Affiche un score de polarité et un **graphique en barres**.

### 2. Résumé de Texte
- Résume le texte saisi en **3 phrases clés** en utilisant l'algorithme **LSA (Latent Semantic Analysis)**.

### 3. Reconnaissance d'Entités Nommées (NER)
- Identifie et extrait les entités (**personnes, organisations, lieux**) du texte saisi.

### 4. Extraction de Mots-Clés
- Extrait les **5 mots-clés les plus importants** du texte saisi en utilisant l'algorithme **RAKE (Rapid Automatic Keyword Extraction)**.

### 5. Génération de Nuage de Mots
- Génère une **visualisation sous forme de nuage de mots** à partir du texte saisi.

---
## Installation

### Prérequis
- **Python 3.10 ou 3.11** (recommandé pour la compatibilité avec toutes les bibliothèques).
- **Streamlit, spaCy, NLTK** et les autres bibliothèques nécessaires.

### Étapes d'Installation

#### 1. Cloner le Répertoire
```bash
git clone https://github.com/SihemOHsin/nlp-playground.git
cd nlp-playground
```

#### 2. Créer un Environnement Virtuel (optionnel mais recommandé)
```bash
python -m venv nlp_env
source nlp_env/bin/activate  # Sur Windows : nlp_env\Scripts\activate
```

#### 3. Installer les Bibliothèques Requises
```bash
pip install streamlit textblob pandas spacy sumy rake-nltk wordcloud matplotlib nltk
```

#### 4. Télécharger le Modèle spaCy
```bash
python -m spacy download en_core_web_sm
```

#### 5. Télécharger les Ressources NLTK
```python
import nltk
nltk.download('stopwords')
nltk.download('punkt')
```

---
## Exécution de l'Application

#### 1. Naviguer vers le Répertoire du Projet
```bash
cd nlp-playground
```

#### 2. Lancer l'Application Streamlit
```bash
streamlit run nlp_app.py
```

#### 3. Ouvrir l'Application
L'application s'ouvrira dans votre navigateur à l'adresse **[http://localhost:8501](http://localhost:8501)**.

Utilisez la barre latérale pour sélectionner les fonctionnalités NLP que vous souhaitez explorer.

---
## Dépendances et Leur Utilité

1. **Streamlit** (`streamlit`) : Interface utilisateur interactive.
2. **TextBlob** (`textblob`) : Analyse de Sentiments.
3. **spaCy** (`spacy`) : Reconnaissance d'Entités Nommées (NER).
4. **Sumy** (`sumy`) : Résumé de Texte avec LSA.
5. **RAKE-NLTK** (`rake-nltk`) : Extraction de Mots-Clés.
6. **WordCloud** (`wordcloud`) : Génération de Nuage de Mots.
7. **Matplotlib** (`matplotlib`) : Visualisation des graphiques.
8. **NLTK** (`nltk`) : Gestion des stopwords et tokenisation.

---
## Dépannage

### 1. Modèle spaCy Introuvable
**Erreur** : `OSError: [E050] Can't find model 'en_core_web_sm'`

**Solution** :
```bash
python -m spacy download en_core_web_sm
```

### 2. Ressources NLTK Manquantes
**Erreur** : `Resource 'stopwords' not found`

**Solution** :
```python
import nltk
nltk.download('stopwords')
nltk.download('punkt')
```

### 3. L'Application Streamlit Ne Fonctionne Pas
**Assurez-vous que Streamlit est installé** :
```bash
pip install streamlit
```
**Lancez l'application avec** :
```bash
streamlit run nlp_app.py
```

---
## Licence
Ce projet est sans licence .

---
## Contact
Pour toute question ou suggestion, contactez-moi :

🐙 **GitHub** : `https://github.com/SihemOHsin`

---
**Amusez-vous bien à explorer le NLP avec le NLP Playground ! 🚀**
