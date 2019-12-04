# AIML Chatbot
Forked from the [python-aiml-chatbot](https://github.com/datenhahn/python-aiml-chatbot) and 
requires installation of ``python-aiml`` library.

## Purpose
The implementation is PoC about chatbot influencing by external signal or data.
It contains three possible ways how to achieve influence of AIML chatbot:
1. By the content of answer and distinguish the NLG response based on  ``<topic>`` and ``<pattern>``.
1. By using the ``<condition>`` tag with the predictor, which defines the flow of the NLG part of the chatbot.
1. By utilizing the ``<think>`` tag with set state based on which should affect the NLG part of the chatbot.

## Condition via question
Uses ``project\condition_via_question.aiml`` AIML dialogue in the ``chatbot_question.py`` Python script.
It reacts conditionally based on the response on the clarification via the question, which is then saved as an internal variable.

See the example of conversation:
```
Loading project/condition_via_question.aiml...done (0.11 seconds)
HUMAN: Do you find me really attractive?
BOT: What is your gender?  In case you don't mind?
HUMAN: female
BOT: I find you very pretty!
HUMAN: Do you find me really attractive?
BOT: What is your gender?  In case you don't mind?
HUMAN: male
BOT: I find you very handsome!
```

## Condition via predictor
Uses ``project\condition_via_predictor.aiml`` AIML dialogue in the ``chatbot_predictor.py`` Python script.
It generates randomly the signal ``SIG = ["yes","no","unknown"]`` and base on its value the chatbot generates the response.

See the example of conversation:
```
Loading project/condition_via_predictor.aiml...done (0.13 seconds)
SIG: yes
HUMAN: hi
BOT: Relax, don't worry!
SIG: no
HUMAN: hi
BOT: The world is perfect again!
SIG: yes
HUMAN: exit
BOT: Bye!
```

## Condition via thinking
Uses ``project\condition_via_think.aiml`` AIML dialogue and it is not implemented.

## Conclusion
The first example **Condition via question** is typical __In Foreground__ influence, i.e., it is a part of the conversation. The user needs to provide such information explicitly.
On the other hand, the second example *Condition via predictor* is typical __On Background__ influence, i.e., the user is not aware of providing influencing data or signal which is collected independently.
