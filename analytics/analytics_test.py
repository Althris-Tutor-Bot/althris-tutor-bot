"""
------------------------------
chatbot_cmd.py

A command line utility that utilises the chatbot package to allow communication with the chatbot locally in the terminal.
To be used during testing before deployment.
------------------------------
"""


import requests
import pprint

if __name__ == '__main__':
    print("####################")
    print("AI Chatbot Analytics")
    print("####################")
    print()
    pprint.pprint(requests.get(
        f"http://54.78.114.97:3996/",
    ).json())
