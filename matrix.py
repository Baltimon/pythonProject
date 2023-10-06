a=[[1,2,3,4],[5,6,7,8]]
for i in range(len(a)):
  for e in range(len(a[i])):
    print(a[i][e])
    
def createMX(r,c):
  MX=[]
  for i in range(r):
    MX.append([])
    for e in range(c):
      MX[i].insert(e,5)
  return MX
  
def addMX(A,B):
  MX=[]
  for i in range(len(A)):
    MX.append([])
    for e in range(len(A[i])):
      MX[i].insert(e,A[i][e]+B[i][e])
  return MX
  
def printMX(mx):
  print("--------")
  for x in range(len(mx)):
    row=""
    for y in range(len(mx[x])):
      row =row +str(mx[x][y])+" "
    print(row)
  print("------")
      
  
def initMX(mx):
  counter=0
  for x in range(len(mx)):
    for y in range(len(mx[x])):
      counter=counter+1
      mx[x][y]=counter
      
  return mx
      
Mat=createMX(8,8)
printMX(Mat) 
a2=initMX(Mat)
printMX(a2)
mat1=createMX(4,4)
mat2=initMX(createMX(4,4))
res=addMX(mat1,mat2)
printMX(res)

