import eel
import bin.OsType as IDEN
browserMode = IDEN.SystemType(True) 
try:
    eel.init('web')
    eel.start('index.html', mode=browserMode, size=(200, 100))
except OSError:
    import bin.error as error
    error.ERROR("UNKNOWN")

