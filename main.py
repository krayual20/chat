import tkinter as tk


window = tk.Tk()
window.geometry("400x900")
window.title("Chat")

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
)
button1.grid(row=0, column=1)
window.mainloop()

