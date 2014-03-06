# -*-coding:utf-8 -*
'''
Created on 19 févr. 2014
@author: vincent

Cours 2. : les bases du langage.
'''
#######################################
# 1. Variables
#######################################

# Une variable est une "boite" avec un nom dans laquelle on va ranger une donnée.
#+-------------+  +-------------+
#|    b1       |  |    b2       |
#|-------------|  |-------------|
#|             |  |             |
#|     15      |  |  "Bonjour !"|
#|             |  |             |
#+-------------+  +-------------+
b1 = 15
b2 = "Bonjour"

# Affectation d'une variable
var1 = 3 # définition d'IDENTIFICATEUR 'var1' puis affectation (avec le signe égal) de la valeur 3
print var1
var2 = 5
print var2

# Définition d'une variable et affectation d'une valeur
variable = "Valeur !"

# Nom de variable : lettres, nombres, underscores. Le nom d'une variable ne peut PAS commencer par un chiffre.
# Sensible à la casse.
a = 75
A = 35
print A, a
print '\n'

# EXO1. : Définissez les variables b1 et b2 (cf. plus haut). Quel est leur type ?
# C'est à vous.

#######################################
# 2. Variables et mémoire.
#######################################

# Une variable fait REFERENCE à l'adresse d'une case mémoire. Elle est définie par
# - son nom (identificateur) ;
# - sa valeur : la donnée stockée dans la case mémoire ;
# - son adresse : l'adresse de la case mémoire ;
# - son type : décrit la nature de la structure de la donnée stockée en mémoire.

# Pour être manipulées, les valeurs des variables sont stockées en mémoire vive. 
# La mémoire centrale est organisée en CASE MEMOIRES qui sont accessibles via des ADRESSES.

# Illustration
#         Mémoire centrale
#         +--------------+
#         |              |
#         +--------------+
#adresse 2|      1       |
#         +--------------+
#adresse 3|     True     |
#         +--------------+
#adresse 4|     2.3      |
#         +--------------+
#adresse 5|  "Hello !"   |
#         +--------------+
#         |    ....      |
#         +--------------+

# id() permet d'obtenir l'adresse d'une variable.
a = 1
print id(a)

# EXO 2. : testez les instruction suivantes et commentez...
a = 1
print a
b = 2
print b
a = b
print a
print id(a)
print id(b)

# EXO 3. : Testez les instructions suivantes et représenter graphiquement la mémoire
a = int(input())
a = a + 2
b = 4
y = b
a = 2 * y +a
b == 3
z = a = b

print "\n"


#######################################
# 3. Manipulation de variables
#######################################

# Les variables se manipulent comme n'importe quelle autre donnée !
# Tout ce qu'il y a à DROITE du signe égal (affectation) est EVALUÉ avant l'affectation.
age = 24
print age
age = age + 1  # python calcule (age + 1) puis affecte le résultat à la variable age.
print age
age += 1 # Identique à age = age +1

# EXO2. : Conversion Fahrenheit -> Celsius : en utilisant http://fr.wikipedia.org/wiki/Fahrenheit, convertissez la température suivante en °C.
degre_farenheit = 176 
# C'est à vous

# EXO3. À partir de la température en °C., calculez la température en °F.