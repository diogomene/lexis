import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

nltk.download("punkt")
nltk.download('punkt_tab')
nltk.download("stopwords")

# Diret´orios com os PDFs
current_dir = os.path.dirname(os.path.abspath(__file__))

diretorios = {
    "poetry": os.path.abspath(os.path.join(current_dir, "../../data/books/poetry/")),
    "philosophy": os.path.abspath(os.path.join(current_dir, "../../data/books/philosophy/")),
    "fiction": os.path.abspath(os.path.join(current_dir, "../../data/books/fiction/"))
}

def limpar_texto(texto):
    stop_words = set(stopwords.words("english"))
    palavras = word_tokenize(texto.lower())
    palavras_limpa = [palavra for palavra in palavras
    if palavra.isalnum()
    and palavra not in stop_words]
    return " ".join(palavras_limpa)

# Extraindo e tratando textos e classes
# Além disso exporta textos em Bag of Words
def get_formated_data():
    textos = []
    classes = []

    def read_txt(caminho):
        with open(caminho, 'rb') as f:
            return f.read().decode('utf-8')

    for classe, caminho in diretorios.items():
        for arquivo in os.listdir(caminho):
                texto = read_txt(os.path.join(caminho, arquivo))
                texto_limpo = limpar_texto(texto)
                textos.append(texto_limpo)
                classes.append(classe)

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(textos)
    return [X, classes]

