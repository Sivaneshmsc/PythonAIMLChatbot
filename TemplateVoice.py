import pyttsx3
voiceEngine = pyttsx3.init()
voiceEngine.say("My first code on text-to-speech")
voiceEngine.runAndWait()
# newVoiceRate = 50
# while newVoiceRate <= 300:
#     print('newVoiceRate', newVoiceRate)
#     voiceEngine.setProperty('rate', 120)
#     voiceEngine.say('My first code on text-to-speech')
#     voiceEngine.runAndWait()
#     newVoiceRate = newVoiceRate + 50

voiceEngine.setProperty('rate', 125)

newVolume = 0.1
while newVolume <= 1:
    voiceEngine.setProperty('volume', newVolume)
    voiceEngine.say('Testing different voice volumes.')
    voiceEngine.runAndWait()
    newVolume = newVolume + 0.3

voiceEngine.say("My first code on text-to-speech")
voiceEngine.say("Thank you, Geeksforgeeks")
voiceEngine.runAndWait()