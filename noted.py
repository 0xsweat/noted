import os
import sys
import datetime
from colorama import Fore
usage = r"""
███╗   ██╗ ██████╗ ████████╗███████╗██████╗ 
████╗  ██║██╔═══██╗╚══██╔══╝██╔════╝██╔══██╗
██╔██╗ ██║██║   ██║   ██║   █████╗  ██║  ██║
██║╚██╗██║██║   ██║   ██║   ██╔══╝  ██║  ██║
██║ ╚████║╚██████╔╝   ██║   ███████╗██████╔╝
╚═╝  ╚═══╝ ╚═════╝    ╚═╝   ╚══════╝╚═════
            made by 0xsweat
            usage : noted [OPTION]
            options : 
                view : view your notes
                add : add a note
"""
notedascii = r"""
███╗   ██╗ ██████╗ ████████╗███████╗██████╗ 
████╗  ██║██╔═══██╗╚══██╔══╝██╔════╝██╔══██╗
██╔██╗ ██║██║   ██║   ██║   █████╗  ██║  ██║
██║╚██╗██║██║   ██║   ██║   ██╔══╝  ██║  ██║
██║ ╚████║╚██████╔╝   ██║   ███████╗██████╔╝
╚═╝  ╚═══╝ ╚═════╝    ╚═╝   ╚══════╝╚═════
"""
try :
    option = sys.argv[1]
    if str(option) == "--help":
        print(Fore.BLUE + usage)
        quit()
    if os.path.isfile("/home/" + str(os.getlogin()) + "/.notednotes") == False and os.path.isfile("/home/" + str(os.getlogin()) + "/.notednotes.cpt") == False:
        print(Fore.GREEN + "Your notes were not found in /home/" + str(os.getlogin()) + "/.notednotes.cpt creating a new notes file it will be located at /home/" + str(os.getlogin()) + "/.notednotes.cpt")
        os.system('touch /home/' + str(os.getlogin()) + '/.notednotes && /bin/ccrypt -e -K "NOTED" /home/' + str(os.getlogin()) + "/.notednotes")
except Exception as e:
    print(Fore.RED + "ERROR : please enter an option")
    print(Fore.BLUE + usage)
    quit()
print(Fore.BLUE + notedascii)
if str(option) == "view":
    os.system('/bin/ccrypt -d -K "NOTED" /home/' + str(os.getlogin()) + '/.notednotes.cpt')
    print("Would you like to view them all or just one?")
    ans = str(input("-# "))
    if ans == "all":
        print(Fore.MAGENTA + "Your saved notes : ")
        os.system("cat /home/" + str(os.getlogin()) + '/.notednotes')
    else:
        print("Enter in the note's name, or date")
        note2search4 = str(input("-# "))
        print(Fore.MAGENTA)
        with open ("/home/" + str(os.getlogin()) + "/.notednotes", 'r') as file:
            nr = file.read()
            file.close()
        s1 = nr.split("\n")
        for i in range(0, len(s1)):
            if note2search4 in str(s1[i]):
                print(s1[i])
                for x in range(i + 1, len(s1)):
                    if str(s1[x]) != "~~~~~~~~~~~~~~~~NOTE~~~~~~END~~~~~~~~~~~~~~~~~":
                        print(str(s1[x]))
                    else:
                        print(str(s1[x]))
                        os.system('/bin/ccrypt -e -K "NOTED" /home/' + str(os.getlogin()) + '/.notednotes')
                        quit()
        print(Fore.RED + "Note could not be found.")
        os.system('/bin/ccrypt -e -K "NOTED" /home/' + str(os.getlogin()) + '/.notednotes')
        quit()
    os.system('/bin/ccrypt -e -K "NOTED" /home/' + str(os.getlogin()) + '/.notednotes')
    quit() 
elif str(option) == "add":
    os.system('/bin/ccrypt -d -K "NOTED" /home/' + str(os.getlogin()) + '/.notednotes.cpt')
    print("Enter in the name : ")
    name = str(input("-# "))
    print("Enter in the note (type in note.finish when you are done writing): ")
    contents = []
    ntxt = ''
    nl = ''
    ls = "\n"
    ln = 0
    while nl != 'note.finish':
        ln = ln + 1
        nl = input("# " + str(ln) + " # ")
        if nl != 'note.finish':
                contents.append(nl)
                contents.append(ls)
    ntxt = ''.join(contents)
    with open('/home/' + str(os.getlogin()) + '/.notednotes', "a") as f:
        f.write("# " + name + " " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + " USER : " + str(os.getlogin()) + " #\n" + ntxt + "\n~~~~~~~~~~~~~~~~NOTE~~~~~~END~~~~~~~~~~~~~~~~~\n")
        f.close()
    print(Fore.GREEN + "Saved!")
    os.system('/bin/ccrypt -e -K "NOTED" /home/' + str(os.getlogin()) + '/.notednotes')
    quit()