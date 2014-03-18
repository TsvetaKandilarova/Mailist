from glob import glob


def show_lists():
    _list = glob("list_*")
    for i in range(len(_list)):
        _list[i] = _list[i][5:- 4:]
        print ("[" + str(i + 1) + "] " + _list[i])


def main():
    show_lists()

if __name__ == '__main__':
    main()
