from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

class ENGSM:
    ISO_639_1='en_core_web_sm'

bot_name = "Bot"
chatbot = ChatBot(bot_name, tagger_language=ENGSM)

conversation = ['Hello', 'Hi', 'How are you?', "I'm great!", 
			'Do you like to program?', 'Yes, I love to program using Python.']

trainer = ListTrainer(chatbot)
trainer.train(conversation)

while(True):
    text = input("$You: ")

    if(text == 'exit'):
        print('Closing...')
        exit()

    response = chatbot.get_response(text)
    print(f"${bot_name}: {response}")

    