import random
import string
from hashlib import sha256
from time import sleep

from alive_progress import alive_bar

from src.utils import *


def ch():
    xor("dcr", "ecr", False, False, DisplayText.CH)


def dch():
    xor("ecr", "dcr", True, False, DisplayText.DCH)


def chk():
    xor("keys", "keys", False, True, DisplayText.CH)


def dchk():
    xor("keys", "keys", True, True, DisplayText.DCH)


def xor(input_folder: str, output_folder: str, isreversed: bool, iskey: bool, header: str):
    if iskey:
        k = input("Password : ")
        print("")

    files: list[str] = filelist(input_folder)

    if dir_contains_files(input_folder):

        print(header)

        for a in range(len(files)):
            en = input_folder + "/" + files[a]

            if isreversed:
                ou = output_folder + "/" + files[a].replace("CH$_", "")
                keyfilename = 'keys/key' + files[a].replace("CH$_", "")
            else:
                ou = output_folder + "/" + "CH$_" + files[a]
                keyfilename = 'keys/key' + files[a]

            ksz = os.path.getsize(en)
            print(files[a], ' size : ', ksz, 'bytes')
            print("")

            with alive_bar(ksz) as bar:
                if not iskey:
                    if isreversed:
                        try:
                            k = open(keyfilename, 'r').read()
                        except FileNotFoundError:

                            print(Colors.FAIL
                                  + "The key file is missing in folder 'keys' or is still encrypted"
                                  + Colors.ENDC)
                            exit(1)
                    else:
                        k = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=ksz))
                ks = sha256(k.encode('utf-8')).digest()
                if not iskey:
                    open(keyfilename, 'wb').write(bytes(k.encode('utf-8')))
                with open(en, 'rb') as f_en:
                    with open(ou, 'wb') as f_ou:
                        i = 0
                        while f_en.peek():
                            c = ord(f_en.read(1))
                            j = i % len(ks)
                            b = bytes([c ^ ks[j]])
                            f_ou.write(b)
                            i = i + 1
                            bar()

            os.remove(en)
            if isreversed and not iskey:
                os.remove(keyfilename)

            print("")
        print(DisplayText.END)

    else:
        print(Colors.WARNING + "The folder " + input_folder + " is empty" + Colors.ENDC + "\n")
    sleep(2)
