from common_import import *

from nltk.corpus import gutenberg

# this will create list of sentence tokens
gberg_tokens = sent_tokenize(gutenberg.raw())

word_tokens = word_tokenize(gberg_tokens[2])

word_tokens

