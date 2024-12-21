from tkinter import*
import pyttsx3
engine=pyttsx3.init()
engine.setProperty('volume',2.0)
engine.setProperty('rate',150)
def chatbot_response(user_message):
    response={
        "hi":"Hi how can i Assist you",
        "how are you":"I am find, and please don't ask me this stupid questions",
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
    chatbox.delete(1.2,END)
window=Tk()
window.geometry('560x560')
window.title("Novida")
icon=PhotoImage(file="Novida chatbot.PNG")
window.iconphoto(True,icon)
window.config(background="black")
button=Button(window,text="send",command=send_message,font=("white"))
button.pack(side=BOTTOM)
button=Button(window,text="clear",command=clear_message,font=("white"))
button.pack(side=BOTTOM)
chatbox=Text(window,height=20,width=50,bg="black",fg="white")
chatbox.pack()
user_input=Entry(window)
user_input.pack()
window.mainloop()

