import numpy as np
import random


def get_response(self, question):
    # This part classifies the response as either "glossary", "general" or "events"
    user_bag = self.bag_of_words(question, self.wordbank)  # Creates a bag of words out of the question.
    predicted_results = self.model.predict([user_bag])  # Returns an np.array of probabilities for each of the tags in the wordbank.
    result_index = np.argmax(predicted_results)  # Finds the largest
    result_tag = self.tags[result_index]
    responses = []
    for pattern in self.dataset["intents"]:  # Finds the response that corresponds with the tag.
        if pattern['tag'] == result_tag:
            if predicted_results[0, result_index] > 0.3:  # If it is more than 30 percent sure that that is the correct response, return the response
                responses = pattern['response']
            else:
                responses = ["Sorry I did not quite understand that. Please try again!"]

    return random.choice(responses)
