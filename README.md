# Billy-Bot
A fun little chat bot trying to learn

This program is an implementation of a chatbot named Billy-Bot. It uses the ChatterBot library to generate responses to user input. The bot can also log conversations in a JSON file and ask the user for input when it is unable to generate a proper response.

Here's a detailed breakdown of the different parts of the code:

Import Statements
The program starts with a series of import statements that import the necessary libraries and modules:

python
Copy code
import json
import codecs
import os

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
json is a built-in Python library that provides a way to work with JSON data.
codecs is a built-in Python library that provides a way to work with encodings and decoding of data.
os is a built-in Python library that provides a way to interact with the operating system, such as working with files and directories.
chatterbot is a Python library that provides a framework for building chatbots.
ChatterBotCorpusTrainer is a class in the chatterbot.trainers module that provides a way to train a ChatterBot instance using a corpus of conversational data.
run_python_file() Function
The run_python_file() function checks for Python files in the current directory and provides the user with a list of available files. If the user chooses a file, the function executes the file using the exec() function.

Creating the ChatBot Instance
The program creates an instance of the ChatBot class with the name "Billy-Bot". This instance will be used to generate responses to user input.

scss
Copy code
bot = ChatBot('Billy-Bot')
Training the ChatBot Instance
The ChatterBotCorpusTrainer instance is created to train the ChatBot instance with conversational data from the "chatterbot.corpus.english" corpus.

scss
Copy code
trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.english')
log_conversation() Function
The log_conversation() function takes in a user input and a bot response and logs them in a JSON file named "Billys-Brain.json". The user input and bot response are encoded in hexadecimal format before being written to the file.

Chatting with the Bot
The program enters a while loop that continuously prompts the user for input. If the user inputs "run py", the program runs the run_python_file() function. If the user inputs anything else, the ChatBot instance generates a response based on the input using the get_response() method.

If the bot's confidence level in its response is less than 0.5, it will log the conversation and ask the user for input using the input() function. The user's response is then logged.

If the bot's confidence level is greater than or equal to 0.5, the bot's response is printed to the console using the print() function. The conversation is then logged and the ChatterBotCorpusTrainer instance is used to train the ChatBot instance with the new input and response.

Handling Exceptions
The program uses a try-except block to handle any exceptions that might occur while running the program, such as a keyboard interrupt or the user typing "exit". When an exception is caught, the program breaks out of the while loop and exits.

And that's it! That's how this program works.
