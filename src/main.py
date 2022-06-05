# pip freeze > requirements.txt
#* Initialize
import updateAllModules
updateAllModules.update("src/keyboardTemplates")

#* -- Imports
import os
from keyboardTemplates import *

#* -- Variables
path = os.path.dirname(__file__) #? Directory path

#* -- Functions
def clearConsole() -> None: #? Clear console
    os.system("cls" if os.name == "nt" else "clear")

def main() -> None:
    kbDefault.test()
    test.say("test")

#! Main
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
