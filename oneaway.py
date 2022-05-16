#!/usr/bin/python3
import sys
#two words are one edit away or not (insert, delete, update)

def check(word, word1):
    #differnce shouldnt be greater than 1
     
    if len(word) - len(word1) > 1:
        print(word, ",", word1, " ->  False")
        return False

    # number of letters in the word and word1
    letter=0
    letter1=0

    counter = 0

    while letter1 < len(word1):

        if word[letter] != word1[letter1]:
            #counter for edits
            counter += 1
            if counter > 1:
                print(word, ",", word1, " ->  False")
                return False

            #move to next character in longer word    
            letter += 1

            if len(word) == len(word1):
                letter1 +=1

        else:
            letter += 1
            letter1 += 1
    print(word, ",", word1, " ->  True")
    return True

if len(sys.argv) < 3:
        print('usage:oneaway.py <bigger word> <smaller word>')
        exit(1)
word = sys.argv[1]
word1 = sys.argv[2]
if __name__ == '__main__':
    check(word, word1)

                  
        


