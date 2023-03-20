# Variables

name = input("Wie heißt du?: ")
age = int(input("Wie alt bist du?: "))
height = float(input("Wie hoch bist du?: "))

print("Hello "+name)
print("Du bist "+str(age)+" Jahre alt")
print("Du bist "+str(height)+"cm hoch")

# Statements for age

if age == 100:
    print("Du bist 100 Jahre alt!")
if age > 100:
    print("Wow sehr beeindruckend!")
elif age >= 18:
    print("Du bist erwachesn!")
elif age < 0:
    print(":O")
else:
    print("Du bist noch nicht erwachsen!")

# Sleep timer between input

import time
print("Zeit für das nächste Thema...")
time.sleep(7)
print("Zeit für Mathe!")

# Variables 

answer = int(input("Was sind die ersten 2 Nachkommastellen von π? "))

# Statements for answer

if answer == 14:
    print("Sehr gut!")
if answer == 141:
    print("Die ersten 2 Nachkommastellen!")
    
import time
print("Wie berechne ich die Hypotenuse eines Dreiecks? ")
time.sleep(5)
print("Mithilfe von Python! ")

# Hypotenuse berechnen

from math import sqrt
print("Kürzere Seiten des Dreiecks eingeben: ")
a = float(input("a: "))
b = float(input("b: "))
c = sqrt(a**2 + b**2)
print("Die Länge der Hypotenuse ist: ", c )

import time
print("Das ist erstmals alles!")
time.sleep(5)
print("Ich hoffe es hat euch gefallen.")