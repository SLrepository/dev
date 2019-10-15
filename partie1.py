# -*- coding: utf-8 -*-
## 1\.Exercice 1 : Hello World
print("Hello World")

Macron =  "hello world"

print(Macron)

## 2\.Exercice 2 : Calculs divers
print(3*3)
try:
    12/0
except ZeroDivisionError:
    print("Null division not allowed")
print(4+9+78)
print(12-7)
print(5e4)

## 3\.Exercice 3 : Communiquer avec l'ordinateur
name = input("Who should I introduce ? ")
print("Hi",name,", welcome on board!".format(name))

## 4\.Exercice 4 : Nom et prénom
name = "Vladimir"
familyname = "Illitch"
print("Bonjour {} {}".format(name,familyname))

## 5\.Exercice 5 : Des caractères au nombre
myNumber = "123"
print(myNumber)
print(type(myNumber))
myNumber = int(myNumber)
print(myNumber)
print(type(myNumber))

## 6\.Exercice 6 : Majuscules et miniscules
myMAJString = "ALEA JACTA EST"
print(myMAJString.lower())
myminString = "alea jacta est"
print(myminString.upper())
