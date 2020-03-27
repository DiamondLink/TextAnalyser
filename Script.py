#-*-coding:UTF-8 -*
import os
from math import *
voyelle=0
consonne=0
autre=0
le_tout=0
nb_letrres={}
le_tout=0
le_tout_lettre=0
creation_nb_lettre="abcdefghijklmnopqrstuvwxyz"

for element in creation_nb_lettre:
    nb_letrres[element]=0

def arrondir(nombre):
    if nombre-floor(nombre)<ceil(nombre)-nombre:
        nombre=floor(nombre)
    else:
        nombre=ceil(nombre)

    return(nombre)


with open("Source.txt","r") as fichier:
    text=fichier.read()

text=str(text)
for element in text:
    if element=="é" or element=="è" or element=="ê":
        nb_letrres["e"]+=1
    if element=="à" or element=="â":
        nb_letrres["a"]+=1
    if element=="ç":
        nb_letrres["c"]+=1
    if element=="ù":
        nb_letrres["u"]+=1
    element=element.lower()
    if element in "aeiouyéèàùôêâ":
        voyelle+=1
    elif element in "bcdfghjklmnpqrstvwxz":
        consonne+=1
    else:
        pass
        #if element!=" " and element!="\n" and element!="	":
            #autre+=1

    if element in nb_letrres:
        for truc in nb_letrres:
            if element==truc:
                nb_letrres[truc]+=1 


le_tout=voyelle+consonne+autre
for element in creation_nb_lettre:
    le_tout_lettre+=nb_letrres[element]

le_tout_lettre+=autre


if le_tout==0:
    print("Le fichier source est vide")

else:
    print("""Le fichier source contient {} voyelle(s), {} consonne(s) et {} autre(s) caractère(s).

            Voici les proportions:  - {} % de voyelle
                                    - {} % de consonne
                                    - {} % d'autre caractère
                                    
                                    """.format(voyelle,consonne,autre,arrondir(voyelle*(100/le_tout)),arrondir(consonne*(100/le_tout)),arrondir(autre*(100/le_tout))))

    print("""Voici les lettres présente(ent) dans le fichier source:
    """)
    for element in nb_letrres:
        if nb_letrres[element]!=0:
            print("""{} : {}""".format(element,nb_letrres[element]))

    print("""
Voici les proportions de ces lettres :
    """)
    for element in nb_letrres:
        if nb_letrres[element]!=0:
            print("""  - {} % de {} """.format(nb_letrres[element]*(100/le_tout_lettre),element))#.format(arrondir(nb_letrres[element]*(100/le_tout_lettre)),element))

with open("output.txt","w") as f:
    for element in nb_letrres:
        try:
            variable_intermediaire=str(element)+":"+str(nb_letrres[element]*(100/le_tout_lettre))+"\n"
            variable_intermediaire=str(variable_intermediaire)
            f.write(variable_intermediaire)
        except:
            pass
os.system("pause")                           




    
