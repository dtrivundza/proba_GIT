#         0        1     2      3
#osoba= ["Sofija", 20, "plava",True]
#print(osoba)
#print(osoba[0])
#print("godine:",osoba[1])
#automobili=["opel","citroen","mercedes"]
#print(automobili[1])

#for x in range(20,10,-2):
#print(x)
#     012345
#kurs="python"
#print(kurs[0])
#for x in range(len(kurs)):
#    print("Na poziciji",x,kurs[x])

#ustanova="IT Academy"
#for indeks in range(len(ustanova)):
#    print(ustanova[indeks])
#primjer="zadatak1"

#for indeks in range(len(primjer)):
    #print(primjer[indeks])

#cities=["Berlin"," BL","BG"]

#for e in range(len(cities)):
#    cities[e]=cities[e]+"2"
#print(cities)
#name="Jason Momoa"
#name_length=len(name)
#print("Broj karaktera:",name_length)
#name_valid=name.lower()
#print(name_valid)
#primjer="zadatak"
#broj_karaktera=len(primjer)
#indeks=0
#while broj_karaktera<indeks:
#    indeks=+1
#   print(primjer[indeks])

korisnicko_ime="admin"
unijeto_korisnicko_ime=input("Unesi korisnicko ime:").lower()

if korisnicko_ime== unijeto_korisnicko_ime:
    print("Pogodili ste.")
else:
    print("Pogresni podaci.")
