def createMatrix(rows, columns):
  MX=[]
  for i in range(rows):
    MX.append([])
    for e in range(columns):
      print("position: [",i,"][",e,"]")
      x=int(input("value:"))
      MX[i].insert(e,x)
  return MX

def printMatrix(mx):
  print("--------")
  for x in range(len(mx)):
    row=""
    for y in range(len(mx[x])):
      row =row +str(mx[x][y])+" "
    print(row)
  print("------")


def sumMatrix(M):
  sum=0
  for x in range(len(M)):
    for y in range(len(M[x])):
      sum=M[x][y]+sum
  return sum
      
  
def averageMatrix(Mx):
  return sumMatrix(Mx)/(len(Mx)*len(Mx[0]))
   

def rowMatrix(M,row,num):
  for i in range(len(M[row])):
    M[row][i]=M[row][i]+num
  return M
  
def evenPosition(M):
  for x in range(len(M)):
    for y in range(len(M[x])):
      if(M[x][y]%2==0):
        print("[",x,"][",y,"]= ",M[x][y])
  
  
def sumReverseDiagonal(M):
  x=len(M)
  y=len(M[0])
  sum=0
  if x!=y:
    print("Matrix not symetrix! No Diagonale")
    return 0
  else:
    for i in range(x):
      sum += M[i][-(i+1)]
  return sum
  
def menu():
  print("1.Print")
  print("2. Sum")
  print("3. Average")
  print("4.Matrix-Row")
  print("5. Position of even numbers")
  print("6. Reverse diagonal sum")
  print("7. Exit")


def main():
  
  print("please create a Matrix!")
  colum = int(input("enter the number of colums :"))
  row = int(input("enter the number of rows : "))
  M =createMatrix(row,colum)
  print("this is your Matrix")
  printMatrix(M)  
    
  while(True):  
    menu()
    choice=int(input("input Number of choice: "))
    
    if(choice==1):
      printMatrix(M)
    
    elif(choice==2):
      print(sumMatrix(M))
      
    elif(choice==3):
      print(averageMatrix(M))
      
    elif(choice==4):
      row = int(input("enter the number of rows): "))
      num = int(input("enrer the number :"))
      printMatrix(rowMatrix(M,row,num))
    elif(choice==5):
      evenPosition(M)
    elif(choice==6):
      print(sumReverseDiagonal(M))
    elif(choice==7):
      print("END")
      break
    else:
      print("WRONG INPUT!!!!!!!")

main()