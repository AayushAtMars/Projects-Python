import speech_recognition as sr
#import pyttsx3
import win32com.client  # module to convert text to speech
#import webbrowser
import os
import datetime
import webbrowser
import google.generativeai as genai
import pyttsx3

def chat(query):
    from apikey import API_KEY
    genai.configure(api_key=API_KEY)
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
    }
    safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    ]

    model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    safety_settings=safety_settings,
    generation_config=generation_config,
    )

    chat_session = model.start_chat(
    history=[
        {
        "role": "user",
        "parts": [
            "hy\n",
        ],
        },
        {
        "role": "model",
        "parts": [
            "Hello! How can I help you today? \n",
        ],
        },
    ]
    )

    response = chat_session.send_message(query)

    print(response.text)
    say(response.text)
    
    
    
def write_text(query):
    print("Writing in file......")
    say("Writing in file......")
    from apikey import API_KEY
    genai.configure(api_key=API_KEY)
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 5000,
    "response_mime_type": "text/plain",
    }
    safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    ]

    model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    safety_settings=safety_settings,
    generation_config=generation_config,
    )

    chat_session = model.start_chat(
    history=[
        {
        "role": "user",
        "parts": [
            "hy\n",
        ],
        },
        {
        "role": "model",
        "parts": [
            "Hello! How can I help you today? \n",
        ],
        },
    ]
    )

    response = chat_session.send_message(query)
    c = response.text

    if not os.path.exists("Openai"):
        os.makedirs("Openai")

    # Construct filename
    split=query.split("using AI ")
    filename = f"Openai/{split[1]}.txt"

    # Open the file for writing with UTF-8 encoding and error handling
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(c)
        print("DONE....What more I can do?")
        say("DONE....What more I can do?")
    except Exception as e:
        print(f"Error writing to file: {e}")

def say(text):
    speaker=win32com.client.Dispatch("SAPI.SpVoice")
    #(SAPI.SpVoice) it intracts with microsoft speech SDK to speak what we type from keyboard
    speaker.Speak(text)
    
#     engine = pyttsx3.init()
#     voices = engine.getProperty('voices')

# # Improved logic to identify a female voice (consider language and name)
#     for voice in voices:
#         if 'Microsoft Zira Desktop - English (United States)' in voice.name:  # Check for female and English
#             engine.setProperty('voice', voice.id)
#             break


# #Adjust speaking rate (might indirectly affect perceived pitch)
#     if hasattr(engine, 'setProperty'):
#         engine.setProperty('rate', 140)
#     engine.say(text)
#     engine.runAndWait()

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

def browser(query):
        sites=[["youtube", "https://www.youtube.com"],["wikipedia", "https://www.wikipedia.com"],["instagram", "https://www.instagram.com"],
               ["facebook", "https://www.facebook.com"],["google", "https://www.google.com"],["gmail", "https://mail.google.com/"]]
        for site in sites:
            #import webbrowser
            if f"open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]}......")                         #webbrowser module doesn't provide close function
                webbrowser.open(site[1])
                
                
                
def open_app(query):
        apps=["WhatsApp","Spotify","Notepad","Word","PowerPoint","Excel","Photos","Discord" 
              "Telegram Desktop","Prime Video","Chrome","Calculator","Settings","Camera"]
        for i in apps:
            if f"open {i}".lower() in query.lower():
                from AppOpener import open
                say(f"Opening{i}....")
                open(i)
                
                
def close_app(query):
        apps=["WhatsApp","Spotify","Notepad","Word","PowerPoint","Excel","Photos","Discord" 
              "Telegram Desktop","Prime Video","Chrome","Calculator","Settings","Camera"]
        for i in apps:
            if f"close {i}".lower() in query.lower():
                from AppOpener import close
                say(f"Closing{i}....")
                close(i)

if __name__ =='__main__':
    print("HELLO I AM EDITH")
    print("HOW MAY I HELP YOU")
    say("Hello I am EDITH, how may I help you")
    while True:
        print("listening......")
        query=takecommand()
        
        
        if "open youtube" or "open wikipedia" or "open instagram" or "open facebook" or "open google" or "open mail" in query.lower():
            browser(query)
                
        if "play music" in query:
            #import os
            say("Playing music.....")
            os.startfile("C:\\Users\\ajay1\\Music\\test2.m4a")

        if "time" in query:
            strfTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The Time is {strfTime}")
            say(f"The Time is {strfTime}")

        if "open whatsApp"or"open spotify"or"open notepad"or"open word"or"open powerPoint"or"open excel"or"open photos"or"open discord"or"open telegram"or"open prime video"or"open chrome"or"open calculator"or"open settings"or"open camera" in query.lower():
            open_app(query)
            
            
        if "close whatsApp"or"close spotify"or"close notepad"or"close word"or"close powerPoint"or"close excel"or"close photos"or"close discord"or"close telegram"or"close prime video"or"close chrome" or"close calculator"or"close settings"or"close camera" in query.lower():
            close_app(query)
              
        if "what is the meaning of your name" in query.lower():
            meaning = "This is the name given by my Master, The full form of my Name is Efficient Digital Intelligence and Task Handling"
            print("This is the name given by my Master, The full form of my Name is Efficient Digital Intelligence and Task Handling")
            say(meaning)


        if "using AI".lower() in query.lower():
            write_text(query)



        #if "Jarvis".lower() in query.lower():
        
        if "quit" in query:
            print("Have a nice day")
            say("Have a nice day")
            break 
        else:
            chat(query)

        






        #say(query)
