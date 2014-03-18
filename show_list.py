from glob import glob


def print_list(file_name):
    file = open(file_name, "r")
    contents = file.read()
    contents = list(contents.split('\n'))
    for i in range(len(contents)):
        print (("[" + str(i + 1) + "] " + contents[i]))


def show_list(number):
    _list = glob("list_*")
    print_list(_list[number - 1])


def main():
    show_list(1)

if __name__ == '__main__':
    main()
