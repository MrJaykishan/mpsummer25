from gtts import gTTS
from playsound import playsound
start=int(input("enter start number"))
last=int(input("enter end number"))
if start<last:
    i=start
    while i<=last:
        if i % 2 == 0:
            print("even no=", i)
            a = gTTS('Even No')
            a.save('audio1.mp3')
            playsound('audio1.mp3')
        else:
            print("Odd no=", i)
            a = gTTS('Odd1 No')
            a.save('audio2.mp3')
            playsound('audio2.mp3')
        i=i+1
else:
    i = start
    while i >= last:
        if i % 2 == 0:
            print("even no=", i)
            a = gTTS('Even No')
            a.save('audio1.mp3')
            playsound('audio1.mp3')
        else:
            print("Odd no=", i)
            a = gTTS('Odd1 No')
            a.save('audio2.mp3')
            playsound('audio2.mp3')
        i = i - 1