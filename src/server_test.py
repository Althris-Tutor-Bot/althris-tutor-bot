"""
------------------------------
chatbot_cmd.py

A command line utility that utilises the chatbot package to allow communication with the chatbot locally in the terminal.
To be used during testing before deployment.
------------------------------
"""


import requests
import json


if __name__ == '__main__':
    print("##########")
    print("AI Chatbot")
    print("##########")
    print("Please enter text to start talking to chatbot (type quit to stop)")
    while True:
        message = input("You: ")
        if message.lower() == "quit":  # Checking if the user has asked to quit
            exit(0)  # Terminates the program.
        else:
            response = requests.get(
                "https://p46vbj47a8.execute-api.eu-west-3.amazonaws.com/default/chatbot-lambda",
                params={"question": message}
            ).json()["body"]
            print(response)  # This message is outputted to the screen.
