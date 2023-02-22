from .dirs import *


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class DisplayText:
    TITLE = """===========================================================================

                    XOR Encryption by WTE - Version 1.0                    

===========================================================================
"""
    CH = """====================================================
               Encryption in progress               
             Don't make any file changes            
====================================================
"""
    DCH = """====================================================
               Decryption in progress               
             Don't make any file changes            
====================================================
"""
    END = """====================================================
                 Operation completed                
====================================================
"""


def show_files(header: str, folder: str, color: str):
    print("    " + header)
    for file in filelist(folder):
        print(color + "         -" + file + Colors.ENDC)
    print("")
