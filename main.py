list=[0.2,0.4,0.6,0.8]
for i in list:
  i = i+8
  print(i)
for i in range(len(list)):
  list[i] =list[i] +8
print(list)
list= [0,0,0,0,0,0,0,0,0,0]
for i in range(1,11):
  list[i-1]=i

list[7]=list[6]+list[9]
list[8]=3*list[4]-57
print(list)
list.append(300)
list.insert(2,200)
print(list)

def addTwo(list):
  for i in range(len(list)):
    list[i]=list[i]+2
  print(list)
  
addTwo(list)

def printList(list):
  for i in range(len(list)):
    print("[",i,"] :",list[i])
    
printList(list)