#Cerem utilizatorului numarul de secunde
secunde=int(input("secunde="))

#Afisam ore, minute, secunde

print("ore=",secunde//(60*60),
      "\n""minute=", (secunde%(60*60))//60 ,
      "\n""secunde=", (((secunde%(60*60)))%3600)%60)