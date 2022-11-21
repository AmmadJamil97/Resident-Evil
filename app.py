from flask import Flask, session, render_template, request, redirect
from tkinter import *
from tkinter import messagebox


app = Flask(__name__)

@app.route("/")
def route():
    return render_template("test4.html")




# Create an instance of tkinter frame or window
win = Tk()

# Set the size of the tkinter window
win.geometry("700x350")


@app.route("/register", methods=["GET", "POST"])
def register():

    session.clear()

    # if method of requesting from the HTML page is POST
    if request.method == "POST":

        # Ensure user submit a username
        if not request.form.get("username"):
            messagebox.showerror("nousername", "Please insert username")

# Create a label widget
label = Label(win, text="Click the button to show the message ",
font=('Calibri 15 bold'))
label.pack(pady=20)

# Create a button to delete the button
b = Button(win, text="Click Me", command=on_click)
b.pack(pady=20)

win.mainloop()
