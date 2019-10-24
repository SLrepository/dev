# -*- coding: utf-8 -*-
## 1\.Exercice 1 : Un échiquier
print("\nExercice 1 : Un échiquier")
line = "# # # # # # # #"
blanc = " "

print("```")
print("  \"")
for i in range(0, 8):
    if i%2 == 0:
        print("   {}{}".format(line, blanc))
    else: 
        print ("   {}{}".format(blanc, line)) 
print("  \"")
print("```")      

## 2\.Exercice 2 : Matrix dans le terminal
print("\nExercice 2 : Matrix dans le terminal")
L = [0,0,0,0]
var1=0; var2=0; var3=0; var4=0; var5= "-------"
print("```")
for i in range(0, 4):
    L[i] = 1
    var1 = L[0]
    var2 = L[1]
    var3 = L[2]
    var4 = L[3]
    print("{}\n{}\n{}\n{}\n{}".format(var1,var2,var3,var4,var5))
    L[i] = 0
print("```")

## 3\.Exercice 3 : Nombre paire ?
print("\nExercice 3 : Nombre paire ?")

def evenYesNo(number):
    number = int(number)
    print(not(number%2))

user = input("Entrez votre montant ? ") 
if "." in user:
    user=float(user)
else:
    user=int(user)
evenYesNo(user) 

## 4\.Exercice 4 : Vous avez dit factorielle ?
print("\nExercice 4 : Vous avez dit factorielle ?")

def fact(n):
    """fact(n): calcule la factorielle de n (entier >= 0)"""
    x=0
    if "." in n:
        print("Pas un nombre enier")
    else:
        n=int(n)
        if n == 0:
            x=0
        else:
            x=1
            for i in range(2,n+1):
                x*=i
    return x

nb= input("Entrez un nombre entier : ")
print("Resultat = ",fact(nb))

## 5\.Exercice 5 : Les tirets ça compte !
print("\nExercice 5 : Les tirets ça compte !")

def convertHyphenintoUnderscore1(theString):
    try:
        isNB = float(theString)
        if float(isNB):
           myReturn = "Ceci est un nombre"
    except:
        if "-" in theString:
            i=0
            while "-" in theString:
                if theString[i] == '-':
                    break
                i+=1
            myReturn = theString[:i]+'\_'+theString[i+2:]
        else:
            myReturn = theString
    return(myReturn)


def convertHyphenintoUnderscore2(theString):
    return(theString.replace('-','\_'))

myString = input("Entrez votre ligne de facturation : ")
string2 = myString
print(convertHyphenintoUnderscore1(myString))
print(convertHyphenintoUnderscore2(string2))



## 6\.Exercice 6 : Entraînez-vous avec les tableaux
print("\nExercice 6 : Entraînez-vous avec les tableaux")


listeDeCourse =["jambon","pain","fromage","cumin"]
print("Vous devez acheter du {}".format(listeDeCourse[0]))
print("Mais aussi du {}".format(listeDeCourse[-1]))
print("Et également du {}".format(listeDeCourse[2]))

## 7\.Exercice 7 : Le tableau d'un homme
print("\nExercice 7 : Le tableau d'un homme")
# 
ecce_homo = [["\nvladimir", "poutine", "7 Octobre 1952", "67 ans"],["\nvladimir", "ilitch", "21 Janvier 1924", "53 ans"],["\nvladimir", "cosma", "13 Avril 1940", "79 ans"]]

def showTheMan(details):
    print("\n")
    for j in range(len(details)):
        for i in range(len(details[j])):
            print(details[j][i])

def showList(theList):
    for List in theList:
        for inlist in List:
            print(inlist)

showTheMan(ecce_homo)
showList(ecce_homo)

## 8\.Exercice 8 : Le max d'un tableau
print("\nExercice 8 : Le max d'un tableau")

mylist = [123,52,67,256,10]
mylist2 = ["AA","AAA","AAA","AAAAA","AAAA"]
mylist3 = ["GNU", 125, "Frei", 1048]

def findMax(array):
    try:
        print(max(array))
    except:
        print("You are going completely bersek, this is just:")
        print(False)

findMax(mylist)
findMax(mylist2)
findMax(mylist3)



## 9\.Exercice 9 : Une to do list
print("\nExercice 9 : Une to do list")

myToDoList = []

while True:
    myTask = input("Please enter your task (type \"fin\" to exit) ")
    if "fin" in myTask:
        break
    myToDoList.append(myTask)

for i in range(len(myToDoList)):
    print(myToDoList[i])




