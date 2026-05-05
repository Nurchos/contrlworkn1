from tkinter import *

history = []

try:
    file = open("history.txt", "r", encoding="utf-8")
    history = file.read().splitlines()
    file.close()
except:
    history = []


def greet():
    name = entry.get()

    if name == "":
        returnls

    text = "Привет, " + name
    history.append(text)

    
    while len(history) > 5:
        history.pop(0)


    file = open("history.txt", "w", encoding="utf-8")
    file.write("\n".join(history))
    file.close()

    update_text()


def update_text():
    text_box.delete("1.0", END)
    for item in history:
        text_box.insert(END, item + "\n")


root = Tk()

entry = Entry(root)
entry.pack()

button = Button(root, text="Привет", command=greet)
button.pack()

text_box = Text(root)
text_box.pack()

update_text()

root.mainloop()