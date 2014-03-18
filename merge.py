import sys
# ne e zavarsheno ochevidno 
def merge():
    list1 = sys.argv[1]
    list2 = sys.argv[2]
    new_list = sys.argv[3]

    nl = open("%s" %(new_list),"a")
    l1 = open("%s" %(list1),"r")
    nl.write(l1.read())







def main():
    merge()
if __name__ == '__main__':
    main()