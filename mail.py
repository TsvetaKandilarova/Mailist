from subprocess import call
def main():
    print("Hello Stranger! This is a cutting-edge, console-based mail-list!Type help, to see a list of commands.")
    while True:
        command = input("")
        call("py %s" %(command))



if __name__ == '__main__':
    main()