import pyttsx3
engine = pyttsx3.init() # object creation

for i in range(1,10):
    engine.say(str(i))
    print(i)
    engine.runAndWait()