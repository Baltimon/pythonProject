def menu():
  print("Hello and Welcome to Hangman by Baltimon \s \s")
  print("1. START Game")
  print("2. END Game")

Letter1 = '_'
Letter2 = '_'
Letter3 = '_'
Letter4 = '_'
Letter5 = '_'
win = False

live = int(5)

def prntWord():
  global Letter1
  global Letter2
  global Letter3
  global Letter4
  global Letter5
  print(Letter1 ," ",Letter2," ",Letter3," ",Letter4," ",Letter5)

def prntLives():
  global live
  print("You have ", live, "  left!!")
  
def testWin():
  global Letter1
  global Letter2
  global Letter3
  global Letter4
  global win
  if (Letter1 != '_' and Letter2 != '_' and Letter3 != '_'  and Letter4 != '_'  and Letter5 != '_'):
   win= True
   print ("--------WIN--------")

def game():
  global live
  global Letter1
  global Letter2
  global Letter3
  global Letter4
  global Letter5
  global win
  while(live > 0 and win == False):
    print("Guess the Letters ")
    prntWord()
    gues = input()
    if( gues == 'h'):
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
       prntLives()
    testWin()
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