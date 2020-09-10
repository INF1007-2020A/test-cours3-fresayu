#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    liste_de_caractere = [chr(ord(lettre)-32) if lettre.islower() else lettre for lettre in mot]

    return "".join(liste_de_caractere)


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
