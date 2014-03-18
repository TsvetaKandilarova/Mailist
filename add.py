import sys
from glob import glob

def add():
    if len(sys.argv) == 2:
        contact = []
        _list = glob("list_*")
        
        k = int(sys.argv[1])
        if  k <= len(_list):
            list = open("%s" %(_list[k]),"a")
            name_list = _list[k][5:- 4:]
            name = input("Name ")
            email = input("Email ")
            contact.append(name)
            contact.append(email)
            list.write("\n%s - %s" %(contact[0],contact[1]))
            print("%s <%s> was added to %s!" %(name,email,name_list))
        else:
            print("List with unique identifier %s was not found!" %(sys.argv[1]))
    else:
        print("Wrong input!")


def main():
    add()

if __name__ == '__main__':
    main()
