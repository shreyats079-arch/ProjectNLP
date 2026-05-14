import string
import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

def preprocess(text):

    # Lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(
        str.maketrans('', '', string.punctuation)
    )

    # Tokenization
    tokens = word_tokenize(text)

    # Stopword Removal
    filtered_tokens = [
        word for word in tokens
        if word not in stop_words
    ]

    return filtered_tokens


sample = "The mobile battery backup is excellent!"

print(preprocess(sample))