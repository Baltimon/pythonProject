def printString(message):
  for i in range(len(message)):
    print(message[i],end='')
  print()
    
def printStringHori(message):
  for i in range(len(message)):
    print(message[i])
    
def repetition(text,character):
  counter=0
  for i in range(len(text)):
    if text[i]==character:
      counter+=1
  return counter
  
def solindrom(text):
  text=text.upper()
  text=text.replace(" ","")
  bul=True
  for i in range(int(len(text)/2)):
    if text[i]!=text[len(text)-i-1]:
      bul=False
  return bul
  
def jumper(text):
  return text.replace("\n","<br>")
  
def countVowels(text):
  counter =0
  for i in range(len(text)):
    if text[i]=='a' or text[i]=='e' or text[i]=='i' or text[i]=='o' or text[i]=='u':
      counter+=1
  return counter




    
stri="Hallo"
print(stri.upper)
print(stri.lower)    
    
printString("hallo")
printStringHori("tschüß")
print(repetition("Hallo schnell weg von hier sonst gehts in die Hose !",'e'))
print(solindrom("hallah"))
print(solindrom("wer"))
print(jumper("hallo \n wie gehts?"))
print(countVowels("aeiouwwww"))