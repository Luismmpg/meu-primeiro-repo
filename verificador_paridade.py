# -*- coding: utf-8 -*-
"""
Created on Mon May 29 22:18:13 2023

@author: luism
"""

## Atividades Pedagógicas em Grupo - Exercício 2

print("Considera-se uma pessoa honesta? ")
caracteristica_1 = input("Resposta: ")
car_minusc1 = caracteristica_1.lower()
print("Já bateu em alguém de forma gratuita? ")
caracteristica_2 = input("Resposta: ")
car_minusc2 = caracteristica_2.lower()
print("Gosta de ananás na pizza? ")
caracteristica_3 = input("Resposta: ")
car_minusc3 = caracteristica_3.lower()

if car_minusc1=="sim" and car_minusc2=="não" and car_minusc3=="não":
    print("Você é um super-heroi!!")
elif car_minusc1=="sim" and car_minusc2=="não" and car_minusc3=="sim":    
    print("Você é um super-heroi, mas a pizza come-se sem ananás!!!")
# utilizámos a opção and e or porque no fundo a questão da pizza não é importante
elif car_minusc1=="sim" and car_minusc2=="sim" and car_minusc3=="sim" or car_minusc3=="não": 
    print("Você está a caminho de ser um super-heroi, mas não pode bater nas pessoas!!")
else:
    print("Você é claramente um vilão!")