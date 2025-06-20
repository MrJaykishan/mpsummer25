from gtts import gTTS
from playsound import playsound
text=input("Enter any text u want to speak")
print(text)
a=gTTS(text)
a.save('audio.mp3')
playsound('audio.mp3')