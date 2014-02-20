# -*-coding:utf-8 -*
'''
Created on 19 févr. 2014
@author: vincent

Cours 2. : les bases du langages.
'''
#######################################
# 1. Variables
#######################################

# Une variable est une "boite" avec un nom dans laquelle on va ranger une donnée.
#+-------------+  +-------------+
#|    toto     |  |    tata     |
#|-------------|  |-------------|
#|             |  |             |
#|     15      |  |  "Bonjour !"|
#|             |  |             |
#+-------------+  +-------------+

# Affectation d'une variable
var1 = 3 # définition de la variable 'var1' puis affectation (avec le signe égal) de la valeur 3
print var1
var2 = 5
print var2


# Définition d'une variable et affectation d'une valeur
variable = "Valeur !"

# Nom de variable : lettres, nombres, underscores. Le nom d'une variable ne peut PAS commencer par un chiffre.
# Sensibles à la casse
a = 75
A = 35
print A, a
print '\n'

# EXO1. : Définissez les variables toto et tata. Quel est leur type ?

# Les variable se manipulent comme n'importe quelle autre données !
# Tout ce qu'il y a à DROITE du signe égal (affectation) est EVALUÉ avant l'affectation.
age = 24
print age
age = age + 1  # python calcul (age + 1) puis affecte le résultat à la variable age.
print age
age += 1 # Identique à age = age +1

# EXO2. : Conversion Fahrenheit -> Celsius : en utilisant http://fr.wikipedia.org/wiki/Fahrenheit, convertissez la température suivante en °C.
degre_farenheit = 176 
# C'est à vous

# EXO3. À partir de la température en °C., calculez la température en °F.