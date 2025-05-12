

from tkinter import *
import pyautogui as pg
import time
import sqlite3
import sys
import os

import shutil

from Record import start_record
from Replay import start_play


def get_database_path():
    try:
    
        base_path = sys._MEIPASS
    except AttributeError:
    
        return "userdb.sqlite"


    writable_db_path = os.path.join(os.getcwd(), "userdb.sqlite")
    if not os.path.exists(writable_db_path):
        bundled_db_path = os.path.join(base_path, "userdb.sqlite")
        shutil.copy2(bundled_db_path, writable_db_path)
        
    return writable_db_path

db_path = get_database_path()
print(db_path)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    username CHAR(20) PRIMARY KEY,
    passwords CHAR(20) NOT NULL
)
''')

def addHover(label, fg_normal, fg_hover):
        label.fg_normal = fg_normal
        label.fg_hover = fg_hover

        label.bind('<Enter>', lambda e: label.config(fg=fg_hover))
        label.bind('<Leave>', lambda e: label.config(fg=fg_normal))
def center_window(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    win.geometry(f"{width}x{height}+{x}+{y}")

def safe_config(widget, **kwargs):
    try:
        widget.config(**kwargs)
    except TclError:
        pass



def page1():
    Tab()
    try:

        window.focus_force()
        
        
        def register():
            def back():
                if frame.winfo_exists():
                    frame.destroy()
                    page1()
            label.destroy()
            user.destroy()
            passw.destroy()
            registerButton.destroy()
            Tab()
            backButton = Button(frame, text="Back", command=back, bg="black", fg="lime", font=("Fixedsys", 10))
            backButton.pack(side=BOTTOM, fill=BOTH, expand=True)
            username = Entry(frame, width=20, font=("Fixedsys", 20), bg="black", fg="lime", insertbackground="lime", background="black", justify="center")
            password = Entry(frame, width=20, font=("Fixedsys", 20), bg="black", fg="lime", insertbackground="lime", background="black", justify="center")
            
            username.pack(expand=True, padx=10, pady=10)
            password.pack(expand=True, padx=10, pady=100)
            
            username.insert(0, "Enter new username")
            password.insert(0, "Enter new password")
            
            window.update()
            time.sleep(0.5)
            username.delete(0, END)
            
            window.focus()
            username.focus_set()

            
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
        frame.pack(side=TOP, expand=True, padx=10, pady=10)
        title = "ArXX"
        window.config(bg="black")

        label = Label(frame, text=title, fg="lime", bg="black", font=("Fixedsys", 20))
        user = Entry(frame, width=20, font=("Fixedsys", 20), bg="black", fg="lime", insertbackground="lime", background="black", justify="center")
        passw = Entry(frame, width=20, font=("Fixedsys", 20), bg="black", fg="lime", insertbackground="lime", background="black", justify="center") 
        registerButton = Button(frame, text="Register", command=register, bg="black", fg="lime", font=("Fixedsys", 10))
        registerButton.pack(side=BOTTOM, fill=BOTH, expand=True, pady=50)

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
        user.pack(fill='both', pady=5, padx=10, ipadx=30)
        passw.pack(fill='both', pady=10, padx=10, ipadx=30)
        user.insert(0, "Enter username")
        window.update()
        time.sleep(0.5)
        user.delete(0, END)
        passw.insert(0, "Enter password")
        center_window(window)
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
                    global userName
                    userName = user.get()
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
    except TclError:
        pass





def page2():
    
    try:

        print(userName)
        def back():
            frame.destroy()
            page1()
        window.wm_attributes("-transparentcolor", "lightblue")
        window.update()
        Tab()

        frame = Frame(window, width=500, height=500, bg="black")
        frame.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        title = "ArXX"
        title2 = "Automation"
        title3 = "Profile"

        title_label = Label(frame, text=title, fg="lime", bg="black", font=("Fixedsys", 20))
        title_label.pack(fill='both', expand=True, side=TOP, anchor='center',pady=100)
        profile_tab = Label(frame, text=title3, fg="lime", bg="black", font=("Fixedsys", 20, 'bold', 'underline'))
        profile_tab.pack(fill='both', expand=True, side=TOP, pady=10)
        Automation_tab = Label(frame, text="Automation", fg="lime", bg="black", font=("Fixedsys", 20, 'bold', 'underline'))
        Automation_tab.pack(fill='both', expand=True, side=TOP, pady=10)
        backButton = Button(frame, text="Back", command=back, bg="black", fg="lime", font=("Fixedsys", 20), state="disabled")
        backButton.pack(side=BOTTOM, expand=True, pady=50, ipadx=100)



        a = 0
        max_length = max(len(title), len(title2), len(title3))


        for a in range(1, max_length + 1):
            window.update()
            a += 1
            safe_config(title_label, text=(title[:a]) + "_")
            title_label.pack()

            
            safe_config(profile_tab, text=(title3[:a]) + "_")
            profile_tab.pack()

           
            safe_config(Automation_tab, text=(title2[:a]) + "_")
            Automation_tab.pack()

            

            window.update()
            time.sleep(0.1)
            title_label.config(text=(title[:a]))
            title_label.pack(fill='both', expand=True)

            profile_tab.config(text=(title3[:a]))
            profile_tab.pack(fill='both', expand=True)

            Automation_tab.config(text=(title2[:a]))
            Automation_tab.pack(fill='both', expand=True)

            backButton.pack(side=BOTTOM, expand=True)
        backButton.config(state="normal")
        
        window.update()
        def on_Automation():
            
            def back():
                if frame.winfo_exists():
                    frame.pack_forget()
                    page2()
                
            for widget in window.winfo_children():
                widget.pack_forget()

            Tab()
            

            window.update()
            frame = Frame(window, width=500, height=500, bg="black")
            frame.pack(side=TOP, fill=BOTH, ipady=100)
            title = "Automation Tab"
            title2 = "Type Spam"
            title3 = "Record and Play"
            title_label = Label(frame, text=title, fg="lime", bg="black", font=("Fixedsys", 20))
            title_label.pack(fill='both', side=TOP, pady=50)

            typeSpam = Label(frame, text=title2, fg="lime", bg="black", font=("Fixedsys", 20, 'bold', 'underline'))
            typeSpam.pack(fill='both',side=TOP, pady=10)

            RePlay = Label(frame, text=title3, fg="lime", bg="black", font=("Fixedsys", 20, 'bold', 'underline'))
            RePlay.pack(fill='both', side=TOP, pady=10)
            

            backButton = Button(frame, text="Back", command=back, bg="black", fg="lime", font=("Fixedsys", 10), state="disabled")
            backButton.pack(side=BOTTOM, ipadx=100, anchor=CENTER)



            a = 0
            max_length = max(len(title), len(title2), len(title3))



            for a in range(1, max_length + 1):
                window.update()
                a += 1
                title_label.config(text=(title[:a]) + "_")
                title_label.pack()

                typeSpam.config(text=(title2[:a]) + "_")
                typeSpam.pack()

                RePlay.config(text=(title3[:a]) + "_")
                RePlay.pack()


                window.update()
                time.sleep(0.1)
                title_label.config(text=(title[:a]))
                title_label.pack(fill='both', expand=True) 
                typeSpam.config(text=(title2[:a]))
                typeSpam.pack(fill='both', expand=True)
                RePlay.config(text=(title3[:a]))
                RePlay.pack(fill='both', expand=True)
            backButton.config(state="normal")
            


            def onTypeSpam():
                
                def back():
                    if frame.winfo_exists():
                        frame.pack_forget()
                        page2()

                for widget in window.winfo_children():
                    widget.pack_forget()
                window.update()
                Tab()

                frame = Frame(window, width=500, height=500, bg="black")
                frame.pack(side=TOP, fill=BOTH, ipady=50)
                title = "Type Spam"
                title2 = "Ingame setting"
                title3 = "Start"

                title_label = Label(frame, text=title, fg="lime", bg="black", font=("Fixedsys", 20))
                title_label.pack(fill='both', side=TOP, pady=50)

                title_setting = Label(frame, text=title2, fg="white", bg="black", font=("Fixedsys", 20, 'bold', 'underline'))
                title_setting.pack(fill='both', expand=True, side=TOP)
                addHover(title_setting, "white", "gray")

                title_start = Label(frame, text=title3, fg="lime", bg="black", font=("Fixedsys", 20, 'bold', 'underline'))
                title_start.pack(fill='both', expand=True, side=TOP, pady=10)

                num_input = Entry(frame, width=20, font=("Fixedsys", 20), bg="black", fg="lime", insertbackground="lime", background="black", justify="center")
                num_input.pack(fill='both', expand=True, pady=20)

                instruction = Label(frame, text="Enter the number of times to spam", fg="lime", bg="black", font=("Fixedsys", 10))
                instruction.pack(fill='both', expand=True, side=TOP)
                
                text_input = Entry(frame, width=20, font=("Fixedsys", 20), bg="black", fg="lime", insertbackground="lime", background="black", justify="center")
                text_input.pack(fill='both', expand=True)

                instruction2 = Label(frame, text="Enter the text to spam", fg="lime", bg="black", font=("Fixedsys", 10))
                instruction2.pack(fill='both', expand=True, side=TOP)

                
                backButton = Button(frame, text="Back", command=back,
                                    bg="black", fg="lime", font=("Fixedsys",20))
                backButton.pack()
                backButton.config(state="disabled")

                

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

                    
                backButton.config(state="normal")
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
                addHover(title_start, "lime", "green")
                    
        
                
                pydirect = False
                def onSetting():
                    nonlocal pydirect  
                    pydirect = not pydirect
                    if pydirect:
                        title_setting.config(fg="lime")
                        addHover(title_setting, "lime", "green")
                    else:
                        title_setting.config(fg="white")
                        addHover(title_setting, "white", "gray")
                    print("pydirect:", pydirect)
                title_setting.bind('<Button-1>', lambda event: onSetting())
                    


            def onReplay():
                window.geometry("550x500")
                def back():
                    if frame.winfo_exists():
                        frame.pack_forget()
                        page2()
                    
                for widget in window.winfo_children():
                    widget.pack_forget()
                window.update()
                Tab()

                frame = Frame(window, width=500, height=500, bg="black")
                frame.pack(side=TOP, fill=BOTH, ipadx=50)
                title = "Record and Play"
                title2 = "Record"
                title3 = "Play"
                title4 = "To stop recording, place cursor to top-left corner of your screen"
                title_label = Label(frame, text=title, fg="lime", bg="black", font=("Fixedsys", 20))
                title_label.pack(fill='both', side=TOP)
                RecordLabel = Label(frame, text=title2, fg="lime", bg="black", font=("Fixedsys", 20, 'bold', 'underline'))
                RecordLabel.pack(fill='both', side=TOP, pady=15)
                PlayLabel = Label(frame, text=title3, fg="lime", bg="black", font=("Fixedsys", 20, 'bold', 'underline'))
                PlayLabel.pack(fill='both', side=TOP, pady=50)

                RecordInstruction = Label(frame, text=title4, fg="lime", bg="black", font=("Fixedsys", 10))
                RecordInstruction.pack(fill='both', expand=True, side=TOP, pady=20)

                backButton = Button(frame, text="Back", command=back, bg="black", fg="lime", font=("Fixedsys", 20), state="disabled")
                backButton.pack(side=BOTTOM, ipadx=100, anchor="center",pady=50)

                count = 0
                counter = Label(frame, text=count, fg="lime", bg="black", font=("Fixedsys", 10))

                a = 0
                max_length = max(len(title), len(title2), len(title3), len(title4))

                for a in range(1, max_length + 1):
                    window.update()
                    a += 1
                    title_label.config(text=(title[:a]) + "_")
                    title_label.pack()

                    RecordLabel.config(text=(title2[:a]) + "_")
                    RecordLabel.pack()

                    PlayLabel.config(text=(title3[:a]) + "_")
                    PlayLabel.pack()

                    RecordInstruction.config(text=(title4[:a]) + "_")
                    RecordInstruction.pack()


                    window.update()
                    time.sleep(0.1)
                    title_label.config(text=(title[:a]))
                    title_label.pack(fill='both', expand=True) 
                    RecordLabel.config(text=(title2[:a]))
                    RecordLabel.pack(fill='both', expand=True)
                    PlayLabel.config(text=(title3[:a]))
                    PlayLabel.pack(fill='both', expand=True)
                    RecordInstruction.config(text=(title4[:a]))
                    RecordInstruction.pack(fill='both', expand=True)

                    

                backButton.config(state="normal")
                

                import threading

                def onRecord():
                    def run():
                        nonlocal count
                        counter.pack(fill='both', expand=True, side=TOP)
                        window.update()
                        for i in range(1, 5):
                            time.sleep(0.2)
                            count += 1
                            counter.config(text=count)
                            window.update()
                        count = 0
                        counter.pack_forget()
                        RecordLabel.config(fg="gray")
                        window.update()
                        print("Recording...")




                        top = Toplevel()
                        top.overrideredirect(True)  
                        top.wm_attributes("-topmost", True)  
                        top.wm_attributes("-transparentcolor", "pink") 

                        top.configure(bg="pink") 

                        
                        label = Label(top, text="Recording", font=("Arial", 24), bg="pink", fg="Lime")
                        label.pack(padx=20, pady=20)

                        top.geometry("+50+600") 

                     



                        RecordLabel.unbind('<Button-1>')
                        backButton.config(state="disabled")
                        window.overrideredirect(False)
                        window.iconify()
                        time.sleep(0.5)
                        start_record()
                        time.sleep(2)
                        window.overrideredirect(True)
                        window.deiconify()
                        PlayLabel.bind('<Button-1>', lambda event: onPlay())
                        window.update()
                        RecordLabel.config(fg="lime")
                        RecordLabel.bind('<Button-1>', lambda event: onRecord())
                        backButton.config(state="normal")

                        top.destroy()
                        
                    

                    threading.Thread(target=run).start()


                def onPlay():
                    def run():
                        nonlocal count
                        count = 0
                        counter.pack(fill='both', expand=True, side=TOP)
                        window.update()
                        for i in range(1, 5):
                            time.sleep(1)
                            count += 1
                            counter.config(text=count)
                            window.update()
                        count = 0
                        counter.pack_forget()

                        top = Toplevel()
                        top.overrideredirect(True)  
                        top.wm_attributes("-topmost", True)  
                        top.wm_attributes("-transparentcolor", "pink") 

                        top.configure(bg="pink") 

                        
                        label = Label(top, text="Replaying", font=("Arial", 24), bg="pink", fg="Lime")
                        label.pack(padx=20, pady=20)

                        top.geometry("+50+600")

                        PlayLabel.config(fg="lime")
                        addHover(PlayLabel, "lime", "green")
                        print("Playing...")
                        PlayLabel.unbind('<Button-1>')
                        backButton.config(state="disabled")
                        RecordLabel.unbind('<Button-1>')
                        window.overrideredirect(False)
                        window.iconify()
                        start_play()

                        backButton.config(state="normal")
                        window.overrideredirect(True)
                        window.deiconify()
                        PlayLabel.bind('<Button-1>', lambda event: onPlay())
                        RecordLabel.bind('<Button-1>', lambda event: onRecord())
                        top.destroy()
                    threading.Thread(target=run).start()



                RecordLabel.bind('<Button-1>', lambda event: onRecord())
                    





                    


            addHover(typeSpam, "lime", "green")
            addHover(RePlay, "lime", "green")

            typeSpam.bind('<Button-1>', lambda event: onTypeSpam())
            RePlay.bind('<Button-1>', lambda event: onReplay())

        
        def onProfile():
            
            def back():
                if frame.winfo_exists():
                    frame.pack_forget()
                    page2()

            for widget in window.winfo_children():
                widget.pack_forget()
            Tab()
            

            window.update()
            frame = Frame(window, width=500, height=500, bg="black")
            frame.pack(side=TOP, fill=BOTH)
            title = "Profile Tab"
            title2 = ("Username: " + userName)
            title_label = Label(frame, text=title, fg="lime", bg="black", font=("Fixedsys", 20))
            title_label.pack(expand=True, ipadx=200, anchor='center', pady=100)

            userNameLabel = Label(frame, text=title2, fg="lime", bg="black", font=("Fixedsys", 20, 'bold', 'underline'))
            userNameLabel.pack(expand=True, ipadx=200, anchor='center', pady=50)

            backButton = Button(frame, text="Back", command=back, bg="black", fg="lime", font=("Fixedsys", 20), state="disabled")
            backButton.pack(side=TOP, pady=5, expand=True,ipadx=100, anchor='center')

            max_length = max(len(title), len(title2))


            for a in range(1, max_length + 1):
                window.update()
                a += 1
                title_label.config(text=(title[:a]) + "_")
                title_label.pack()

                userNameLabel.config(text=(title2[:a]) + "_")
                userNameLabel.pack()

                window.update()
                time.sleep(0.1)
                title_label.config(text=(title[:a]))
                title_label.pack(fill='both', expand=True) 
                userNameLabel.config(text=(title2[:a]))
                userNameLabel.pack(fill='both', expand=True)
            backButton.config(state="normal")

        addHover(Automation_tab, "lime", "green")
        addHover(profile_tab, "lime", "green")
        
                   


        Automation_tab.bind('<Button-1>', lambda event: on_Automation())
        profile_tab.bind('<Button-1>', lambda event: onProfile())
    except TclError:
        pass
        
def start_move(event):
    window.x = event.x
    window.y = event.y

def do_move(event):
    deltax = event.x - window.x
    deltay = event.y - window.y
    x = window.winfo_x() + deltax
    y = window.winfo_y() + deltay
    window.geometry(f"+{x}+{y}")

    
def Tab():
    min.pack(side=RIGHT, padx=10, pady=10)
    tab.pack(side=TOP, fill=BOTH, padx=10, pady=10)



from PIL import Image, ImageTk

window = Tk()

tab = Frame(window, width=500, height=20, bg="gray")
tab.pack(side=TOP, fill=BOTH, padx=10, pady=10)
min = Button(tab, text="X", command=window.destroy, bg="black", fg="red", font=("Fixedsys", 10, 'bold'))
min.pack(side=RIGHT, padx=10, pady=10)

window.bind("<Button-1>", start_move)
window.bind("<B1-Motion>", do_move)

window.overrideredirect(True)
window.minsize(500, 600)

window.wait_visibility()

window.wm_attributes("-alpha", 0.9)
window.update()

center_window(window)

page1()

window.call('wm', 'attributes', '.', '-topmost', '1')
window.mainloop()

