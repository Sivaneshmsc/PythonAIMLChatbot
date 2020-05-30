import speech_recognition as sr
import aiml
import os
import pyttsx3

kernel = aiml.Kernel()

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = os.path.abspath("brain.aiml"), commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")

r = sr.Recognizer()
mic = sr.Microphone()

engine = pyttsx3.init()
engine.setProperty('rate', 120)

print("Micky the bot is ready to hear.")
shutdownKeyword = 'shutdown'
def speak_bot():
    user = ''
    while user!=shutdownKeyword:
        with mic as source:
            try:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                user = r.recognize_google(audio)
                if user != '' and user != shutdownKeyword:
                    print('User : ', user)
                    bot_response = kernel.respond(user)
                    engine.say(bot_response)
                    print("Bot : ", bot_response)
                    engine.runAndWait()
                if user == shutdownKeyword:
                    engine.say('Bye bye')
                    engine.runAndWait()
                    print("Bye bye...")
            except:
                pass

speak_bot()
