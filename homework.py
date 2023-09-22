import random

def createList(size,x):
  list=[]
  if(x>0):
    for i in range(size):
      list.append(x)
      
  elif(x== -1):
    for i in range(size):
      list.append(random.randrange(-10,10,1))
    
  return list

def printList(A):
  for i in range(len(A)):
    print("list[",i,"]=",A[i])

def multiplesList(A,x):
  for i in range(len(A)):
    if(A[i]%x==0):
      print("[",i,"]=",A[i])
    
  
def sumList(A):
  ret=0
  for i in A:
    ret=ret+i
  return ret
  
def smalestList(A):
  min=A[0]
  for i in A:
    if(i<min):
      min=i
  return min
  
def menu():
  print("What do you want to do?")
  print("1: Create new List")
  print("2: print List")
  print("3: multiplesList")
  print("4: sumList")
  print("5: smalestList")  
  print("6: END program")
  
def main():
  
  print("please create a list first!")
  size = int(input("enter the size ot your List: "))
  number= int(input("enter the number to fill the List. (-1 will fill the list with Random Numbers): "))
  liste=createList(size,number)
  print("this is your List ",liste)  
    
  while(True):  
    menu()
    choice=int(input("input Number of choice: "))
    
    if(choice==1):
      size = int(input("enter the size ot your List: "))
      number= int(input("enter the number to fill the List. (-1 will fill the list with Random Numbers): "))
      liste=createList(size,number)
      print("this is your List ",liste)
    
      elif(choice==2):
      printList(liste)
      
    elif(choice==3):
      number=int(input("chouse a number wher yxou want to fint multe of it:"))
      multiplesList(liste,number)
    elif(choice==4):
      print("Summ of",liste,"=",sumList(liste))
    elif(choice==5):
      print("Minimun=",smalestList(liste))
    elif(choice==6):
      print("END")
      break
    else:
      print("WRONG INPUT!!!!!!!")
  
   
  
  
  
main()