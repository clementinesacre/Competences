from web import client as cl
from math import cos, sin, acos, pi
import re


def tous_pays():
    return cl.client_function("tous")


def un_pays(nom_pays):
    return cl.client_function("pays " + nom_pays)


def caracteristique_pays(liste_choix):
    """
    Permet de récupérer certaines informations de plusieurs pays (de 2 à 4 pays) .

    PRE : 'liste_choix' est une liste avec des pays ou des strings vides pour les 4 premiers indices, et le type
    d'information comme 5e paramètre.
    POST : Renvoie une dictionnaire contenant l'information, selon le type précisé, comme valeur et l'id du pays comme
    clé. Passe par une fonction client accédant au serveur qui détient la DB.
    """
    liste_vers_string = ""
    for mot in liste_choix:
        if mot == "":
            liste_vers_string += "''"
        else:
            liste_vers_string += mot

        if liste_choix.index(mot) != len(liste_choix) - 1:
            liste_vers_string += " "

    return cl.client_function("type " + liste_vers_string)


# print(caracteristique_pays(["Belgique", "Brésil", "", "", "habitants_2020,densite"]))

def coordonnees_affichage_4_pays(indice):
    x = 496
    y = 363
    if indice % 2 == 1:
        x = 130
    if indice // 3 == 0:
        y = 10

    return x, y


def tri(donnees, cle):
    cles_dictionnaire = list(donnees.keys())
    tri_intermediaire = sorted(cles_dictionnaire, key=lambda x: donnees[x][cle], reverse=True)

    tri_final = []
    for i in cles_dictionnaire:
        tri_final.append(tri_intermediaire.index(i))
    return tri_final


def distance_coordonnees(pays1, pays2):
    "Calcul la distance entre deux coordonnees Latitude et Longitude en Km"
    a1 = (pays1[0] + (pays1[1] / 60.0)) * pi / 180
    if pays1[2] == "N":
        a1 = -a1
    b1 = (pays1[3] + (pays1[4] / 60.0)) * pi / 180
    if pays1[5] == "O":
        b1 = -b1

    a2 = (pays2[0] + (pays2[1] / 60.0)) * pi / 180
    if pays2[2] == "N":
        a2 = -a2
    b2 = (pays2[3] + (pays2[4] / 60.0)) * pi / 180
    if pays2[5] == "O":
        b2 = -b2
    delta = acos(cos(a1) * cos(b1) * cos(a2) * cos(b2) + cos(a1) * sin(b1) * cos(a2) * sin(b2) + sin(a1) * sin(a2))
    return round(delta * 6378.0, 3)


def format_coordonnees(coord):
    valeurs = ""
    format_final = []
    for caractere in coord:
        if caractere == " ":
            if valeurs.isnumeric():
                format_final.append(int(valeurs))
            else:
                format_final.append(valeurs)
            valeurs = ""
        elif caractere.isalpha() or caractere.isnumeric():
            valeurs += caractere
    format_final.append(valeurs)
    return format_final


def verif_coordonnees(coord):
    donnees = coord.split()
    vertical = "NS"
    horizontal = "EOW"
    try:
        if donnees[0].isnumeric() and donnees[1].isnumeric() and donnees[2].isalpha() and donnees[3].isnumeric() and \
                donnees[4].isnumeric() and donnees[5].isalpha():
            if donnees[2] in vertical and donnees[5] in horizontal:
                return True
    except:
        return False
    return False


# print(verif_coordonnees('50 51 N 4 2 O'))

def ajout_pays_client(id, nom, coo, hab, sup, dens):
    cl.client_function("creation " + id + "  " + nom + "  " + coo + "  " + str(hab) + "  " + str(sup) + "  " +
                       str(dens))


def format_nom_pays(nom):
    pays_reformate = "_".join(re.split("[' -]", nom))

    booleen = True
    index = -1
    while booleen:
        if pays_reformate[index] == "_":
            index -= 1
        else:
            booleen = False

    if index != -1:
        return pays_reformate[:index + 1]
    else:
        return pays_reformate

