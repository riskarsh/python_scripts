#!/usr/bin/python3
import sys

#String has all unique charecters

def main(str):
    for i in range(len(str)):
        for j in range(i+1,len(str)):
            if (str[i] == str[j]):
                print('Not Unique')
                return False
    print('Unique')            
    return True              


str=sys.argv[1]
if __name__ == '__main__':
    main(str)
