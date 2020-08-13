# Import Libraries
import requests
from tkinter import *
from bs4 import BeautifulSoup
from csv import writer

# Version
version = "1.0"

# Create root window for TKinter
root = Tk()

# Window Title
root.title('RAEScrapper')
photo = PhotoImage(file = "icons\icon.png")
root.iconphoto(False, photo)

# About button function
def about():
   window = Toplevel(root)
   window.iconphoto(False, photo)
   aboutButton = Button(window, text="Created by Pedro Ignacio Alcala Durand \n" + version)
   aboutButton.pack()

# Top menu
menuBar = Menu(root)
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="About", command=about)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=root.quit)
menuBar.add_cascade(label="Help", menu=fileMenu)

# User input label
userInput = Entry(root, width=50, borderwidth=5)
userInput.pack()

# Scrollbar widget
myScrollbar = Scrollbar(root, orient=VERTICAL)
myScrollbar.pack(side=RIGHT, fill=Y)

# Textbot widget
textBox = Text(root, width=100)
textBox.pack()

# Search button  function.
def searchF():
    textBox.delete('1.0', END)
    word = userInput.get()
    word = word.lower()

    response = requests.get('https://dle.rae.es/' + word + '/')

    soup = BeautifulSoup(response.text, 'html.parser')

    posts = soup.find_all(True, {"class":["j", "j1", "j2", "j3", "j4", "j5", "j6", "k2","k3","k4","k5", "k6", "m", "l2", "f"]})

    textContent = ""

    if not posts:
      errorMsg = "The word " + word + " is not in the dictionary."
      textBox.insert(END, errorMsg)
    else:
        textContent += word
        textContent += "\n"
        for post in posts:
            checkIfWordFound = post.get_text().find(word)
            checkIfWordStartsNumber = str(post.get_text())
            if not (checkIfWordStartsNumber[0].isdigit()):
                textContent += "\n"

            if (checkIfWordFound != -1):
                if not (checkIfWordStartsNumber[0].isdigit()):
                    textContent += "\n"

            line = post.get_text()

            textContent += line
            textContent += "\n"


    textBox.insert(END, textContent)

# Attach textbox and scrollbar
textBox.config(yscrollcommand=myScrollbar.set)
myScrollbar.config(command=textBox.yview)

# Set the search button functionality
myButton = Button(root, text="Search", command=searchF)
myButton.pack()

# Root Loop
root.config(menu=menuBar)
root.mainloop()
