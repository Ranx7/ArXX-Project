from tkinter import *
import pyautogui as pg
import time



import mysql.connector


mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="password",
    database="userdb",
)

mycursor = mydb.cursor()


def page1():
   

    def register():
        def back():
            frame.destroy()
            page1()
        label.destroy()
        user.destroy()
        registerButton.destroy()
        backButton = Button(frame, text="Back", command=back, bg="black", fg="lime", font=("Fixedsys", 10))
        backButton.pack(side=BOTTOM, fill=BOTH, expand=True)
        username = Entry(frame, width=20, font=("Fixedsys", 20), bg="black", fg="lime", insertbackground="lime", background="black", justify="center")
        username.pack(fill='both', expand=True)
        username.bind('<Return>', lambda event: on_register())
        def on_register():
            mycursor.execute("INSERT INTO users (username) VALUES (%s)", (username.get(),))
            mydb.commit()
            username.delete(0, END)
            username.insert(0, "Registered!")
            window.update()
            time.sleep(0.5)
            frame.destroy()
            page1()

    
        
    frame = Frame(window, width=500, height=500)
    frame.pack(side=TOP, fill=BOTH, expand=True)
    title = "ArXX"
    window.config(bg="black")

    label = Label(frame, text=title, fg="lime", bg="black", font=("Fixedsys", 20))
    user = Entry(frame, width=20, font=("Fixedsys", 20), bg="black", fg="lime", insertbackground="lime", background="black", justify="center")
    registerButton = Button(frame, text="Register", command=register, bg="black", fg="lime", font=("Fixedsys", 10))
    registerButton.pack(side=BOTTOM, fill=BOTH, expand=True)


    a = 0
    for t in title:
        window.update()
        a += 1
        label.config(text=(title[:a]) + "_")
        label.pack()
        window.update()
        time.sleep(0.2)
        label.config(text=(title[:a]))
    label.pack(fill='both', expand=True)
    user.pack(fill='both', expand=True)
    user.insert(0, "Enter username")
    user.focus_set()
    def on_click():
        try:
            mycursor.execute("SELECT username FROM users")
            myresult = [item[0] for item in mycursor.fetchall()]

           
            if user.get() in myresult:
                user.delete(0, END)
                user.insert(0, "Access Granted")
                window.update()
                time.sleep(0.5)
                frame.destroy()
            else:
                user.config(fg="red")
                window.update()
                time.sleep(0.3)
                user.delete(0, END)
                user.insert(0, "Access Denied")
                window.update()
                time.sleep(0.3)
                user.config(fg="lime")
                user.delete(0, END)
        except _tkinter.TclError as e:
            print(f"TclError caught: {e}")


    user.bind('<Return>', lambda event: on_click())
    


window = Tk()
window.config(bg="black")
page1()


window.mainloop()