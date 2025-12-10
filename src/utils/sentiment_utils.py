import re
from collections import Counter

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


def clean_and_tokenize_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", " ", text)
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t not in stop_words and len(t) > 2]
    tokens = [lemmatizer.lemmatize(t) for t in tokens]
    return tokens

def normalized_frequency(token_list):
    counts = Counter(token_list)
    total = sum(counts.values())

    return {token: count / total for token, count in counts.items()}

def happiness_value(token_list, sentiment_values_dict):
    calc_happiness = {}

    for token in token_list:
        if token in sentiment_values_dict.keys():
            calc_happiness[token] = sentiment_values_dict[token]
        else:
            calc_happiness[token] = 0

    return calc_happiness

def calculate_token_list_sentiment(token_list, sentiment_values_dict):
    p = normalized_frequency(token_list)
    h = happiness_value(token_list, sentiment_values_dict)
    sentiment = 0

    for token in p.keys():
        sentiment += (p[token] * h[token])

    return sentiment


def calculate_text_list_sentiment(text_list, sentiment_values_dict):
    text = " ".join(text_list)
            
    token_list      = clean_and_tokenize_text(text)
    sentiment_value = calculate_token_list_sentiment(token_list, sentiment_values_dict)

    return sentiment_value


