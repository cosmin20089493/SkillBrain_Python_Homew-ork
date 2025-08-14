nume_corect = "Cosmin"
parola_corecta = "12345678"

nume_introdus = input("Introdu numele de utilizator: ")
parola_introdusa = input("Introdu parola: ")

if nume_introdus == nume_corect and parola_introdusa == parola_corecta:
    print("Acces permis")
elif nume_introdus == nume_corect or parola_introdusa == parola_corecta:
    print("User/Password incorect")
else:
    print("Acces respins")
