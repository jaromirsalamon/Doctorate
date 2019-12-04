import os
import aiml

BRAIN_FILE = "brain.dump"

k = aiml.Kernel()
print("Parsing aiml files")
k.learn("project/condition_via_question.aiml")

# Test 1
print('DO YOU FIND ME REALLY ATTRACTIVE')
response1 = k.respond('DO YOU FIND ME REALLY ATTRACTIVE')
print(response1)
print('FEMALE')
response2 = k.respond('FEMALE')
print(response2)

# Test 2
print('DO YOU FIND ME REALLY ATTRACTIVE')
response1 = k.respond('DO YOU FIND ME REALLY ATTRACTIVE')
print(response1)
print('MALE')
response2 = k.respond('MALE')
print(response2)