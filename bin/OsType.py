import os
def SystemType(called):
    if called == True:
        get_os = os.name
        stringOs = ''
        if get_os == "nt":
            stringOs = 'edge'
        elif get_os == "posix":
            stringOs = 'chrome'
        else:
            stringOs = 'UNKNOWN'
        return stringOs
