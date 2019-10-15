# -*- coding: utf-8 -*-
## 1\.Exercice 1 : True ou False ?
str1 = "La Mort n'est rien"
str2 = ""
print(len(str1)==0)
print(len(str2)==0)

## 2\.Exercice 2 : Calculer mon âge
currentYear = input("Current Year ?")
yearOfBirth = input("Year of Bith ?")

currentYear = int(currentYear)
yearOfBirth = int(yearOfBirth)

if((currentYear > 2019) or (yearOfBirth > 2019)):
    print("We are not yet there!")
else:
    your_age = currentYear - yearOfBirth
    print("Your age", your_age)

## 3\.Exercice 3 : Problème de chaussures
