#e1.py
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pandas as pd
toy_corpus = ["the fat cat sat on the mat","the big cat slept","the dog chased a cat"]
vectorizer = TfidfVectorizer()
corpus_tfidf = vectorizer.fit_transform(toy_corpus)
print("shape of matrix :" ,corpus_tfidf.shape)
df = pd.DataFrame(np.round(corpus_tfidf.toarray(),2))
df.columns = vectorizer.get_feature_names()
print(df.columns)