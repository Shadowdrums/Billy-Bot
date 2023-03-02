import json
import codecs
import os

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer


def run_python_file():
    files = []
    for file_name in os.listdir(os.getcwd()):
        if file_name.endswith('.py'):
            files.append(file_name)
    if len(files) > 0:
        print('The following Python files are available in the current directory:')
        for i, file_name in enumerate(files):
            print(f'{i + 1}. {file_name}')
        while True:
            try:
                choice = int(input('Enter the number of the file you want to run: '))
                if choice < 1 or choice > len(files):
                    print('Invalid choice. Please try again.')
                else:
                    file_path = os.path.join(os.getcwd(), files[choice - 1])
                    print(f'Running {file_path}...')
                    exec(open(file_path).read())
                    break
            except ValueError:
                print('Invalid choice. Please try again.')


bot = ChatBot('Billy-Bot')

# Create a new instance of the ChatterBotCorpusTrainer using the English corpus
corpus_trainer = ChatterBotCorpusTrainer(bot)
corpus_trainer.train('chatterbot.corpus.english')

# Create a new instance of the ListTrainer using the data from the Billys-Brain.json file
brain_trainer = ListTrainer(bot)
with open('Billys-Brain.json', 'r') as f:
    brain_data = json.load(f)
brain_trainer.train(brain_data)


def log_conversation(user_input, bot_response):
    current_dir = os.getcwd()
    with codecs.open(os.path.join(current_dir, 'Billys-Brain.json'), 'a', encoding='utf-8') as f:
        user_input_hex = codecs.encode(user_input.encode('utf-8'), 'hex').decode('utf-8')
        bot_response_hex = codecs.encode(bot_response.encode('utf-8'), 'hex').decode('utf-8')
        conversation = {'text': user_input_hex, 'in_response_to': bot_response_hex}
        json.dump(conversation, f)
        f.write('\n')


print('Welcome to Billy-Bot. How can I help you today?')

while True:
    try:
        user_input = input('You: ')

        if user_input.lower() == 'run py':
            run_python_file()
            continue

        response = bot.get_response(user_input)

        if response.confidence < 0.5:
            log_conversation(user_input, 'No proper response')
            user_answer = input('Billy-Bot: I am sorry, I do not have an answer. Can you please provide one? ')
            log_conversation(user_input, user_answer)
        else:
            print('Billy-Bot:', response)
            log_conversation(user_input, response)

    except (KeyboardInterrupt, EOFError, SystemExit):
        break
