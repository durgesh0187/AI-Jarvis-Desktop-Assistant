import pyttsx3  #pip install pyttsx3
import speech_recognition as sr  #pip install speech recognition
import datetime
import wikipedia  #for searching on wikipedia  pip install wikipedia
import smtplib  #for sending email    pip install smtplib
import webbrowser as wb
import os


engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)



def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(year)
    speak(month)
    speak(day)


def wishme():
    speak("Welcome back Mansi ma'am!")
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour>= 6  and hour<12:
        speak("Good morning sir!")
    elif hour>= 12 and hour<18:
        speak("Good afternoon sir!")
    elif hour>=18 and hour<24:
        speak("Good evening sir!")
    else:
        speak("Good night sir!")

    speak("Jarvis at youe service Please tell me how can i help you?")



def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recognizning...")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"

    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smpt.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('golusingh200010@gmail.com', 'durgesh7979')
    server.sendmail('golusingh200010@gmail.com',to, content)
    server.close()

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()

        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = 'durgeshkumar0187@gmail.com'
               # sendEmail(to,content)

                speak(content)
            except Exception as e:
                print(e)
                speak("Uable to send the email")

        elif 'search in chrome' in query:
            speak("what should i search ?")
            chromepath = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
            search = takecommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')


        elif 'logout' in query:
            os.system("shutdown -1")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")




        elif 'play songs' in query:
            songs_dir = 'D:\song\Music'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))



        elif 'remember that' in query:
            speak("What should I remember?")
            date = takecommand()
            speak("you said me to remember that"+date)
            remember = open('data.txt','w')
            remember.write(date)
            remember.close()

        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak("you said me to to remember that" +remember.read())


        elif 'offline' in query:
            speak("Thanku Durgesh sir!")
            quit()




        


