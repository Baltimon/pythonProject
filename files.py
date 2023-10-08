name = "test.txt"
#file= open(name,"r") #read
#file= open(name,"w") # delite and write new
#file= open(name,"a+") #write more
#file.close()
#file.seek()# move to the start

#file.read() #reads all
#file.readline() #read line by line
#file.readlines()#rad all lines and save them in a list

#file.writelines("Hallo \n","Bye \n")

#file=open(name,"r+")
#file.seek(0)
#content= 1
#while (content):
#  content= file.readlines()
#  print(len(content))
#  print(content)
#file.close

def readFiletoList(filename):
  file=open(filename,"r")
  list=file.readlines()
  file.close
  for i in range(len(list)):
    list[i]=list[i].replace("\n","")
  return list
  
def saveList(list, filename):
  file=open(filename,"w")
  file.write("")
  file.close
  file=open(filename,"a+")
  for i in range(len(list)):
    file.seek(0)
    file.write(list[i]+"\n")
  file.close
  
saveList(["hallo","tschüss"],name)
print(readFiletoList(name))    
saveList(["eins","zwei"],name)
print(readFiletoList(name))