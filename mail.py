from subprocess import call
def main():
    print("Hello Stranger! This is a cutting-edge, console-based mail-list!Type help, to see a list of commands.")
    while True:
        command = input("Enter command ")
        call("py %s.py" %(command),shell = True)



if __name__ == '__main__':
    main()