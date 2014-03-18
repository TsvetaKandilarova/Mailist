from glob import glob
import sys


def substring(haystack, needle):
    i = 0
    while i < len(haystack):
        if haystack[i] == needle[0]:
            k = 0
            while k < len(needle) and i < len(haystack) and haystack[i] == needle[k]:
                i = i + 1
                k = k + 1
            if k == len(needle):
                return True
            i = i - 1
        i = i + 1
    return False


def search_email():
    _list = glob("list_*")
    new_list = []

    for i in range(len(_list)):
        file = open(_list[i], "r")
        contents = file.read()
        contents = list(contents.split('\n'))
        #print (contents)
        # if str(sys.argv[1]) in contents:
        #     new_list.append("[" + str(i + 1) + "] " + _list[i][5:- 4:])
        # for i in range(len(contents)):
        if substring(contents[i], str(sys.argv[1])):
            new_list.append("[" + str(i + 1) + "] " + _list[i][5:- 4:])
        file.close()

    if len(new_list) == 0:
        print ("<" + str(sys.argv[1]) + "> was not found in the current mailing lists.")
    else:
        print("< " + str(sys.argv[1]) + " > was found in:")
        for item in new_list:
            print (item)


def main():
    search_email()

if __name__ == '__main__':
    main()
