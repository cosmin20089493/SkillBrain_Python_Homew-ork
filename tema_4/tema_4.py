#Pentru inceput ii cerem utilizatorului sa introduca un cod 

pin=input("Introdu un cod PIN:")
#prin >lower() transformam toate literele in minuscule
pin=pin.lower()
#functia len() ne spune cate caractere are un sir de text
lungime=len(pin)

if lungime<6:
    print("Parola slaba")
elif lungime<=10:
    print("Parola medie")
else:
    print("Parola sigura")
    

