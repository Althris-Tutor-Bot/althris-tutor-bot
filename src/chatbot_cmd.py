"""
------------------------------
chatbot_cmd.py

A command line utility that utilises the chatbot package to allow communication with the chatbot locally in the terminal.
To be used during testing before deployment.
------------------------------
"""


from chatbot import Chatbot  # Importing the chatbot package.

if __name__ == '__main__':
    cb = Chatbot()  # Initialise Chatbot instance. All of the necessary initialisation steps are done here, so no supplementary methods are needed.
    print("##########")
    print("AI Chatbot")
    print("##########")
    print("Please enter text to start talking to chatbot (type quit to stop)")
    while True:
        message = input("You: ")
        if message.lower() == "quit":  # Checking if the user has asked to quit
            exit(0)  # Terminates the program.
        else:
            response = cb.get_response(message)  # If the user hasn't asked to quit, a method from the Chatbot class is called to get a response from the chatbot
            print(response)  # This message is outputted to the screen.
