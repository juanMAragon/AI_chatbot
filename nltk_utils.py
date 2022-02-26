from lib2to3.pgen2 import token
import nltk
from nltk.stem.porter import PorterStemmer
import numpy as np 

# nltk.download('punkt')
stemmer = PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())  


def bag_of_words(tokenized_sentence, all_words):
    
    tokenized_sentence = [stem(w) for w in tokenized_sentence]
    bag = np.zeros(len(all_words), dtype=np.float32)

     


if __name__ == '__main__':
    print('----------tokenize---------------')
    a = 'How long does shipping take?'
    print(a)
    a = tokenize(a)
    print(a)
    print('------------stemming-------------')
    words = ['organize', 'organizes', 'organizing']
    stemmed_words = [stem(w) for w in words]
    print(words)
    print(stemmed_words)
    print('-------------------------')
