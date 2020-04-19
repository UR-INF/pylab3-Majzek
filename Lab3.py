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

#Zad5.---------------------------------------------

import collections

def histogram(nazwa):
    plik = open(nazwa,"r")
    text = plik.readline()
    c = collections.Counter(text)
    return c

print(histogram("dokument.txt"))

#Zad6.---------------------------------------------

import random


def deck():
    deck = [('2', 'c'), ('2', 'd'), ('2', 'h'), ('2', 's'), ('3', 'c'), ('3', 'd'), ('3', 'h'), ('3', 's'),
            ('4', 'c'), ('4', 'd'), ('4', 'h'), ('4', 's'), ('5', 'c'), ('5', 'd'), ('5', 'h'), ('5', 's'),
            ('6', 'c'), ('6', 'd'), ('6', 'h'), ('6', 's'), ('7', 'c'), ('7', 'd'), ('7', 'h'), ('7', 's'),
            ('8', 'c'), ('8', 'd'), ('8', 'h'), ('8', 's'), ('9', 'c'), ('9', 'd'), ('9', 'h'), ('9', 's'),
            ('10', 'c'), ('10', 'd'), ('10', 'h'), ('10', 's'), ('J', 'c'), ('J', 'd'), ('J', 'h'), ('J', 's'),
            ('D', 'c'), ('D', 'd'), ('D', 'h'), ('D', 's'), ('K', 'c'), ('K', 'd'), ('K', 'h'), ('K', 's'),
            ('A', 'c'), ('A', 'd'), ('A', 'h'), ('A', 's')]
    return deck


def shuffle_deck(deck):
    random.shuffle(deck)
    return deck


def deal(deck, n):
    lista = []
    shuffled_deck = shuffle_deck(deck)
    x = 0
    for i in range(n):
        for j in range(5):
            lista.append(shuffled_deck[x])
            x = x + 1

    return lista


print(deal(deck(), 5))
