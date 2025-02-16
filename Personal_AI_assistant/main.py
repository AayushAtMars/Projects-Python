import speech_recognition as sr
#import pyttsx3
import win32com.client  # module to convert text to speech
#import webbrowser
import os
import datetime
import openai
import webbrowser


chat1=''
def chat(query):
    global chat1
    print(chat1)
    from apikey import apkey
    openai.api_key=apkey
    chat1+=f"user:{query}\n jarvis: "
    response=openai.Completion.create(
        engine='gpt-3.5-turbo-instruct',
        prompt=query,
        max_tokens=1000
    )
    print(response["choices"][0]["text"])
    say(response["choices"][0]["text"])
    chat1+=f"{response['choices'][0]['text']}\n"
    return response['choices'][0]['text']

def say(text):
    speaker=win32com.client.Dispatch("SAPI.SpVoice") #(SAPI.SpVoice) it intracts with microsoft speech SDK to speak what we type from keyboard
    speaker.Speak(text)

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:  #microphone is also a class we will use it as a source
        r.pause_threshold= 0.6
        audio=r.listen(source)
        try:
            print("recognizing.......")
            query = r.recognize_google(audio, language="en-in")
            #recogniser is the class which helps to recognise voice
            print(f"user said :  {query}")
            return query
        except Exception as e:
            return "some error ocurred sorry"



if __name__ =='__main__':
    print("HELLO I AM YOUR NEXUS")
    print("HOW MAY I HELP YOU")
    say("Hello I am your nexus, how may I help you")
    while True:
        print("listening......")
        query=takecommand()

        sites=[["youtube", "https://www.youtube.com"],["wikipedia", "https://www.wikipedia.com"],["instagram", "https://www.instagram.com"],
               ["facebook", "https://www.facebook.com"],["google", "https://www.google.com"],["gmail", "https://mail.google.com/"]]
        for site in sites:
            #import webbrowser
            if f"open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]}......")                         #webbrowser module doesn't provide close function
                webbrowser.open(site[1])
        if "play music" in query:
            #import os
            say("Playing music.....")
            os.startfile("C:\\Users\\ajay1\\Music\\test2.m4a")

        if "time" in query:
            strfTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The Time is {strfTime}")
            say(f"The Time is {strfTime}")


        apps=["WhatsApp","Spotify","Notepad","Word","PowerPoint","Excel","Photos","Discord",
              "Telegram Desktop","Prime Video","Chrome","Calculator","Settings","Camera"]
        for i in apps:
            if f"open {i}".lower() in query.lower():
                from AppOpener import open
                say(f"Opening{i}....")
                open(i)
            if f"close {i}".lower() in query.lower():
                from AppOpener import close
                say(f"Closing{i}....")
                close(i)


        if "using AI".lower() in query.lower():
            #ai(query)
            from apikey import apkey
            openai.api_key = apkey
            c=f"\n\nOpenAI response for query:  {query} \n              ********************************\n\n"
            response = openai.Completion.create(
                engine='gpt-3.5-turbo-instruct',
                prompt=query,
                max_tokens=100
            )
            c+= (response.choices[0].text.strip())
            from openaitext import b
            #print("Writing in file......")
            #say("Writing in file......")
            #b.write(query)
            b.write(c)
            print("DONE....What more I can do?")
            say("DONE....What more I can do?")


        #if "Jarvis".lower() in query.lower():
        #else:
            #chat(query)

        if "quit" in query:
            print("Have a nice day")
            say("Have a nice day")
            break






        #say(query)
