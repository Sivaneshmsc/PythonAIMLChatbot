import os

brainfile = open("brain.aiml", "w+")
brainfile.write("<aiml version='1.0.1' encoding='UTF-8'>")
brainfile.write("\n<category>")
brainfile.write("\n<pattern>LOAD AIML B</pattern>")
brainfile.write("\n<template>")

path = 'D:\Siva\Workouts\Python\Chatbot\AIMLChatbot\\aiml\\'
files = []
for r, d, f in os.walk(path):
    for file in f:
        if '.aiml' in file:
            brainfile.write("\n<learn>aiml/" + str(file) + "</learn>")

brainfile.write("\n</template>")
brainfile.write("\n</category>")
brainfile.write("\n</aiml>")
brainfile.close()
