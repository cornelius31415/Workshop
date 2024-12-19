#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 09:01:58 2024

@author: cornelius
"""



"""
                          Binäre Suche 
                          
                    Effizienter Suchalgorithmus um nach einem
                    Element in einer SORTIERTEN Liste zu suchen.
                    
                    Funktionweise:
                        1. Teilen
                            Wähle das mittlere Element aus und
                            teile die Liste in 2 Teillisten auf.
                        2. Vergleichen:
                           Wenn das gesuchte Element gleich dem
                           mittleren Element ist, dann bricht
                           der Algorithmus ab (Element gefunden)
                           
                           Wenn das gesuchte Element kleiner ist
                           als das mittlere, dann Fokus auf linke Hälfte
                           
                           Wenn das gesuchte Element größer ist
                           als das mittlere, dann Fokus auf rechte Hälfte
                           
                        3. Wiederholung
                           Schritte 1 und 2 werden so lange wiederholt,
                           bis das Element gefunden wurde.
                           
                           
                Schreibe eine Funktion, die ein Element mit Hilfe
                der binären Suche in einer sortierten Liste von
                Zahlen findet.
                liste = [1,2,3,4,5,6]
                Finde die Position der Zahl 4 mit binärer Suche.

"""


liste = [1,2,3,4,5,6,7]

def binarySearch(array, item):
    
    links = 0
    rechts = len(array)-1
    
    while links <= rechts:
        
        mitte = (rechts + links) // 2
        
        
        if array[mitte] == item:
            return mitte

        elif array[mitte] > item:
            rechts = mitte - 1
        
        else: 
            links = mitte + 1
            
    return None 
    
    
print(binarySearch(liste, 9))


print(9//2)


print("\n")





"""
                     Weihnachtliche Aufgabe 
                    
                                *
                               ***
                              *****
                                |
                                
                      Programmiere den obigen 
                      Weihnachtsbaum
                      
                      Ebene 0: 1 Stern
                      Ebene 1: 3 Sterne
                      Ebene 2: 5 Sterne
                      Ebene 3: 7 Sterne
                      
                      Formel: AnzahlSterne = 2*Ebene + 1
                      
                      Einrückungen:
                          Ebene 0: 3
                          Ebene 1: 2
                          Ebene 2: 1
                          Ebene 3: 0
                      
                          Formel: Einrückungen = hoehe - 1 - ebene  
"""



# def christmasTree(hoehe):

#     for ebene in range(0,hoehe):
#         print( " " * (hoehe-1-ebene)   + "*" * (2*ebene + 1))
    
#     print(" "*(hoehe-1) + "|")


# userInput = int(input("Bitte die Baumhöhe eingeben: "))

# christmasTree(userInput)











# zahl = 10

# for zahl in range(0,10):
#     ergebnis = zahl + 2
#     ergebnis = ergebnis ** 2
#     print(ergebnis)
    

# liste = ["a","b","c"]

# for buchstabe in liste:
#     print(buchstabe)
    

# for i in range(10):
#     print(i)

# for idx in range(10):
#     print(idx)



# alphabet = "qwertzuiopasdfghjklyxcvbnm"

# print(sorted(alphabet))















