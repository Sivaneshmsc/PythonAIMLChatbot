from os import walk
import os

f = "<aiml version='1.0.1' encoding='UTF-8'><category><pattern>LOAD AIML B</pattern><template>"

for (dirpath, dirnames, filenames) in walk("./aiml/"):
    for filename in filenames:
        f = f + "<learn>./aiml/" + str(filename) + "</learn>"

f = f + "</template></category></aiml>"

if os.path.exists("brain.aiml"):
  os.remove("brain.aiml")

file= open("brain.aiml","w+")
file.write(str(f))