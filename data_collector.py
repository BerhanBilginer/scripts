import keyboard
import uuid #with this library we can record our screen in real time.
import time
from PIL import Image
from mss import mss

mon = {"top":388, "left": 734, "width":275, "height":200}
sct = mss() # we use this library bc of to transform these coordinates of screen (ROI) to frames.

i = 0

def record_screen(record_id, key):
    global i 
    i +=1

    print("{}: {}".format(key,i)) # i means is how many times we press the "key" and key means is which key we preesed on the board.
    img = sct.grab(mon)
    im = Image.frombytes("RGB", img.size, img.rgb)
    im.save("./img/{}_{}_{}.png".format(key,record_id,i))

is_exit = False

def exit():
    global is_exit
    is_exit = True

keyboard.add_hotkey("esc",callback=is_exit)
record_id = uuid.uuid4()

while True:
    if is_exit: break


    #what we do in here is: We created a case. That case includes keys that helps teaching to our neural network. Try - Except command is working like that:
        # it tries command that inclueds in it and if there is any potential error in the command it will keep going on it and that s gonna protect our
        # code from crashing.

    try:
        if keyboard.is_pressed(keyboard.KEY_UP): #when we pressed "up key" our neural network will learn that the dinasour is gonna jump
            record_screen(record_id, key="up")
            time.sleep(0.1) #we use this because the passing of between keys are not gonna mess up
        elif keyboard.is_pressed(keyboard.KEY_DOWN): #when we pressed "down key" our neural network will learn that the dinasour is gonna lay down
            record_screen(record_id, key="down")
            time.sleep(0.1)
        elif keyboard.is_pressed("right"): #when we pressed "right key" our neural network will learn nothing is gonna change. That'll protect our neural network from collapsing if get pressed another key.
            time.sleep(0.1)
            record_screen(record_id, key="right")
    except RuntimeError: continue