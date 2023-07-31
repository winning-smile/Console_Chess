import sys
import os
sys.path.append(r"C:\Users\coolm\PycharmProjects\Chess\venv\Lib\site-packages")
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format

def win_out(color):
       clear = lambda: os.system('cls')
       clear()
       if color == "White":
              cprint(figlet_format('White wins!', font='doom'),'white', 'on_black', attrs=['bold'])
       else:
              cprint(figlet_format('Black wins!', font='doom'), 'white', 'on_black', attrs=['bold'])