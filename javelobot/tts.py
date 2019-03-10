from gtts import gTTS


output = open('output2.txt', 'r')

data = output.read()
tts = gTTS(data)
tts.save('fulllecture.mp3')
