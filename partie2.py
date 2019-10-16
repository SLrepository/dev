# -*- coding: utf-8 -*-
## 1\.Exercice 1 : True ou False ?
print("\nExercise Nr. #1")
print("---------------")
str1 = "La Mort n'est rien"
str2 = ""
print(len(str1)==0)
print(len(str2)==0)

## 2\.Exercice 2 : Calculer mon âge
print("\nExercise Nr. #2")
print("---------------")
currentYear = input("Current Year ? ")
yearOfBirth = input("Year of Bith ? ")

currentYear = int(currentYear)
yearOfBirth = int(yearOfBirth)

if((currentYear > 2019) or (yearOfBirth > 2019)):
    print("We are not yet there!")
    exit(0)
else:
    if(yearOfBirth > currentYear):
        print("You already live in the futur")
        exit(0)
    else:
        your_age = currentYear - yearOfBirth
        print("Your age", your_age)

yearOfBirthNextToYou = input("This mate Year of Birth ? " )
yearOfBirthNextToYou = int(yearOfBirthNextToYou)

if(yearOfBirthNextToYou > 2019):
    print("We are not yet there!")
    exit(0)
else:
    if(yearOfBirthNextToYou > currentYear):
            print("You already live in the futur")
            exit(0)
    else:
        cumulated_age = currentYear - yearOfBirthNextToYou
        print("Your mate age", cumulated_age)
        cumulated_age += your_age
        print("Your cumulated age", cumulated_age)

## 3\.Exercice 3 : Problème de chaussures
print("\nExercise Nr. #3")
print("---------------")

shoes = 70
levis = 59
tshirt = 20

total = shoes+levis+tshirt
print("Total avant réduction : {}€".format(total))
bargain = total * 0.2
total = total - bargain
print("Total après réduction : {}€".format(total))

## 4\.Exercice 4 : une calculatrice Python
print("\nExercise Nr. #4")
print("---------------")
operand1 = input("Nombre1 ? ")
operand2 = input("Nombre2 ? ")

if "." in operand1:
    operand1=float(operand1)
else:
    operand1=int(operand1)

if "." in operand2:
    operand2=float(operand2)
else:
    operand2=int(operand2)

sum = operand1+operand2

print("sum = {}".format(sum))


## 5\.Exercice 5 : travailler avec les propriétés
print("\nExercise Nr. #5")
print("---------------")

family_name = input("Hey what's your family name ? ")
name = input("And what's your name ? ")

Fn_prefix = family_name[0].upper()
Fn_suffix = family_name[len(family_name)-1].upper()

n_prefix = name[0].upper()
n_suffix = name[len(name)-1].upper()

print("Short family name: {}{}".format(Fn_prefix,Fn_suffix))
print("Short name: {}{}".format(n_prefix,n_suffix))

print("Combined short name: {}{}{}{}".format(Fn_prefix,Fn_suffix,n_prefix,n_suffix))

age = input("Hey what's your age ? ")
age = int(age)/33
age = int(age)
print("Your age / 33 is {}".format(age))
