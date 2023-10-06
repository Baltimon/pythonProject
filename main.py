from random import random

#name of the File with the wirds
filename="wordslist.txt"


#prints the Menu
def menu():
  print("Hello and Welcome to Hangman by Baltimon \s \s")
  print("1. START Game")
  print("2. Add Word")
  print("3. END Game")


# Define Global Vareables
win = False
live = int(10)


# prints how many Loves are left
def printLives():
  global live
  print("You have ", live, "  left!!")
  
# Checks if the word is guest completely  
def testWin(solution):
  global win
  for i in range(len(solution)):
    win = True
    if (solution[i]==" _ "):
      win = False
      
#Loads al words from the File and returns one random word
def selectWord():
  file=open(filename,"r+")
  words=file.readlines()
  for i in range(len(words)):
    words[i]=words[i].replace("\n","")
  x=int(len(words)*random()) #coose a randim index
  word=words[x] #load the word from the index
  listedword=list(word)
  return listedword



# runns the game
def game():
  global live
  global win
  word=selectWord()
  solution=[]
  for i in range(len(word)):
    solution.append(" _ ")
  
  while(live > 0 and win == False):
    print("Guess the Letters ")
    printLives()
    print(solution)
    gues = input()
    found = False
    for i in range(len(word)):
      if(gues==(word[i])):
        solution[i]= word[i]
        found=True
    if(found==False):
      live=live-1  
    testWin(solution)
  if(win == True):
    print("Your Won !!!")
    print(solution)
  else:
    print(" You Lost :(")
  
#Askes payer for a word and adds it to the List in the file  
def addWord(word):
  file=open(filename,"a+")
  file.write("\n"+word)
  file.close
  
#prints al words in the file
def printFile():
  file=open(filename,"r+")
  words=file.readlines()
  for i in range(len(words)):
    words[i]=words[i].replace("\n","")
  print(words)
  file.close



def main():
  while(True):
    menu()
    x= int(4)
    while(x != 1 and x != 2 and x != 3):
      x= int(input("What do you want to do ?"))
  
    if (x==1):
      game()
    if (x==2):
      print("\nEnter your wornd\n")
      wrd=input("enter yout new Word:")
      print("Your list is now ")
      addWord(wrd)
      printFile()
      #TODO
      #neue Methode adden die Wort in die datei speichert
    if (x==3):
      print("\nThe END\n\ngood bye\n")
      break
  
main()