#Tema: Într-un fișier Python numit tema_capitol_1.py, scrieți un program care să conțină 4 variabile cu
#  valori introduse de utilizator folosind funcția input(). În funcția input() trebuie scrise întrebări
#  adresate utilizatorului, pe care să le ajustați astfel încât răspunsurile să corespundă tipurilor variabilelor:
#  una de tip str (text), una convertită cu int(), una cu float() și una cu bool().
#  Programul va afișa apoi fiecare variabilă împreună cu tipul acesteia, folosind funcțiile print() și type().



nume=input("Cum te cheama?")
varsta=int(input("Ce varsta ai?"))
inaltime=float(input("Ce inaltime ai?").replace(",", "."))
are_catel=bool(input("Ai catel ?"))
print(nume,"-",type(nume))
print(varsta, "-",type(varsta))
print(inaltime,"-",type(inaltime))
print(are_catel, "-",type(are_catel))


# Putin mai "elegant "

#nume=input("Cum te cheama?")
#varsta=int(input("Ce varsta ai?"))
#inaltime=float(input("Ce inaltime ai?).replace(",",".")
#are_catel=input("Ai catel ?")
#if are_catel.lower()== "da":   
#   are_catel=True
#else:
#    are_catel=False
#print(nume,"-",type(nume))
#print(varsta, "-",type(varsta))
#print(inaltime,"-",type(inaltime))
#print(are_catel, "-",type(are_catel))