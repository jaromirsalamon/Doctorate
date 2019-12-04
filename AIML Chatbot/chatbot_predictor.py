#!/usr/bin/python3
# https://www.devdungeon.com/content/ai-chat-bot-python-aiml
# https://pandorabots.github.io/aiml/condition/
# http://nullege.com/codes/search/aiml.Kernel.setBotPredicate
# http://written-in-codes.blogspot.ch/2012/11/build-chat-bot-with-almost-no-code.html
# http://webseitz.fluxent.com/wiki/AIML
# https://ravispeaks.wordpress.com/tag/pyaiml/

# python-aiml, resp. PyAIML
import aiml
import random

random.seed(123)
stress = ["yes","no","unknown"]

k = aiml.Kernel()
k.learn("project/condition_via_predictor.aiml")

# Endless loop which passes the input to the bot and prints its response
while True:
    g = stress[random.randint(0,2)]
    print('SIG: %s' % g)
    k.setPredicate("stress", g)

    input_text = input("HUMAN: ")
    if input_text == 'exit':
        print('BOT: Bye!')
        break
    response = k.respond(input_text)
    print('BOT: %s' % response)