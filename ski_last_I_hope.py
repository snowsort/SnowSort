from math import*
import csv
file=open('ski4_1.csv','r') 
csv1=csv.DictReader(file,delimiter=',')
l=[]
for line in csv1:
    l.append(dict(line))
csv2={}
for row in l:
    for key, value in row.items():
        if key not in csv2:
            csv2[key] = [value]
        else:
            csv2[key].append(value)
import csv
file_1 = open('Station de ski.csv', 'r')
csv3 = csv.DictReader(file_1, delimiter=',')
nom_stations = []
for ligne in csv3:
    nom_stations.append(ligne['Abondance'])  # "nom_station" est le nom de la colonne contenant les noms des stations
nom_stations.insert(0,'Abondance')
liste_zéro=[]
o=len(nom_stations)
for bonjour in range(0,o):
    liste_zéro.append(0)
dictionnaire=dict(zip(nom_stations,liste_zéro))
print(dictionnaire)
def menu():
    print("Dans ce programme, vous allez choisir certaines caractéristiques que vous voulez dans votre station de ski et vous allez associé à ces stations de ski un nombre, ce nombre représentera l'importance que vous donnez à cette caractèristique, \n plus elle est haute, plus vous souhaitez retrouver cette caractéristique dans votre station. \n pour trouver les stations de ski qui correspondent à vos exigences, chaque station de ski sera associé à la somme des nombres des caractéristiques choisies, les stations avec le plus grand nombre vous serons conseillées")
    print("Dans quelle massif voulez-vous aller ?"+"\n tapez 1 pour choisir les alpes du nord"+"\n tapez 2 pour choisir les alpes du sud"+"\n tapez 3 pour choisir le jura"+"\n tapez 4 pour choisir le massif central"+"\n tapez 5 pour choisir les pyrénées"+"\n tapez 6 pour choisir les vosges")
    a=int(input("votre choix : "))
    coefficient=int(input("votre nombre associé à cette caractéristique :"))
    if a==1:
        w=csv2['Alpes du Nord']
        for dieu in range(0,len(w)):
            for diable in range(0,o):
                valeur=nom_stations[diable]
                if w[dieu]==nom_stations[diable]:
                    dictionnaire[valeur]+=coefficient
    elif a==2:
        w=csv2['Alpes du Sud']
        for dieu in range(0,len(w)):
            for diable in range(0,o):
                valeur=nom_stations[diable]
                if w[dieu]==nom_stations[diable]:
                    dictionnaire[valeur]+=coefficient
    elif a==3:
        w=csv2['Jura']
        for dieu in range(0,len(w)):
            for diable in range(0,o):
                valeur=nom_stations[diable]
                if w[dieu]==nom_stations[diable]:
                    dictionnaire[valeur]+=coefficient
    elif a==4:
        w=csv2['Massif Central']
        for dieu in range(0,len(w)):
            for diable in range(0,o):
                valeur=nom_stations[diable]
                if w[dieu]==nom_stations[diable]:
                    dictionnaire[valeur]+=coefficient
    elif a==5:
        w=csv2['PyrÃ©nÃ©es']
        for dieu in range(0,len(w)):
            for diable in range(0,o):
                valeur=nom_stations[diable]
                if w[dieu]==nom_stations[diable]:
                    dictionnaire[valeur]+=coefficient
    elif a==6:
        w=csv2['Vosges']
        for dieu in range(0,len(w)):
            for diable in range(0,o):
                valeur=nom_stations[diable]
                if w[dieu]==nom_stations[diable]:
                    dictionnaire[valeur]+=coefficient
    print("definnissez une altitude moyenne pour votre station"+"\n tapez 1 pour une altitude inférieur à 1000m"+"\n tapez 2 pour une altitude entre 1000m et 1500m"+"\n tapez 3 pour une altitude entre 1500m et 2000m"+"\n tapez 4 pour une altitude de plus de 2000m")
    b=int(input("votre choix : "))
    coefficient=int(input("votre nombre associé à cette caractéristique :"))
    if b==1:
        w=csv2['inferieur Ã\xa0 1000']
        for dieu in range(0,len(w)):
            for diable in range(0,o):
                valeur=nom_stations[diable]
                if w[dieu]==nom_stations[diable]:
                    dictionnaire[valeur]+=coefficient
    elif b==2:
        w=csv2['entre 1000 et 1500']
        for dieu in range(0,len(w)):
            for diable in range(0,o):
                valeur=nom_stations[diable]
                if w[dieu]==nom_stations[diable]:
                    dictionnaire[valeur]+=coefficient
    elif b==3:
        w=csv2['entre 1500 et 2000']
        for dieu in range(0,len(w)):
            for diable in range(0,o):
                valeur=nom_stations[diable]
                if w[dieu]==nom_stations[diable]:
                    dictionnaire[valeur]+=coefficient
    elif b==4:
        w=csv2['entre 2000 et 2500']
        for dieu in range(0,len(w)):
            for diable in range(0,o):
                valeur=nom_stations[diable]
                if w[dieu]==nom_stations[diable]:
                    dictionnaire[valeur]+=coefficient
    print("Combien de piste de ski y attendez vous ?"+"\n tapez 1 pour avoir entre 1 et 14 pistes"+"\n tapez 2 pour avoir entre 15 et 29"+"\n tapez 3 pour avoir entre 30 et 49 pistes"+"\n tapez 4 pour avoir entre 50 et 98 pistes"+"\n tapez 5 pour avoir entre 99 et 187 pistes"+"\n tapez 0 si vous n'en avez aucune idée")
    c=int(input("votre choix : "))
    coefficient=int(input("votre nombre associé à cette caractéristique :"))
    if c==1:
        w=csv2['Entre 14 et 1 pistes']
        for dieu in range(0,len(w)):
            for diable in range(0,o):
                valeur=nom_stations[diable]
                if w[dieu]==nom_stations[diable]:
                    dictionnaire[valeur]+=coefficient
    elif c==2:
        w=csv2['Entre 29 et 15 pistes']
        for dieu in range(0,len(w)):
            for diable in range(0,o):
                valeur=nom_stations[diable]
                if w[dieu]==nom_stations[diable]:
                    dictionnaire[valeur]+=coefficient
    elif c==3:
        w=csv2['Entre 49 et 30 pistes']
        for dieu in range(0,len(w)):
            for diable in range(0,o):
                valeur=nom_stations[diable]
                if w[dieu]==nom_stations[diable]:
                    dictionnaire[valeur]+=coefficient
    elif c==4:
        w=csv2['Entre 98 et 50 pistes']
        for dieu in range(0,len(w)):
            for diable in range(0,o):
                valeur=nom_stations[diable]
                if w[dieu]==nom_stations[diable]:
                    dictionnaire[valeur]+=coefficient
    elif c==5:
        w=csv2['Entre 187 et 109 pistes']
        for dieu in range(0,len(w)):
            for diable in range(0,o):
                valeur=nom_stations[diable]
                if w[dieu]==nom_stations[diable]:
                    dictionnaire[valeur]+=coefficient
    print("Combien de kilometre de piste y attendez vous ?"+"\n tapez 1 pour avoir moins de 30km de pistes"+"\n tapez 2 pour avoir entre 30 et 100 km de pistes"+"\n tapez 3 pour avoir entre 100 et 200 km de pistes"+"\n tapez 4 pour avoir plus de 200 km de pistes"+"\n tapez 0 si vous n'en avez aucune idée")
    d=int(input("votre choix : "))
    coefficient=int(input("votre nombre associé à cette caractéristique :"))
    if d==1:
        w=csv2['inferieur Ã\xa0 30 km ']
        for dieu in range(0,len(w)):
            for diable in range(0,o):
                valeur=nom_stations[diable]
                if w[dieu]==nom_stations[diable]:
                    dictionnaire[valeur]+=coefficient
    elif d==2:
        w=csv2['entre 30 km et 100 km']
        for dieu in range(0,len(w)):
            for diable in range(0,o):
                valeur=nom_stations[diable]
                if w[dieu]==nom_stations[diable]:
                    dictionnaire[valeur]+=coefficient
    elif d==3:
        w=csv2['entre 100 et 200 km']
        for dieu in range(0,len(w)):
            for diable in range(0,o):
                valeur=nom_stations[diable]
                if w[dieu]==nom_stations[diable]:
                    dictionnaire[valeur]+=coefficient
    elif d==4:
        w=csv2['superieur Ã\xa0 200 km']
        for dieu in range(0,len(w)):
            for diable in range(0,o):
                valeur=nom_stations[diable]
                if w[dieu]==nom_stations[diable]:
                    dictionnaire[valeur]+=coefficient
    print("Voulez vous que votre domaine soit connecté ?"+"\n si oui, tapez 1"+"\n si non, tapez 2"+"\n si cela nous vous intéresse pas tapez 0")
    e=int(input("votre choix : "))
    coefficient=int(input("votre nombre associé à cette caractéristique :"))
    if e==1:
        w=csv2['domaine connecte']
        for dieu in range(0,len(w)):
            for diable in range(0,o):
                valeur=nom_stations[diable]
                if w[dieu]==nom_stations[diable]:
                    dictionnaire[valeur]+=coefficient
    print("Combien de kilometre de ski de fond y attendez vous ?"+"\n tapez 0 si cela ne vous interesse pas"+"\n tapez 1 pour avoir moins de 30km de pistes"+"\n tapez 2 pour avoir entre 30 et 100km de pistes"+"\n tapez 3 pour avoir entre 100 et 200km de pistes"+"\n tapez 4 pour avoir plus de 200km de pistes")
    f=int(input("votre choix : "))
    coefficient=int(input("votre nombre associé à cette caractéristique :"))
    if f==1:
        w=csv2['inferieur a 10 km (fond)']
        for dieu in range(0,len(w)):
            for diable in range(0,o):
                valeur=nom_stations[diable]
                if w[dieu]==nom_stations[diable]:
                    dictionnaire[valeur]+=coefficient
    elif f==2:
        w=csv2['entre 10 et 20 km (fond)']
        for dieu in range(0,len(w)):
            for diable in range(0,o):
                valeur=nom_stations[diable]
                if w[dieu]==nom_stations[diable]:
                    dictionnaire[valeur]+=coefficient
    elif f==3:
        w=csv2['entre 20 et 30 (fond)']
        for dieu in range(0,len(w)):
            for diable in range(0,o):
                valeur=nom_stations[diable]
                if w[dieu]==nom_stations[diable]:
                    dictionnaire[valeur]+=coefficient
    elif f==4:
        w=csv2['entre 30 et 50 (fond)']
        for dieu in range(0,len(w)):
            for diable in range(0,o):
                valeur=nom_stations[diable]
                if w[dieu]==nom_stations[diable]:
                    dictionnaire[valeur]+=coefficient
    elif f==5:
        w=csv2['entre 50 et 100 km (fond)']
        for dieu in range(0,len(w)):
            for diable in range(0,o):
                valeur=nom_stations[diable]
                if w[dieu]==nom_stations[diable]:
                    dictionnaire[valeur]+=coefficient
    elif f==6:
        w=csv2['superieur a 100 km (fond)']
        for dieu in range(0,len(w)):
            for diable in range(0,o):
                valeur=nom_stations[diable]
                if w[dieu]==nom_stations[diable]:
                    dictionnaire[valeur]+=coefficient
    print("Quel budjet avez vous pour un forfait pour une journee ?"+"\n tapez 1 pour avoir un forfait inférieur à 10e"+"\n tapez 2 pour avoir un forfait entre 10 et 20e"+"\n tapez 3 pour avoir un forfait entre 20 et 30e"+"\n tapez 4 pour avoir un forfait entre 30 et 40e"+"\n tapez 5 pour avoir un forfait entre 40 et 50e"+"\n tapez 6 pour avoir un forfait de plus de 50e")
    g=int(input("votre choix : "))
    coefficient=int(input("votre nombre associé à cette caractéristique :"))
    if g==1:
        w=csv2['inferieur Ã\xa0 10 (forfait)']
        for dieu in range(0,len(w)):
            for diable in range(0,o):
                valeur=nom_stations[diable]
                if w[dieu]==nom_stations[diable]:
                    dictionnaire[valeur]+=coefficient
    elif g==2:
        w=csv2['entre 10 et 20 (forfait)']
        for dieu in range(0,len(w)):
            for diable in range(0,o):
                valeur=nom_stations[diable]
                if w[dieu]==nom_stations[diable]:
                    dictionnaire[valeur]+=coefficient
    elif g==3:
        w=csv2['entre 20 et 30 (forfait)']
        for dieu in range(0,len(w)):
            for diable in range(0,o):
                valeur=nom_stations[diable]
                if w[dieu]==nom_stations[diable]:
                    dictionnaire[valeur]+=coefficient
    elif g==4:
        w=csv2['entre 30 et 40 (forfait)']
        for dieu in range(0,len(w)):
            for diable in range(0,o):
                valeur=nom_stations[diable]
                if w[dieu]==nom_stations[diable]:
                    dictionnaire[valeur]+=coefficient
    elif g==5:
        w=csv2['entre 40 et 50 (forfait)']
        for dieu in range(0,len(w)):
            for diable in range(0,o):
                valeur=nom_stations[diable]
                if w[dieu]==nom_stations[diable]:
                    dictionnaire[valeur]+=coefficient
    elif g==6:
        w=csv2['superieur Ã\xa0 50 (fortfait)']
        for dieu in range(0,len(w)):
            for diable in range(0,o):
                valeur=nom_stations[diable]
                if w[dieu]==nom_stations[diable]:
                    dictionnaire[valeur]+=coefficient
    print("Quel niveau de ski souhaiter vous avoir ?"+"\n tapez 1 si vous souhaitez un niveau débutant (majorité de piste verte et bleu)"+"\n tapez 2 si vous souhaitez un niveau intermediaire( majorité de piste bleu et rouge et quelque noir)"+"\n tapez 3 si vous souhaitez un bon niveau (majorité de piste rouge ou noir en plus de bonne piste verte et bleu)")
    h=int(input("votre choix : "))
    coefficient=int(input("votre nombre associé à cette caractéristique :"))
    if h==1:
        w=csv2['dÃ©butant']
        for dieu in range(0,len(w)):
            for diable in range(0,o):
                valeur=nom_stations[diable]
                if w[dieu]==nom_stations[diable]:
                    dictionnaire[valeur]+=coefficient
    elif h==2:
        w=csv2['intermediaire']
        for dieu in range(0,len(w)):
            for diable in range(0,o):
                valeur=nom_stations[diable]
                if w[dieu]==nom_stations[diable]:
                    dictionnaire[valeur]+=coefficient
    elif h==3:
        w=csv2['bon']
        for dieu in range(0,len(w)):
            for diable in range(0,o):
                valeur=nom_stations[diable]
                if w[dieu]==nom_stations[diable]:
                    dictionnaire[valeur]+=coefficient    
    # trier le dictionnaire par ordre décroissant de valeurs et stocker les stations dans une liste
    cles_triees = sorted(dictionnaire, key=dictionnaire.get, reverse=True)
    # afficher les 10 premières stations avec les plus grandes valeurs
    for i in range(10):
        print(cles_triees[i], dictionnaire[cles_triees[i]])
