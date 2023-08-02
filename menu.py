import sys
import os
sys.path.append(r"C:\Users\coolm\PycharmProjects\Chess\venv\Lib\site-packages")
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format
import keyboard
import main
from main import *
import cursor


class MenuItem:
    def __init__(self, name, active):
        self.name = name
        self.active = active
        self.isActive()

    def activating(self):
        self.active = True
        self.name = ">" + self.name + "<"

    def deactivating(self):
        self.active = False
        self.name = self.name[1 : -1]

    def isActive(self):
        if self.active:
            self.name = ">" + self.name + "<"


class Pointer:
    def __init__(self, val):
        self.val = val

    def addition(self):
        self.val = self.val + 1
        self.loop()

    def substraction(self):
        self.val = self.val - 1
        self.loop()

    def loop(self):
        if self.val == 3:
            self.val = 0
        elif self.val == -1:
            self.val = 2


def print_menu(menu):
    for elem in menu:
        cprint(figlet_format(f'{elem.name}', font='standard', justify="center"), 'white', 'on_black')


def pressed_down(menu, pointer):
    menu[pointer.val].deactivating()
    pointer.addition()
    menu[pointer.val].activating()
    main.clear_console()
    print_menu(menu)


def pressed_up(menu, pointer):
    menu[pointer.val].deactivating()
    pointer.substraction()
    menu[pointer.val].activating()
    main.clear_console()
    print_menu(menu)

def singleplayer():
    exec(open('main.py').read())

def multiplayer():
    pass

def stop():
    print("\n See you later, baby <3")
    sys.exit(0)

if __name__ == '__main__':
    pointer_dict = {"0": singleplayer, "1": multiplayer, "2": stop}
    menu = [MenuItem("Singleplayer", True), MenuItem("Multiplayer", False), MenuItem("Exit", False)]
    main.clear_console()
    print_menu(menu)
    pointer = Pointer(0)
    cursor.hide()

    while True:
        try:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN and event.name == 'down':
                pressed_down(menu, pointer)
            elif event.event_type == keyboard.KEY_DOWN and event.name == 'up':
                pressed_up(menu, pointer)
            elif event.event_type == keyboard.KEY_DOWN and event.name == 'enter':
                pointer_dict[str(pointer.val)]()
        except KeyboardInterrupt:
            print("\n See you later, baby <3")
            break
