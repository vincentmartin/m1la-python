# -*-coding:utf-8 -*
'''
Created on 19 févr. 2014
@author: vincent

Cours 2. : les bases du langages.
'''
#######################################
# 1. Types de données
#######################################

# Cest le premier bout de code que vous voyez ! Les langages de programmation récents, dont python, sont construits pour être compréhensibles, même par un non expert.
# Le code ci-dessous parle de lui même.
print 3, -4
print 3.14, -6.2

print '\n' 

print str((3, 4)) + " sont deux nombres entiers. Leur type est int()"
print str((3.14, -6.2)) + " sont deux nombres flottants. Leur type est 'float()'"  # Ça peut faire peur au début mais ça signifie juste un nombre réel, ou nombre à virgule si vous préférez"


print '\n' 

# Python est un langage 'FORTEMENT TYPÉ', c'est à dire que chaque donnée a un type et que tout changement de type nécessite une conversion explicite.
print type(4)
print type(3.15)
print type("Hello ! ")
print "\n"
# ... et Python dispose d'un typage dynamique, c'est à dire que le type d'un objet est déterminé à l'exécution 
# et sans que le programmeur n'ait à spécifier explicitement le type (contrairement à SQL).

# Liste des types de données : http://docs.python.org/2/library/datatypes.htmlprint float(3)


# EXO2 : quelle est le type de 4.0 ?
# C'est à vous ?print float(3)


#######################################
# 2. Transtypage (conversion explicite de type)
#######################################

print int(3.5)
# EXO3: Expliquez le résultat. Quel est le type du résultat ? 
# C'est à vous

# EXO4. : Expliquez à quoi sert 'str' (cf. 1.)
# C'est à vous !

print "\n"
#######################################
# 3. Expressions arithmétiques. 
#######################################
# Opérateurs 
# +
# -
# *
# /
# **    puissance

# EXO5. Pour chaque opérateur, affichez le résultat d'une opération de votre choix.
# C'est à vous

print 1 / 3
print 1.0 / 3
print 1 / 3.0
print "\n"
# Si les deux opérandes sont de type int(), le résultat sera aussi de type int() (entier), arrondi. 0.333 arrondi = 0.
# Si au moins une des deux opérande est de type float(), le résultat sera de type float().

# Une expression arithmétique est un nombre (e.g. 2) ou un opérateur appliqué à deux expressions arithmétiques (e.g. : 2 + 3)
print 1 # est une expression airthmétique.
print -6 # est une expression airthmétique.
print 1 + 5 * 8 - 8 # est une expression arithmétique.
print "\n"
 
#######################################
# 3. Priorité des opérateurs.
####################################### 

# ASTUCE pour se souvenir des priorités : 
# "Please Excuse My dear Aunt Sallie" = (), **, *, /, +, -

# EXO6 : Pour chacune des expressions arithmétque suivante, donnez l'ordre des opérateurs
print 7+3*4
print (7+3)*4
print (15//2)**3*5
print 0b101*2

# Utilisez les parenthèses si vous doutez !
