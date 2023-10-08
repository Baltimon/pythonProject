def uppercaseString(value):
  ret=""
  for i in range(len(value)):
    ret=ret+value[i].upper()
  return ret
    
  
def countRepetitions(value,c):
  counter=0
  for i in range(len(value)):
    if value[i].upper()==c.upper():
      counter +=1
  return counter
  
def printPosSpaces(value):
  pos=[]
  for i in range(len(value)):
    if value[i].upper()==" ":
      pos.append(i)
      
  print(pos)
  
def spellString(value):
  ret=""
  for i in range(len(value)):
    if i == len(value)-1:
      ret=ret+value[i]
    else:
      ret=ret+value[i]+"-"  
  return ret
  
def menu():
  print("1.Uppercase")
  print("2. count Repetition")
  print("3. print pos space")
  print("4. spell String")
  print("5. exit")



def main():
  
  while(True):  
    menu()
    choice=int(input("input Number of choice: "))
    
    if(choice==1):
      v=input("type your text and press enter:")
      print(uppercaseString(v))
    
    elif(choice==2):
      v=input("type your text and press enter:")
      ca=input("type one caracter to search for:")
      print(countRepetitions(v,ca))
      
    elif(choice==3):
      v=input("type your text and press enter:")
      printPosSpaces(v)
    
    elif(choice==4):
      v=input("type your text and press enter:")
      print(spellString(v))
      
    elif(choice==5):
      print("END")
      break
    else:
      print("WRONG INPUT!!!!!!!")

main()