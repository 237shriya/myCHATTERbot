# import win32com.client package after installing pywin32 in cmd
# use inbuilt functions of the package
# take input from the user and store it in text
# pass text as argument in Speak function
# keep some text to exit the program here exit is used for this purpose

import win32com.client as wincom

print("  HELLO! and Welcome to MY CHATTER BOT")
speak = wincom.Dispatch("SAPI.SpVoice")
while True:
    text = input(" What do you want me to speak for you?")
    if text == " exit":
        break
    speak.Speak(text)
