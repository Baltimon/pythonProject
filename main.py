

def menu():
  print("Hello and Welcome to Hangman by Baltimon \s \s")
  print("1. START Game")
  print("2. END Game")


# Define Global Vareables
Letter1 = '_'
Letter2 = '_'
Letter3 = '_'
Letter4 = '_'
Letter5 = '_'
win = False
live = int(5)
words=["house","rat","bottle","tree"]


# prints the word in the current status
def prntWord():
  #'global Letter1
  #global Letter2
  #global Letter3
  #global Letter4
  #global Letter5
  #print(Letter1 ," ",Letter2," ",Letter3," ",Letter4," ",Letter5)

# prints how many Loves are left
def printLives():
   global live
   print("You have ", live, "  left!!")
  
# Checks if the word is guest completely  
def testWin(solution):
  for i in range(len(solution)):
    if lolution[i].equals(" _ ")
    return false
  return true
   
  #global Letter1
  #global Letter2
  #global Letter3
  #global Letter4
  #global win
  #if (Letter1 != '_' and Letter2 != '_' and Letter3 != '_'  and Letter4 != '_'  and Letter5 != '_'):
  # win= True
  # print ("--------WIN--------")
  
def selectWord():
  x=int(len(words)*random()) #coose a randim index
  word=words[x] #load the word from the index
  listedword=split(word)
  return listedword



# runns the game
def game():
  #global Letter1
  #global Letter2
  #global Letter3
  #global Letter4
  #global Letter5
  global live
  global win
  word=selectWord()
  solution=[]
  for i in range(len(word)):
    solution[i]= " _ "
  
  while(live > 0 and win == False):
    print("Guess the Letters ")
    printLives()
    prnt(solution)
    gues = input()
    found = False
    for i in range(len.word):
      if(gues.equals(word[i])):
        solution= word[i]
        found=True
    if(found=False):
      live=live-1  
    
    '''if( gues == 'h'):
      Letter1 =  'h'
      prntWord()
      prntLives()
    elif( gues == 'o'):
      Letter2 = gues
      prntWord()
      prntLives()
    elif( gues == 'u'):
      Letter3 = gues
      prntWord()
      prntLives()
    elif( gues == 's'):
      Letter4 = gues
      prntWord()
      prntLives()
    elif( gues == 'e'):
      Letter5 = gues
      prntWord()
      prntLives()
    else:
       live = live-1
    '''   prntLives()
  win= testWin(solution)
  if(win == True):
    print("Your Won !!!")
  else:
    print(" You Lost :(")
  
  



def main():
  menu()
  x= int(4)
  while(x != 1 and x != 2):
    x= int(input("What do you want to do ?"))
  
  if (x==1):
    game()
  if (x==2):
    print("The END  \s \s good bye")
  
main()