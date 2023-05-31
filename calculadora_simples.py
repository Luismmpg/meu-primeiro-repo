# -*- coding: utf-8 -*-
"""
Created on Mon May 29 21:35:56 2023

@author: luism
"""

# Atividades Pedagógicas em Grupo - Exercício 1


fruta = input("Escreva aqui a futa: ")
quantidade_texto = input("Qual a quantidade? ")
quantidade_numero = int(quantidade_texto)

if fruta == "maçãs":
    valor = 1
    print(quantidade_numero*valor)
elif fruta == "bananas":
    valor = 2
    print(quantidade_numero*valor)    
elif fruta == "laranjas":
    valor = 3.5
    print(quantidade_numero*valor)    
else:
    print("Sem stock de momento!")
    