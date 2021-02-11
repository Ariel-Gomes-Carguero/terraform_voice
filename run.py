import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from python_terraform import *

#Falas pré-configuradas
audio2 = "Infraestrutura Criada"
audio3 = "Infraestrutura Destruida"

#Modulo Terraform
def terraformation(frase):
    tf = Terraform(working_dir='Terraform/')
    tf.init()
    tf.plan()
    tf.apply(skip_plan=True)

def destruir(frase):
    tf = Terraform(working_dir='Terraform/')
    tf.destroy()

#Funcao responsavel por ouvir e reconhecer a fala
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

#Funcao responsavel por falar audio recebido
def welcome(audio2):
    tts = gTTS(audio2,lang='pt-br')
    #Salva o arquivo de audio
    tts.save('audios/hello.mp3')
    #Da play ao audio
    playsound('audios/hello.mp3')

if __name__ == "__main__":
    frase = ouvir_microfone()
    if frase == "criar ec2":
        print("Iniciando construcao da ec2")
        terraformation(frase)
        welcome(audio2)
    elif frase == "destruir infraestrutura":
        destruir(frase)
        welcome(audio3)
    else:
        print("Erro para criar infraestrutura")




