import time
import pyautogui
import os
import sys
# from pynput.keyboard import Key, Listener

print("Welcome to the  M E S S A G E  S P A M M E R")
print("Developed by Matthew Trent (matthewtrent.me)")
print("\n")


def SpamTime(message, spams, delay):
    time.sleep(5)
    for x in range(spams):
        pyautogui.typewrite(message)
        pyautogui.press('enter')
        time.sleep(delay)
    print("Spam complete!")
    os.execv(sys.executable, ['python'] + sys.argv)


def clearConsole(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')


def userInfo():
    try:
        while True:
            print("IMPORTANT: click back into the terminal and press \"CTRL + C\" to cancel the program anytime. After inputting something, press ENTER to continue.")
            print("Enter message to spam:")
            message = input()
            print("Enter how many times you'd like to spam (only enter a number):")
            try:
                spams = int(input())
            except:
                print("That wasn't a number... PROGRAM RESTARTING.")
                print("\n")
                userInfo()
            print(
                "Enter time between each message in seconds (recomended minimum = 2; only enter a number):")
            try:
                delay = int(input())
            except:
                print("That wasn't a number... PROGRAM RESTARTING.")
                print("\n")
                userInfo()
            print("Press ENTER here, then quickly move your mouse cursor to the textfield you'd like to spam (5 second delay before spam starts).")
            input()
            print("Starting... MOVE YOUR CURSOR TO TEXTFIELD!!")
            SpamTime(message=message, spams=spams, delay=delay)
    except KeyboardInterrupt:
        print("Error caught. Likely caused by entering non-numerical values where numerical values are expected. PROGRAM RESTARTING.")
        print("\n")
        userInfo()


userInfo()
