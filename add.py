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
            _email = open("%s" %(_list[k]),"r")
            contents = _email.read()
            if not contains_substring(contents,email):
                list.write("\n%s - %s" %(contact[0],contact[1]))
                print("%s <%s> was added to %s!" %(name,email,name_list))
            else:
                print("A person with the given email %s is already in the list!" %(email))
        else:
            print("List with unique identifier %s was not found!" %(sys.argv[1]))
    else:
        print("Wrong input!")

def contains_substring(haystack, needle):
    i = 0
    while i < len(haystack):
        if haystack[i] == needle[0]:
            k = 0
            while  k < len(needle) and i < len(haystack) and haystack[i] == needle[k]:
                i = i+1
                k = k+1
            if k == len(needle):
                return True
            i = i - 1
        i = i + 1
    return False

def main():
    add()
    #print(contains_substring("haystack", "yst"))

if __name__ == '__main__':
    main()