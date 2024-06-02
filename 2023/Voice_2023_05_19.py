import speech_recognition as sr
import sys

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say Something")
    speech = r.listen(source)
    r.adjust_for_ambient_noise(source)

sys.stdout = open('audio_output.txt', 'w')

try:
    audio = r.recognize_google(speech, language="ko-KR")
    print("Your speech thinks like\n " + audio)
except sr.UnknownValueError:
    print("Your speech can not understand")
except sr.RequestError as e:
    print("Request Error!; {0}".format(e))


from gtts import gTTS as gt

#speech = gt("This is test speech") #-- 영문 출력의 경우
if("실행" in audio):
    speech = gt("다음 운동종목", lang = 'ko')
    speech.save('say_hello.wav') #-- 출력 저장
    

sys.stdout.close()




