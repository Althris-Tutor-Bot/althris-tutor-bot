import numpy as np
import random
import os
import json


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
                if not os.path.isdir(os.path.join(os.path.dirname(__file__), "..", "..", "analytics")):
                    os.mkdir(os.path.join(os.path.dirname(__file__), "..", "..", "analytics"))

                if not os.path.isfile(os.path.join(os.path.dirname(__file__),
                                                   "..", "..", "analytics", "questionable.json")):
                    with open(os.path.join(os.path.dirname(__file__),
                                           "..", "..", "analytics", "questionable.json"), "w+") as _:
                        pass

                with open(os.path.join(os.path.dirname(__file__), "..", "..", "analytics", "questionable.json")) as f:
                    try:
                        data = json.load(f)
                    except Exception as _:
                        data = {
                            "questionable": []
                        }

                    data["questionable"].append({
                        "question": question,
                        "response": pattern['response'],
                        "confidence": str(round(predicted_results[0, result_index] * 100, 2)) + "%"
                    })

                with open(os.path.join(os.path.dirname(__file__), "..", "..",
                                       "analytics", "questionable.json"), "w+") as f:
                    json.dump(data, f, indent=4)

    return random.choice(responses)
