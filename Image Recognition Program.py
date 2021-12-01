from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#X:RGB: (255, 255, 255)
#Text Box Point(x=478, y=349)
#Submit Q1 Point(x=1425, y=341)
#Finish point Point(x=1414, y=411)
#Point(x=1347, y=530) Restart 1 
#Point(x=948, y=363) Restart 2
#Point(x=826, y=250) Restart 3

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

    

while keyboard.is_pressed('q') == False:
    
    if pyautogui.locateOnScreen('question1.png', confidence=0.6 ) != None:
        print("I can see question 1")

        click(528,282)
        time.sleep(0.05)
        
        pyautogui.press("P")
        pyautogui.press("r")
        pyautogui.press("o")
        pyautogui.press("c")
        pyautogui.press("e")
        pyautogui.press("s")
        pyautogui.press("s")
        pyautogui.press("e")
        pyautogui.press("s")

        click(1426,273)
        
        time.sleep(1.0)
        
        click(1416,367)

        print("Waiting for next question ...")
        
        time.sleep(1.5)


        
    elif pyautogui.locateOnScreen('question2.png', confidence=0.6 ) != None:
        print("I can see question 2")

        click(528,282)
        time.sleep(0.05)

        pyautogui.press("T")
        pyautogui.press("h")
        pyautogui.press("e")
        pyautogui.press(" ")
        pyautogui.press("p")
        pyautogui.press("u")
        pyautogui.press("r")
        pyautogui.press("p")
        pyautogui.press("o")
        pyautogui.press("s")
        pyautogui.press("e")

        click(1426,273)
        
        time.sleep(1.0)
        
        click(1416,367)

        print("Waiting for next question ...")
        
        time.sleep(1.5)



    elif pyautogui.locateOnScreen('restart1.png', confidence=0.6 ) != None:
        print("R - Finished")

        time.sleep(1.3)
        click(465,656)
        time.sleep(0.2)



    elif pyautogui.locateOnScreen('restart2.png', confidence=0.6 ) != None:
        print("R - Assess Page")

        time.sleep(0.5)
        click(1349,458)
        
    elif pyautogui.locateOnScreen('restart-2.png', confidence=0.6 ) != None:
        print("R - Topic Page")
        
        time.sleep(1.0)
        click(953,293)

    elif pyautogui.locateOnScreen('restart-3.png', confidence=0.6 ) != None:
        print("R - Question Page")
        
        time.sleep(1.0)
        click(832,178)
        

   
 
    
    else:
        print("Error no valid task to be exacuted")
        
        
        
