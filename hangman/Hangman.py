import random
from words import words

def hangman():
    word=random.choice(words).upper()
    wordlist=set(list(word.upper()))
    userlist=[]
    while len(wordlist) >0:
        print("Used letters :",userlist)
        #print("Original word :",word)
        for i in word:
            if i in userlist:
                print(i,end="")
            else:
                print("-",end="")
        print("")
        userip=input("Enter your input :").upper()
        if userip in userlist:
            print("letter already used try again")
            continue
        elif userip in wordlist:
            wordlist.remove(userip)
            userlist.append(userip)
        else:
            userlist.append(userip)
    print(f'Yaay! you guessed the word {word} correctly')
hangman()
