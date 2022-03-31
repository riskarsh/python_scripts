#!/usr/bin/python3
import sys

#Check if one string is permutation or not

def main(str,str1):
    if len(str) != len(str1):
        print('Not a permutation')
        return False
    elif sorted(str) == sorted(str1):
        print('Permutation')
        return True
    else:
        print('Not a permutation')
        return False

str = sys.argv[1]
str1 = sys.argv[2]

if __name__ == '__main__':
    main(str, str1)