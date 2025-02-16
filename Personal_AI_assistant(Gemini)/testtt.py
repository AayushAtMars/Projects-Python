# # str="using ai write a code in python"
# # a=str.split("ai")
# # print(a[1])
# import webbrowser
# import pyttsx3
# import speech_recognition as sr


# def say (text):
#     engine = pyttsx3.init()
#     voices = engine.getProperty('voices')

# # Improved logic to identify a female voice (consider language and name)
#     for voice in voices:
#         if 'Microsoft Zira Desktop - English (United States)' in voice.name:  # Check for female and English
#             engine.setProperty('voice', voice.id)
#             break


# #Adjust speaking rate (might indirectly affect perceived pitch)
#     if hasattr(engine, 'setProperty'):
#         engine.setProperty('rate', 125)
#     engine.say(text)
#     engine.runAndWait()
    
    
    
    
# def takecommand():
#     r=sr.Recognizer()
#     with sr.Microphone() as source:  #microphone is also a class we will use it as a source
#         r.pause_threshold= 0.6
#         audio=r.listen(source)
#         try:
#             print("recognizing.......")
#             query = r.recognize_google(audio, language="en-in")
#             #recogniser is the class which helps to recognise voice
#             print(f"user said :  {query}")
#             return query
#         except Exception as e:
#             return "some error ocurred sorry"
        
# def open_app(query):
#         apps=["WhatsApp","Spotify","Notepad","Word","PowerPoint","Excel","Photos","Discord" 
#               "Telegram Desktop","Prime Video","Chrome","Calculator","Settings","Camera"]
#         for i in apps:
#             if f"open {i}".lower() in query.lower():
#                 from AppOpener import open
#                 say(f"Opening{i}....")
#                 open(i)
                
                
                      
        
# if __name__ =='__main__':
#     print("HELLO I AM YOUR NEXUS")
#     print("HOW MAY I HELP YOU")
#     say("Hello I am your nexus, how may I help you")
#     while True:
#         print("listening......")
#         query=takecommand()

