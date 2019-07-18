a=str(input("Enter a character: "))
list=["w","r","t","y","p","s","d","f","g","h","j","k","l","z","x","c","v","b","n","Q","W","R","T","Y","P","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
if(a=="A" or a=="E" or a=="I" or a=="O" or a=="U" or a=="a" or a=="e" or a=="i" or a=="u" or a=="o"):
  print("Vowel")
elif(a in list):
   print("consonant")
else:
   print("Invalid")
