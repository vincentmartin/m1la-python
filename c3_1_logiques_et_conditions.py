# -*-coding:utf-8 -*
'''
Created on 4 mars. 2014
@author: vincent

Cours 3. : Structures de contrôle et fonctions.
'''
#######################################
# 4. Expressions logiques (booléennes)
#######################################

# LA VALEUR D'UNE EXPRESSION LOGIQUE BOOLENNE NE PEUT PRENDRE QUE 2 VALEURS :
#   VRAI ou FAUX (true false)
# 3 opérateurs : NOT, AND, OR

# 4.1. NOT

# Table de vérité (T = True ; F = False)
# --------------
#  X   | NOT(X)
#+------------+
#   T  |  F
#   F  |  T
#      +
a = True
print "a=" + str(a)
print "not(a)=" + str(not(a))

b = False
print "b=" + str(b)
print "not(b)=" + str(not(b))

# Exemples parlants
ilFaitBeauAujourdhui = True  # j'ai le droit d'appeler ma variable comme ça ;)
print "ilFaitBeauAujourdhui=" + str(ilFaitBeauAujourdhui)
print "not(ilFaitBeauAujourdhui)=" + str(not(ilFaitBeauAujourdhui))


# 4.2. OR

# Table de vérité

#   +   +   
# X | Y | X OR Y
#+--|---|-----------+
# T | T | ? 
# F | F | ? 
# T | F | ?  
# F | T | ?  

# EXO 1: À l'aide du langage Python, déterminez la table de vérité de l'opérateur booléen OR
# en créant deux variables booléennes et en testant les 4 possibilités.


# 4.3. AND

# Table de vérité

#   +   +   
# X | Y | X AND Y
#+--|---|-----------+
# T | T | ? 
# F | F | ? 
# T | F | ?  
# F | T | ?  

# EXO 2: À l'aide du langage Python, déterminez la table de vérité de l'opérateur booléen AND
# en créant deux variables booléennes et en testant les 4 possibilités.

# 4.3 Expressions booléennes complexes
c = (False and True) and (True and not(False)) 
# EXO 3: quelle est la valeur de c ? Vérifiez en utilisant print.

print "\n"
#######################################
# 4. Opérateurs de comparaison
#######################################

# Opérateurs disponibles
# >     strictement supérieur
# <     strictement inférieur
# >=    supérieur ou égal
# <=    inférieur ou égal
# ==    égalité
# !=    non égalité 

# Le résultat d'une comparaison est soit vraie soit faux.

age = input("Entrez votre age : ")
print "Age > 18 ? " + str(age > 18)
print "Age < 60 ? " + str(age < 60)
print "Age == 24 ? " + str(age == 24)
print "Age différent de 24 ? " + str(age != 24)

print '\n'
#######################################
# 5. Structures conditionnelles.
#######################################

# if, elif, else

if age >= 12 and age <= 25: 
    print "Vous avez droit à la carte 12-25"
elif age >= 60:
    print "Vous avez droit à la carte senior (60+)"
elif age == 100:
    print "Vous avez droit à la carte 'Tout gratos' !"
else:
    print "Vous n'avez droit à rien du tout !!!"

# IMPORTANT : notez les tabulations. Elles permettent de délimiter les blocs d'instruction à exécuter en fonction de la condition. 
# Les blocs sont créés par les instructions de contrôles : if, elif, else, while, for.
