# -*-coding:utf-8 -*
'''
Created on 10 mars. 2014
@author: vincent

Cours 3. : Itérations.
'''
# Le code suivant affiche la table de multiplication d'un nombre entré par l'utilisateur.
n = int(input("Quelle table de multiplication souhaitez-vous (1, 2, 3, ...) : "))
print "Table de multiplications de " + str(n)
print str(n) + " * 1 = " + str(n * 1)
print str(n) + " * 2 = " + str(n * 2)
print str(n) + " * 3 = " + str(n * 3)
print str(n) + " * 4 = " + str(n * 4)
print str(n) + " * 5 = " + str(n * 5)
print str(n) + " * 6 = " + str(n * 6)
print str(n) + " * 7 = " + str(n * 7)
print str(n) + " * 8 = " + str(n * 8)
print str(n) + " * 9 = " + str(n * 9)
print("\n")
# Ce code est répétitif ! Nous allons voir une méthode permettant de le réduire considérablement.

#######################################
# 1. Boucle while
####################################### 

# Les boucles permettent de répéter (itérer) un bloc d'instructions tant qu'une condition est remplie.
# Nous pouvons réécrire de façon plus condensée le code précédent à l'aide d'une boucle while.
print "Table de multiplications de " + str(n) + " en utilisant une boucle while"
compteur = 1
while compteur <= 9:
    print str(n) + " * " + str(compteur) + " = " + str(n * compteur)
    compteur += 1  # NE PAS OUBLIER SOUS PEINE DE BOUCLE INFINIE
print("\n")
# EXO1: Modifiez le code précédent pour afficher la table de multiplication jusqu'à 15.

#######################################
# 2. Boucle for
####################################### 

# La boucle for permet d'itérer sur les éléments d'une séquence.
# Ici nous itérons successivement sur les nombres 1, 2, ..., 9
print "Table de multiplications de " + str(n) + " en utilisant une boucle for"
for compteur in range(1, 10):  # 1, 2, ..., 9
    print str(n) + " * " + str(compteur) + " = " + str(n * compteur)
print("\n")



#######################################
# 3. Mots-clés break et continue
####################################### 

# Le mot clé break permet d'arrêter la boucle courante.
for i in range(0, 10):  # 0, 1, ..., 9
    if i == 5:
        break
    print i

# Le mot clé continue permet de revenir au début de la boucle courante sans exécuter la suite du bloc.
for i in range(0, 10):
    if i == 5:
        continue
    print i