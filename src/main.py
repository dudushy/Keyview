# pip freeze > requirements.txt
#* Initialize and Imports
import updateKeyboardTemplates
updateKeyboardTemplates.update__all__()
import os
from keyboardTemplates import *
import keyboard

#* -- Variables
path = os.path.dirname(__file__) #? Directory path

keys = [
    'alt',
    'alt gr',
    'left ctrl',
    'left shift',
    'right ctrl',
    'right shift',
    'windows',
    'capslock',
]

#* -- Functions
def clearConsole() -> None: #? Clear console
    os.system("cls" if os.name == "nt" else "clear")

def main() -> None:
    while True:
        for key in keys:
            if keyboard.is_pressed(key):
                clearConsole()
                print(f"You pressed {key}")
                break

#! Main
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
