

from tkinter import *
import pyautogui as pg
import time
import sqlite3



conn = sqlite3.connect("userdb.sqlite")
cursor = conn.cursor()

def page1():
    window.focus_force()
    
    def register():
        def back():
            frame.destroy()
            page1()
        label.destroy()
        user.destroy()
        passw.destroy()
        registerButton.destroy()
        backButton = Button(frame, text="Back", command=back, bg="black", fg="lime", font=("Fixedsys", 10))
        backButton.pack(side=BOTTOM, fill=BOTH, expand=True)
        username = Entry(frame, width=20, font=("Fixedsys", 20), bg="black", fg="lime", insertbackground="lime", background="black", justify="center")
        password = Entry(frame, width=20, font=("Fixedsys", 20), bg="black", fg="lime", insertbackground="lime", background="black", justify="center")
        
        username.pack(fill='both', expand=True)
        password.pack(fill='both', expand=True)
        username.insert(0, "Enter new username")
        password.insert(0, "Enter new password")
        username.focus_set()
        window.update()
        time.sleep(0.5)
        username.delete(0, END)
        window.focus()
        
        username.bind('<Return>', lambda event: on_username())
        password.bind('<Return>', lambda event: on_register())

        def on_username():
            password.focus_set()
            window.update()
            time.sleep(0.5)
            password.delete(0, END)
        def on_register():
            cursor.execute("SELECT username FROM users")
            myresult_user = [item[0] for item in cursor.fetchall()]

            if username.get() in myresult_user:
                username.delete(0, END)
                username.insert(0, "Username already exists")
                window.update()
                time.sleep(0.5)
                username.delete(0, END)
                username.insert(0, "Enter new username")
                window.update()
                time.sleep(0.5)
            else:
                cursor.execute("INSERT INTO users (username, passwords) VALUES (?, ?)", (username.get(), password.get()))
                conn.commit()
                username.delete(0, END)
                username.insert(0, "Registered!")
                window.update()
                time.sleep(0.5)
                frame.destroy()
                page1()
    
    frame = Frame(window, width=500, height=500, bg="black")
    frame.pack(side=TOP, fill=BOTH, expand=True)
    title = "ArXX"
    window.config(bg="black")

    label = Label(frame, text=title, fg="lime", bg="black", font=("Fixedsys", 20))
    user = Entry(frame, width=20, font=("Fixedsys", 20), bg="black", fg="lime", insertbackground="lime", background="black", justify="center")
    passw = Entry(frame, width=20, font=("Fixedsys", 20), bg="black", fg="lime", insertbackground="lime", background="black", justify="center") 
    registerButton = Button(frame, text="Register", command=register, bg="black", fg="lime", font=("Fixedsys", 10))
    registerButton.pack(side=BOTTOM, fill=BOTH, expand=True)

    a = 0
    for t in title:
        window.update()
        a += 1
        label.config(text=(title[:a]) + "_")
        label.pack()
        window.update()
        time.sleep(0.1)
        label.config(text=(title[:a]))
    
    label.pack(fill='both', expand=True)
    user.pack(fill='both', expand=True)
    passw.pack(fill='both', expand=True)
    user.insert(0, "Enter username")
    window.update()
    time.sleep(0.5)
    user.delete(0, END)
    passw.insert(0, "Enter password")
    window.eval('tk::PlaceWindow . center')
    user.focus_set()
    

    def on_user():
        passw.focus_set()
        window.update()
        time.sleep(0.5)
        passw.delete(0, END)

    def on_click():
        try:
            cursor.execute("SELECT username FROM users")
            myresult_user = [item[0] for item in cursor.fetchall()]
            cursor.execute("SELECT passwords FROM users")
            myresult_pass = [item[0] for item in cursor.fetchall()]
            if user.get() in myresult_user and passw.get() in myresult_pass:
                user.delete(0, END)
                passw.delete(0, END)
                user.insert(0, "Access Granted")
                window.update()
                time.sleep(0.5)
                frame.destroy()
                page2()
            else:
                user.config(fg="red")
                passw.config(fg="red")
                window.update()
                time.sleep(0.3)
                user.delete(0, END)
                user.insert(0, "Access Denied")
                window.update()
                time.sleep(0.3)
                user.config(fg="lime")
                user.delete(0, END)
                passw.delete(0, END)
                passw.config(fg="lime")
                user.focus_set()
        except TclError as e:
            print(f"TclError caught: {e}")

    user.bind('<Return>', lambda event: on_user())
    passw.bind('<Return>', lambda event: on_click())





def page2():
    def back():
        frame.destroy()
        page1()
    window.config(bg="black")
    window.update()

    frame = Frame(window, width=500, height=500, bg="black")
    frame.pack(side=TOP, fill=BOTH, expand=True)

    title = "ArXX"
    title2 = "Automation"

    title_label = Label(frame, text=title, fg="lime", bg="black", font=("Fixedsys", 20))
    title_label.pack(fill='both', expand=True, side=TOP)
    Automation_tab = Label(frame, text="Automation", fg="lime", bg="black", font=("Fixedsys", 20, 'bold', 'underline'))
    Automation_tab.pack(fill='both', expand=True, side=TOP, pady=10)
    backButton = Button(frame, text="Back", command=back, bg="black", fg="lime", font=("Fixedsys", 10))
    backButton.pack(side=BOTTOM, fill=BOTH, expand=True)


    a = 0
    max_length = max(len(title), len(title2))


    for a in range(1, max_length + 1):
        window.update()
        a += 1
        title_label.config(text=(title[:a]) + "_")
        title_label.pack()

        Automation_tab.config(text=(title2[:a]) + "_")
        Automation_tab.pack()

        

        window.update()
        time.sleep(0.1)
        title_label.config(text=(title[:a]))
        title_label.pack(fill='both', expand=True)

        Automation_tab.config(text=(title2[:a]))
        Automation_tab.pack(fill='both', expand=True)

        backButton.pack(side=BOTTOM, fill=BOTH, expand=True)
    def on_Automation():
        def back():
            frame.destroy()
            page2()
        for widget in window.winfo_children():
            widget.destroy()
        

        window.update()
        frame = Frame(window, width=500, height=500, bg="black")
        frame.pack(side=TOP, fill=BOTH, expand=True)
        title = "Automation Tab"
        title2 = "Type Spam"
        title_label = Label(frame, text=title, fg="lime", bg="black", font=("Fixedsys", 20))
        title_label.pack(fill='both', expand=True, side=TOP)

        typeSpam = Label(frame, text=title2, fg="lime", bg="black", font=("Fixedsys", 20, 'bold', 'underline'))
        typeSpam.pack(fill='both', expand=True, side=TOP, pady=10)

        backButton = Button(frame, text="Back", command=back, bg="black", fg="lime", font=("Fixedsys", 10))
        backButton.pack(side=BOTTOM, fill=BOTH, expand=True)



        a = 0
        max_length = max(len(title), len(title2))


        for a in range(1, max_length + 1):
            window.update()
            a += 1
            title_label.config(text=(title[:a]) + "_")
            title_label.pack()

            typeSpam.config(text=(title2[:a]) + "_")
            typeSpam.pack()

            window.update()
            time.sleep(0.1)
            title_label.config(text=(title[:a]))
            title_label.pack(fill='both', expand=True) 
            typeSpam.config(text=(title2[:a]))
            typeSpam.pack(fill='both', expand=True)


            def onTypeSpam():
                def back():
                    frame.destroy()
                    page2()

                for widget in window.winfo_children():
                    widget.destroy()
                window.update()

                frame = Frame(window, width=500, height=500, bg="black")
                frame.pack(side=TOP, fill=BOTH, expand=True)
                title = "Type Spam"
                title2 = "Ingame setting"
                title3 = "Start"

                title_label = Label(frame, text=title, fg="lime", bg="black", font=("Fixedsys", 20))
                title_label.pack(fill='both', expand=True, side=TOP)

                title_setting = Label(frame, text=title2, fg="lime", bg="black", font=("Fixedsys", 20, 'bold', 'underline'))
                title_setting.pack(fill='both', expand=True, side=TOP)

                title_start = Label(frame, text=title3, fg="lime", bg="black", font=("Fixedsys", 20, 'bold', 'underline'))
                title_start.pack(fill='both', expand=True, side=TOP, pady=10)

                num_input = Entry(frame, width=20, font=("Fixedsys", 20), bg="black", fg="lime", insertbackground="lime", background="black", justify="center")
                num_input.pack(fill='both', expand=True, pady=20)

                instruction = Label(frame, text="Enter the number of times to spam", fg="lime", bg="black", font=("Fixedsys", 10))
                instruction.pack(fill='both', expand=True, side=TOP)
                
                text_input = Entry(frame, width=20, font=("Fixedsys", 20), bg="black", fg="lime", insertbackground="lime", background="black", justify="center")
                text_input.pack(fill='both', expand=True, pady=20)

                instruction2 = Label(frame, text="Enter the text to spam", fg="lime", bg="black", font=("Fixedsys", 10))
                instruction2.pack(fill='both', expand=True, side=TOP)

                backButton = Button(frame, text="Back", command=back, bg="black", fg="lime", font=("Fixedsys", 10))
                backButton.pack(side=BOTTOM, fill=BOTH, expand=True)

                

                count = 0

                counter = Label(frame, text=count, fg="lime", bg="black", font=("Fixedsys", 10))


                a = 0
                max_length = max(len(title), len(title2), len(title3))

                for a in range(1, max_length + 1):
                    window.update()
                    a += 1
                    title_label.config(text=(title[:a]) + "_")
                    title_label.pack()

                    title_setting.config(text=(title2[:a]) + "_")
                    title_setting.pack()

                    title_start.config(text=(title3[:a]) + "_")
                    title_start.pack()

                    window.update()
                    time.sleep(0.1)
                    title_label.config(text=(title[:a]))
                    title_label.pack(fill='both', expand=True)

                    title_setting.config(text=(title2[:a]))
                    title_setting.pack(fill='both', expand=True)

                    title_start.config(text=(title3[:a]))
                    title_start.pack(fill='both', expand=True)
                num_input.focus_set()
                def onStart():
                    nonlocal count, pydirect
                    counter.pack(fill='both', expand=True, side=TOP)
                    window.update()
                    for i in range(1, 5):
                        time.sleep(1)
                        count += 1
                        counter.config(text=count)
                        window.update()
                    count = 0
                    counter.pack_forget()
                    window.update()
                    try:
                        num = int(num_input.get())
                        print("Number of times to spam:", num)
                        from Automation import Auto
                        sp_text = text_input.get()

                        if pydirect:
                            
                            Auto.type_spamDirect(sp_text, num)
                        else:
                            Auto.type_spam(sp_text, num)
                    except ValueError:
                        num_input.delete(0, END)
                        num_input.insert(0, "Invalid input!")
                        window.update()
                        time.sleep(0.5)
                        num_input.delete(0, END)
                        window.update()
                        time.sleep(0.5)
                        num_input.focus_set()

                title_start.bind('<Button-1>', lambda event: onStart())
       
              
                pydirect = False
                def onSetting():
                    nonlocal pydirect  
                    pydirect = not pydirect
                    if pydirect:
                        title_setting.config(fg="lime")
                    else:
                        title_setting.config(fg="white")
                    print("pydirect:", pydirect)





                title_setting.bind('<Button-1>', lambda event: onSetting())




            typeSpam.bind('<Button-1>', lambda event: onTypeSpam())
    
        

    Automation_tab.bind('<Button-1>', lambda event: on_Automation())
    
    
    

   



window = Tk()
window.config(bg="black")
window.update()

window.eval('tk::PlaceWindow . center')

page1()

window.call('wm', 'attributes', '.', '-topmost', '1')
window.mainloop()
