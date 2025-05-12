# FILE: Automation.py FOR Python 3.10.6
# DESCRIPTION: This file contains a class with methods to operate inside ArXX Project.py.





class Auto:
    def type_spam(text, num_times):
        import pyautogui as pg
        import time
        pg.PAUSE = False
        for i in range(num_times):
            pg.write(text)
            pg.press('enter')
          
        
    def type_spamDirect(text, num_times):
        import pydirectinput as pg
        import time
        pg.PAUSE = False
        for i in range(num_times):
            pg.write(text)
            pg.press('enter')
            


