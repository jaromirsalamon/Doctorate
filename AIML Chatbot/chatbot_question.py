import os
import aiml

BRAIN_FILE = "brain.dump"

k = aiml.Kernel()
print("Parsing aiml files")
k.learn("project/condition_via_question.aiml")

# Test 1
print('HUMAN: Do you find me really attractive?')
response1 = k.respond('DO YOU FIND ME REALLY ATTRACTIVE?')
print('BOT: %s' % response1)
print('HUMAN: female')
response2 = k.respond('FEMALE')
print('BOT: %s' % response2)

# Test 2
print('HUMAN: Do you find me really attractive?')
response1 = k.respond('DO YOU FIND ME REALLY ATTRACTIVE?')
print('BOT: %s' % response1)
print('HUMAN: male')
response2 = k.respond('MALE')
print('BOT: %s' % response2)