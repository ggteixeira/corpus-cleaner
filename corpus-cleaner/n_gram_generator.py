""" Reference for extract_ngrams function: 
https://www.pythonprogramming.in/generate-the-n-grams-for-the-given-sentence-using-nltk-or-textblob.html
"""

import nltk
from nltk.util import ngrams
from random import randrange

def get_text():
    text_file = open(f"corpora/informativo/in_bug_feature_spoladore.txt", "r")
    text = text_file.read()
    text_file.close()
    return text

# Function to generate n-grams from sentences.
def extract_ngrams(text, num):
    n_grams = ngrams(nltk.word_tokenize(text), num)
    return [' '.join(grams) for grams in n_grams]

def write_in_file(generated_ngrams):
    with open("ngrams_terminet/ngrams.txt", "w+") as file:
        for token in generated_ngrams:
            file.write(f"{token} \n")


write_in_file(extract_ngrams(get_text(), 1))