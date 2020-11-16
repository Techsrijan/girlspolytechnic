from gtts import gTTS
from playsound import playsound
tts = gTTS('kya hal hi sab kuch thik hi')
tts.save('techsrijan.mp3')
playsound('techsrijan.mp3')