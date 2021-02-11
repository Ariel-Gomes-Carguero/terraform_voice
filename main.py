import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import wikipedia
import time
audio2 = "Bem Vindo a Bat-caverna Senhor Ariel, o que buscar hoje ?"

#Funcao responsavel por ouvir e reconhecer a fala
def cria_audio(audio):
    tts = gTTS(audio,lang='pt-br')
    #Salva o arquivo de audio
    tts.save('audios/hello.mp3')
    print("Trazendo resultados da internet...")
    #Da play ao audio
    playsound('audios/hello.mp3')

def wikicria(frase):
    wikipedia.set_lang("pt")
    busca = wikipedia.summary(frase, sentences=1)
    return busca





def ouvir_microfone():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("Diga alguma coisa: ")
        audio = microfone.listen(source)




    try:
        frase = microfone.recognize_google(audio,language='pt-BR')
        print("Você disse: " + frase)
    except sr.UnkownValueError:
        print("Não entendi")
    return frase


def welcome(audio2):
    tts = gTTS(audio2,lang='pt-br')
    #Salva o arquivo de audio
    tts.save('audios/hello.mp3')
    print("Bem vindo mestre...")
    #Da play ao audio
    playsound('audios/hello.mp3')

welcome(audio2)

while True:
    frase = ouvir_microfone()
    testando = wikicria(frase)
    cria_audio(testando)