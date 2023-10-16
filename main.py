from random import random

# name of the File with the wirds
filename="wordslist.txt"


# prints the Menu
def menu():
  print("\nHello and Welcome to Hangman by Baltimon \n")
  print("1. START Game")
  print("2. Add Word")
  print("3. END Game")


# prints how many Lives are left
def printLives(live):
  print("You have ", live, "  left!!")

  
# Checks if the word is guest completely  
def testWin(solution):
  win = False
  for i in range(len(solution)):
    win = True
    if (solution[i]==" _ "):
      return False
  return win

  
# Loads al words from the File and returns one random word
def selectWord():
  file=open(filename,"r+")
  words=file.readlines()
  file.close
  for i in range(len(words)):
    words[i]=words[i].replace("\n","")
  x=int(len(words)*random()) #coose a randim index
  word=words[x].upper() #load the word from the index
  listedword=list(word)
  return listedword


# contains game loop with game logic and user-interaction during the game
def game():
  live=10
  word=selectWord()
  solution=[]
  for i in range(len(word)):
    solution.append(" _ ")
  while(live > 0 and not testWin(solution)):
    print("Guess the Letters ")
    printLives(live)
    print(solution)
    gues = input().upper()
    found = False
    for i in range(len(word)):
      if(gues==(word[i])):
        solution[i]= word[i]
        found=True
    if(found==False):
      live=live-1     
  if(testWin(solution)):
    print("Your Won !!!")
    print(solution)
  else:
    print(" You Lost :(")

  
# Askes payer for a word and adds it to the List in the file  
def addWord(word):
  file=open(filename,"a+")
  file.write("\n"+word)
  file.close
  

# prints al words in the file
def printFile():
  file=open(filename,"r+")
  words=file.readlines()
  for i in range(len(words)):
    words[i]=words[i].replace("\n","")
  print(words)
  file.close

# main function. this is going to be executed when starting the program
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
    if (x==3):
      print("\nThe END\n\ngood bye\n")
      break
  
main()