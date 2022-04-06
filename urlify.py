#!/usr/bin/python3
import sys
#Urlify- replace the spaces with %20

def main(str,size):
    lst = []
    for i in str:
        if i == ' ':
            url = '%20'
        else:
            url = i
        lst.append(url)
        url_str = ''.join(lst)
    print('the URLified string is',url_str)
    return url_str

str = sys.argv[1]
size = sys.argv[2]

if __name__ == '__main__':
    main(str,size)    