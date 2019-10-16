# -*- coding: utf-8 -*-
## 1\.Exercice 1 : Hello World
print("\nExercise Nr. #1")
print("---------------")

print("Hello World")

Macron =  "hello world"

print(Macron)

## 2\.Exercice 2 : Calculs divers
print("\nExercise Nr. #2")
print("---------------")

print(3*3)
try:
    12/0
except ZeroDivisionError:
    print("Null division not allowed")
print(4+9+78)
print(12-7)
print(5e4)

## 3\.Exercice 3 : Communiquer avec l'ordinateur
print("\nExercise Nr. #3")
print("---------------")

name = input("Who should I introduce ? ")
print("Hi",name,", welcome on board!".format(name))

## 4\.Exercice 4 : Nom et prénom
print("\nExercise Nr. #4")
print("---------------")

name = "Vladimir"
familyname = "Illitch"
print("Bonjour {} {}".format(name,familyname))

## 5\.Exercice 5 : Des caractères au nombre
print("\nExercise Nr. #5")
print("---------------")

myNumber = "123"
print(myNumber)
print(type(myNumber))
myNumber = int(myNumber)
print(myNumber)
print(type(myNumber))

## 6\.Exercice 6 : Majuscules et miniscules
print("\nExercise Nr. #6")
print("---------------")

myMAJString = "ALEA JACTA EST"
print(myMAJString.lower())
myminString = "alea jacta est"
print(myminString.upper())
