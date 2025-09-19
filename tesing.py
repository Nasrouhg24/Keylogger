from pynput.keyboard import Key, Listener #importing what we need to listenn on the keyboard   
from pynput.mouse import Controller #importing what we need to listenn on the mouse 


#Function to Liten on the mouse 
def Mouse_listener():
    mouse = Controller()
    mouse.position= (10,20)

#Function to listen on the keyboard 
def Keyboard_listener():
    Keyboard = Controller()
    Keyboard.type('U re done !')
    Keyboard_listener()