list=[-1,4,2,-6,5,3,]

unsorted=True
while(unsorted):
  unsorted=False
  for i in range(len(list)-1):
    if(list[i]>list[i+1]):
      swaper=list[i]
      list[i]=list[i+1]
      list[i+1]=swaper
      unsorted=True
print(list)     