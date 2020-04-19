# fragmenty dotyczące rozwiązania poszczególnych zadań proszę oddzielić odpowiednimi komentarzami

#Zad2.------------------------------------

from array import *

lista = array('u', [])
znaki = input("Podaj znaki: ")

i = 0
while i < len(znaki):
    lista.append(znaki[i])
    i += 1

print("Podane znaki w odwrotnej kolejnosci: ", end="")
lista.reverse()
i =0
while i < len(lista):             #wypisanie znaków
    print(lista[i], end="")
    i += 1
print()

#Zad3.-----------------------------------------

import random
from array import array

lista = array('i', [])
for i in range(5):
    lista.append(random.randint(-5,5))
plik = open("result.txt","w")
i = 0
while i < len(lista):
    plik.write(str(lista[i]) + " ")
    i += 1

plik.close()

#Zad4.---------------------------------------------

import numpy as num


def funkcja():
    lista = num.array(
        [[2, 3, 4, 5, 6], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])  
    i = 1
    while i < 5:
        for j in range(5):
            lista[i][j] = pow(lista[i - 1][j], 2)                                                   
        i += 1
    return lista

print(funkcja())

