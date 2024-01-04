import tkinter
def send_message():
    message = entry.get()
    label.config(text=message)
window = tkinter.Tk()
entry = tkinter.Entry(window)
entry.pack()
button = tkinter.Button(window, text="发送", command=send_message)
button.pack()
label = tkinter.Label(window, text="")
label.pack()
