import smtplib
import speech_recognition as sr
import pyttsx3
listener=sr.Recognizer()
engine=pyttsx3.init()
def talk (text):
    engine.say(text)
    engine.runAndWait()
def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice= listener.listen(source)
            info= listener.recognize_google(voice)
            print (info)
            return info.lower()
    except:
        pass
    def send_email():
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login('samananees86@gmail.com','2001@Nainital')
        server.sendmail('samananees86@gmail.com','zahmad7081@gmail.com','Hi Dude')
        def get_email_info():
            talk('To whom you want to send email')
            get_email_info()



