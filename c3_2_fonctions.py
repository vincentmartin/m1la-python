# -*-coding:utf-8 -*
'''
Created on 13 mars 2014

@author: vincent

Cours 3. : Fonctions.
'''
#######################################
# 1. Définition et utilisation de fonctions.
#######################################

# Définition d'une fonction qui affiche bonjour.
# 0 paramètres, pas de valeur de retour.
def bonjour():
    '''Ceci est la documentation de la fonction (docstring)'''
    print "Bonjour"

# Utilisation
bonjour()

# Définition d'une fonction prenant un paramètre.
def bonjour_a_vous(nom):
    '''Fonction affichant bonjour suivi du nom.'''
    print "Bonjour " + nom
    
bonjour_a_vous("Toto")

#######################################
# 2. Valeur de retour.
#######################################

# Fonction retournant une valeur.
def retourner_bonjour_a_vous(nom):
    '''Fonction retournant bonjour suivi du nom.'''
    return ("Bonjour " + nom)

retourner_bonjour_a_vous("Tata")  # la fonction n'affiche rien, c'est normal, pas de 'print' dans la fonction.

# Récupération du retour de la fonction dans une variable.
texte = retourner_bonjour_a_vous("Tata")
print texte 


def retourner_bonjour_nom_prenom(prenom, nom):
    '''Fonction retournant bonjour suivi du nom.'''
    return ("Bonjour " + prenom + " " + nom)
texte = retourner_bonjour_nom_prenom("Franck", "Dupond")
print texte 


print "\n"
#######################################
# 3. Valeurs par défaut des paramètres
#######################################
def afficher_table_multiplication(n, debut=1, fin=9):
    '''Affichage d'une table de multiplication.'''
    compteur = debut
    while compteur <= fin:
        print str(n) + " * " + str(compteur) + " = " + str(n * compteur)
        compteur += 1

afficher_table_multiplication(2)  # multiplications de 2 par 1 jusqu'à 9
print "\n"
afficher_table_multiplication(2, 2)  # multiplications de 2 par  2 jusqu'à 9
print "\n"
afficher_table_multiplication(2, fin=15)  # multiplications de 2 par 1 jusqu'à 15

print "\n"
#######################################
# 4. Attention aux types des paramètres.
#######################################

# Le programme plante si la ligne suivante est décommentée.
#texte = retourner_bonjour_nom_prenom(2, "Dupond") 


def retourner_bonjour_nom_prenom2(prenom, nom):
    '''Fonction retournant bonjour suivi du nom.'''
    if type(prenom) != str or type(nom) != str:
        print "Les paramètres nom et prenom doivent etre de type string (str)"
    else:
        return ("Bonjour " + prenom + " " + nom)

# Le programme ne plante plus et affiche l'erreur à l'utilisateur. 
# Nous verrons par la suite une façon plus élégante d'attraper les erreurs par la gestion des exceptions.
texte = retourner_bonjour_nom_prenom2(2, "Dupond")


print "\n"
#######################################
# 5. Utilisation d'une fonction dans une autre fonction.
#######################################

# Définition d'une première fonction.
def verifier_parametres(p1, p2):
    '''Fonction vérifiant que les paramètres soient bien de type string (str)'''
    if type(p1) != str or type(p2) != str:
        return False
    return True

# Puis utilisation dans la seconde.
def retourner_bonjour_nom_prenom3(prenom, nom):
    '''Fonction retournant bonjour suivi du nom.'''
    params_ok = verifier_parametres(prenom, nom) # appel de la fonction verifier_parametres
    if params_ok == False:
        print "Les paramètres nom et prenom doivent etre de type string (str)"
    else:
        return ("Bonjour " + prenom + " " + nom)

print retourner_bonjour_nom_prenom3("Marie", 8)
print retourner_bonjour_nom_prenom3("Marie", "Durand")