#osoba=["Sofija", 25, "plava",True]
#for x in range(len(osoba)):
#    print(osoba[x])

#for osobina in osoba:
#   print(osobina)
#voce_i_povrce=["jabuka","bijeli luk","crveni luk","banana","mandarina"]
#for stavka in voce_i_povrce:
    #print(stavka)

#for indeks in range(len(voce_i_povrce)):
#    print(indeks, voce_i_povrce[indeks])

#for indeks,vrijednost in enumerate(voce_i_povrce):
#    print("Indeks:",indeks,"Stavka:",vrijednost)

#automobili=["Citroen", "BMW","Opel","Mercedes", "Citroen","Opel"]
#for pozicija,auto in enumerate(automobili):
#    if len(auto)==3:
#        print(auto)
#    #print("Pozicija:", pozicija,"Auto:", auto)

#automobili.append("Mercedes")
#automobili[2]="Opel corsa"
#automobili[3]="Kia sportage"
#del automobili[3]
#automobili.remove("BMW")
#automobili.pop(0)
#automobili.clear()
#print(automobili)


#automobili=["Citroen", "BMW","Opel","Mercedes", "Citroen","Opel", "Peugeot"]

#automobili_na_akciji=[]

#for i in range(len(automobili)):
#    if i==1 or i==2 or i==3:
#        automobili_na_akciji.append(automobili[i])
#print(automobili_na_akciji)

#automobili_na_akciji=automobili[0:6:2]
#print(automobili_na_akciji)

numbers=[2,8,12,7,5,14,11,15]
parni=[]
neparni=[]

for broj in numbers:
    parni.append(broj) if broj%2==0 else neparni.append(broj)
    #if broj%2 == 0 :
    #   parni.append(broj)
    #else:
    #    neparni.append(broj)
print(parni,neparni)



