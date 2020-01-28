import nltk
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import *

nltk.download('gutenberg')
nltk.download('punkt')
nltk.download('stopwords')

import string

import gensim

from gensim.models.phrases import Phraser,Phrases
from gensim.models.word2vec import Word2Vec

