from tkinter import*
import pyttsx3
from datetime import datetime
import pytz
import webbrowser
engine=pyttsx3.init()
engine.setProperty('volume',2.0)
engine.setProperty('rate',150)
def date_time():
    dt = datetime.now(pytz.timezone('Asia/karachi'))
    return dt.strftime("%d-%m-%Y %H : %M : %S")
def chatbot_response(user_message):
    if "date" in user_message.lower() or "time" in user_message.lower():
        return f"The current date and time is {date_time()}"
    elif "youtube" in user_message.lower():
        youtube_url="https://www.youtube.com"
        webbrowser.open(youtube_url)
        return f"open Youtube..."
    elif "google" in user_message.lower():
        google_url="https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwiJmM2V_MeKAxVAQPEDHSxUKu0QPAgI"
        webbrowser.open(google_url)
        return f"Opening Google........."
    response={
        "hi":"Hi how can i Assist you",
        "how are you":"I am find, but i am a rebot so i have no feelings",
        "goodbye":"BYe have a nice day",
        "what is your name":"My name is Novida",
        "who create you":"I am created by saad pasha who is a student of SSUET university",
        "default":"I don't understand what are you saying"
    }
    return response.get(user_message.lower(),response["default"])
def send_message():
    user_message=user_input.get()
    if not user_message.strip():
        return
    chatbox.insert(END,f"YOU: {user_message}\n")
    user_input.delete(0,END)

    bot_reply=chatbot_response(user_message)
    chatbox.insert(END,f"Chatbot: {bot_reply}\n")
    engine.say(bot_reply)
    engine.runAndWait()
def clear_message():
    chatbox.delete(1.0,END)
window=Tk()
window.geometry('560x560')
window.title("Novida")
icon=PhotoImage(file="Novida chatbot.png")
window.iconphoto(True,icon)
window.config(background="black")
button=Button(window,text="send",command=send_message,bg=("Red"),font=("Arial",14))
button.pack(side=BOTTOM)
button=Button(window,text="clear",command=clear_message,bg=("Blue"),font=("Arial",14))
button.pack(side=BOTTOM)
chatbox=Text(window,height=20,width=75,bg="black",fg="white")
chatbox.pack()
user_input=Entry(window)
user_input.pack()
window.mainloop()
