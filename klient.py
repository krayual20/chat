import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 2205

s.connect((host, port))
msg = s.recv(1024)
print(msg.decode('ascii'))
s.close()

import tkinter as tk


window = tk.Tk()
window.geometry("400x900")
window.title("Chat")

def send():
    print("dsfdg")
def text():
    user_input = entry1.get()
    entry1.delete(0, tk.END)
    mess = user_input
    print(mess)

label1 = tk.Label(
    text='mess',
    background="black",
    foreground="white"
)
label1.grid(row=1)
entry1 = tk.Entry(
    width=35,
    fg="white",
    bg="black"
)
entry1.grid(row=0, column=0)

button1 = tk.Button(
    text="Send!",
    bg="green",
    fg="black",
    width=5,
    height=1,
    command=text
)
button1.grid(row=0, column=1)
window.mainloop()