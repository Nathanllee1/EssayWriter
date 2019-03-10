from gtts import gTTS


output = open('output.txt', 'r')

data = output.read()
tts = gTTS(data)
tts.save('Javelo.mp3')
