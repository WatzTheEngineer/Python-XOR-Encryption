from src import *

if __name__ == "__main__":

    clear()
    checkdirs()
    opid: int = -1

    print(DisplayText.TITLE)

    while opid != 5:

        print(Colors.BOLD + "File detected :" + Colors.ENDC)
        print("")
        show_files("Readable files :", "dcr", Colors.OKBLUE)
        show_files("Encrypted files :", "ecr", Colors.OKCYAN)
        show_files("Key files :", "keys", Colors.OKGREEN)

        print("Select an operation :\n")
        print("    0 : Encrypt files")
        print("    1 : Encrypt files and keys")
        print("    2 : Decrypt keys")
        print("    3 : Decrypt files")
        print("    4 : Decrypt files and keys")
        print("    5 : Quit")

        while True:
            try:
                opid = int(input("\nOperation [0-5] : "))
                if (opid <= 5) & (opid >= 0):
                    break
                else:
                    print(Colors.FAIL + str(opid) + " is not a valid as an operation" + Colors.ENDC)
            except ValueError:
                print(Colors.FAIL + "Invalid operation" + Colors.ENDC)

        match opid:
            case 0:
                print("")
                ch()
            case 1:
                print("")
                if dir_contains_files("dcr"):
                    ch()
                    chk()
                else:
                    ch()
            case 2:
                print("")
                if dir_contains_files("keys"):
                    dchk()
                else:
                    print(Colors.WARNING + "The key folder is empty" + Colors.ENDC + "\n")
                    sleep(2)
            case 3:
                print("")
                dch()
            case 4:
                print("")
                if dir_contains_files("ecr"):
                    dchk()
                dch()
            case 5:
                pass
            case _:
                print(Colors.FAIL + "ERROR INVALID ARGS" + Colors.ENDC)

    print("\n===========================================================================")
