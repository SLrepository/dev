# -*- coding: utf-8 -*-
import math

## 1\.Exercice 1 : Le nombre le plus grand
print("\nExercice 1 : Le nombre le plus grand")
nb_1 = 3; nb_2 = 8; nb_3 = 23; nb_4 = 64
myList = [nb_1, nb_2, nb_3, nb_4]
print(max(myList))

## 2\.Exercice 2 : Conditon d'âge
print("\nExercice 2 : Conditon d'âge")

try:
   Age = int(input("Quel est votre âge ? "))

   if Age <= 0:
           print("Entrez votre âge réel ")
   if Age >= 21:
           print("Bonne nouvelle, l'accés vous est autorisé")
   if Age%2 == 0:
           print("Encore une bonne nouvelle, votre âge est pair")
   if math.sqrt(Age).is_integer():
           print("Bingo ! votre âge est un carré")

except ValueError:
   print("petit canaillou, tu ne m'auras pas ;)")

## 3\.Exercice 3 : Le nombre caché
print("\nExercice 3 : Le nombre caché")

Nombre_caché = 25
User = int(input("Quel est le nombre caché ? "))
while Nombre_caché != User:
   if User > Nombre_caché:
       print("Votre nombre est trop grand")
       User = int(input("Recommencez "))
   if User < Nombre_caché:
       print("Votre Nombre est trop petit")
       User = int(input("Recommencez "))
   if User == Nombre_caché:
       print("Bien joué vous avez trouvé le nombre caché !")
if User == Nombre_caché:
   print("bravooooo!!!")

## 4\.Exercice 4 : Des nombres en boucle
print("\nExercice 4 : Des nombres en boucle")

input("Appuyez sur ENTER/ENTRÉE")
for x in range(101):
   print(x)

## 5\.Exercice 5 : Des nombres en boucle bis
print("\nExercice 5 : Des nombres en boucle BIS")

for x in range(101):
   if x%2 == 0:
       print(int(x), "Ce nombre est pair")

## 6\.Exercice 6 : Remplir la piscine
print("\nExercice 6 : Remplir la piscine")

def pool_filing(long, larg, prof, debit):
   filing_time = (long*larg*prof)/debit
   print("time of filing is {} minutes".format(filing_time))

pool_filing(9, 9, 9, 9)

## 7\.Exercice 7 : Calcul de cercle
print("\nExercice 7 : Calcul de cercle")
def Périmètre(rayon):
   périmètre = round((2*math.pi*rayon), 2)
   print("votre cercle a un périmètre de {} cm".format(périmètre))

def Aire(rayon):
   aire = round((math.sqrt(rayon)*math.pi), 2)
   print("Votre cercle a une aire de {} cm carré".format(aire))

rayon = int(input("Quel est le rayon de votre cercle ? "))
Périmètre(rayon)
Aire(rayon)

## 8\.Exercice 8 : Une pyramide
print("\nExercice 8 : Une pyramide")

Var_0 = "```"
Var_1 = "\n"
Var_2 = ""
for i in range(1, 6):
   if i == 1:
       Var_1 = Var_0 + Var_1
   else:
       Var_2 += "*"
       Var_1 += Var_2 + "\n"
print(Var_1 + Var_0)

## 9\.Exercice 9 : FIZZ BUZZ
print("\nExercice 9 : FIZZ BUZZ")
fizbuz = ""
for i in range(1, 101):
   if i%3 == 0:
       fizbuz = "FIZZ"
       if i%5 == 0:
           fizbuz = "FIZZBUZZ"
   elif i%5 == 0:
       fizbuz = "BUZZ"
   print("{} - {}".format(i, fizbuz))
   fizbuz = ""
   