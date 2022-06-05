# pip freeze > requirements.txt
#* Initialize and Imports
import updateKeyboardTemplates
updateKeyboardTemplates.update__all__()
import os
from keyboardTemplates import *

#* -- Variables
path = os.path.dirname(__file__) #? Directory path

#* -- Functions
def clearConsole() -> None: #? Clear console
    os.system("cls" if os.name == "nt" else "clear")

def main() -> None:
    kbDefault.test()
    kbTest0.test()
    kbTest1.test()

#! Main
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
