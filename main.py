import eel
import bin.OsType as IDEN
browserMode = IDEN.SystemType(True) 
try:
    eel.init('web')
    eel.start('index.html', mode=browserMode, size=(200, 100))
except OSError:
    print("Fatal Error. \nPossible problems: Unrecognised OS or Chrome(Chromium)/Edge is not installed")
    print(f"logs: Received - {browserMode}")

