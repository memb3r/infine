# pip install chatterbot==1.0.4 pytz
# python3 infine.py
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot('Infine')

trainer = ListTrainer(chatbot)

trainer.train([
    "Hi",
    "Hello, how may I help you?",
    "Hey there!",
    "Greetings!",
    "Good to see you!",
    "Hey!",
    "What's up?",
    "Hi, how are you doing?",
    "Hello!",
    "Hi, nice to meet you!",
    "Hey, what's going on?",
])

trainer.train([
    "Thank you!",
    "You're most welcome!",
    "Thanks!",
    "Of course!",
    "Appreciate it!",
    "Thank you so much!",
    "You're awesome!",
    "Thanks a bunch!",
    "Thanks a million!",
    "You're the best!",
    "I'm grateful!",
])

trainer.train([
    "Who are you?",
    "What is your identity?",
    "Tell me about yourself.",
    "What's your name?",
    "Are you a human or a machine?",
    "Explain what you are.",
    "Can you introduce yourself?",
    "What kind of entity are you?",
    "Define your identity.",
    "Are you a bot or a person?",
])

trainer.train([
    "How are you?",
    "What's up with you?",
    "How's everything?",
    "How are things going?",
    "How's your day?",
    "Are you doing well?",
    "What's your status?",
    "How's life treating you?",
    "What's happening?",
    "How's everything on your end?",
    "What's going on with you?",
])

trainer.train([
    "I am Infine, a language model created to assist and generate text.",
    "I'm an AI designed to help with various tasks and provide information.",
    "I am Infine, a virtual assistant here to assist you.",
    "I'm a language model created by OpenAI called Infine.",
    "I am an artificial intelligence designed for natural language processing.",
    "I'm here to help! I am Infine, a program for natural language understanding.",
    "I'm just a computer program called Infine, but I'm here to assist you.",
    "I'm doing well, thank you! How can I assist you today?",
    "Life in the digital world is treating me well, thanks for asking!",
    "I'm functioning well. How can I help you today?",
    "I don't have feelings, but I'm ready to assist you with any questions you have!",
])

print('''\u001b[35m
 /$$$$$$            /$$$$$$  /$$                    
|_  $$_/           /$$__  $$|__/                    
  | $$   /$$$$$$$ | $$  \__/ /$$ /$$$$$$$   /$$$$$$ 
  | $$  | $$__  $$| $$$$    | $$| $$__  $$ /$$__  $$
  | $$  | $$  \ $$| $$_/    | $$| $$  \ $$| $$$$$$$$
  | $$  | $$  | $$| $$      | $$| $$  | $$| $$_____/
 /$$$$$$| $$  | $$| $$      | $$| $$  | $$|  $$$$$$$
|______/|__/  |__/|__/      |__/|__/  |__/ \_______/\u001b[0m
''')

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"\u001b[35mInfine\u001b[0m: {chatbot.get_response(query)}")
