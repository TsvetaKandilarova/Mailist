import sys
from glob import glob


def create_list():
    _list = glob("list_*")
    for i in range(len(_list)):
        _list[i] = _list[i][5:- 4:]

    # print ("Test:")
    # print (_list)
    if str(sys.argv[1]) in _list:
        print("A list with name <" + str(sys.argv[1]) + "> already exists!")
    else:
        file = open("list_" + str(sys.argv[1]) + ".txt", "w")
        file.close()


def main():
    create_list()

if __name__ == '__main__':
    main()
