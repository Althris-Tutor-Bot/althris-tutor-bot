import os
import json
import nltk  # Natural Language Toolkit
import pickle  # To dump large python data structures (lists, dictionaries etc.) into files so that they can be loaded in and worked with as python data structures.
import re  # To match regular expressions.


def load_data(self):  # self is a Chatbot instance. This method is never explicitly called, but it is imported into the class defined in __init__ in order to save space.
    with open(os.path.join(os.path.dirname(__file__), "..", "..", "intent", "intent.json"), encoding="utf-8") as file:  # os.path.dirname() returns the full path to the directory a folder is in
        self.dataset = json.load(file)  # Loads dataset intents from a json file as a python dictionary.

    try:
        with open(os.path.join(os.path.dirname(__file__), "..", "..", "Data", "data_patterns.pickle"), "rb") as f:
            self.wordbank, self.tags, self.training, self.output = pickle.load(f)  # Tries to load the arrays that have been produced in a previous run of the chatbot.
    except FileNotFoundError as e:  # If these files do not exist, generate the arrays.
        print(e)
        patterns = []
        patterns_tags = []

        for intent in self.dataset["intents"]:
            if intent["tag"] not in self.tags:
                self.tags.append(intent["tag"])

            for pat in intent["question"]:
                token_word = nltk.word_tokenize(pat)
                token_stem_word = []

                for w in token_word:
                    if re.match('[a-z]', w.lower()) is not None:  # If there are alphabetical characters in the string
                        w = self.snowball_stemmer.stem(w.lower())  # Takes in a word and returns its stem. for example apple -> appl, revived -> reviv
                        self.wordbank.append(w)
                        token_stem_word.append(w)
                    else:
                        continue

                patterns.append(token_stem_word)
                patterns_tags.append(intent["tag"])

        self.wordbank = sorted(list(set(self.wordbank)))  # Removes duplicates and sorts alphabetically.
        self.tags = sorted(self.tags)

        out_empty = [0] * len(self.tags)  # if len(self.tags) is 5, out_empty becomes [0, 0, 0, 0, 0].

        for i, p in enumerate(patterns):
            bag = []

            for w in self.wordbank:
                if w in p:
                    bag.append(1)
                else:
                    bag.append(0)

            output_row = out_empty[:]
            output_row[self.tags.index(patterns_tags[i])] = 1

            self.training.append(bag)
            self.output.append(output_row)

        os.mkdir(os.path.join(os.path.dirname(__file__), "..", "..", "Data"))

        with open(os.path.join(os.path.dirname(__file__), "..", "..", "Data", "data_patterns.pickle"), "wb") as f:
            pickle.dump((self.wordbank, self.tags, self.training, self.output), f)
