"""--------------------
Create a bag of words for users input
In:
    user_input - what the user has said
    wordbank - a list of all the words, from the patterns in the intent file
Out:
    bag - A list that has a 1 to 1 correspondence withs the wordbank.
          With a 1 if the word was in the user input otherwise 0.
--------------------"""


import nltk
import numpy as np
import unidecode


def bag_of_words(self, user_input, wordbank):
    bag = [0] * len(wordbank)

    user_words = nltk.word_tokenize(user_input)
    for i in range(len(user_words)):
        user_words[i] = unidecode.unidecode(self.snowball_stemmer.stem(user_words[i].lower())).lower()

    for word in user_words:
        for i, w in enumerate(wordbank):
            if w == word:
                bag[i] = 1

    return np.array(bag)


