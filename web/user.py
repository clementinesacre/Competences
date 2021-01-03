from typing import Tuple

from web import client as cl
from math import cos, sin, acos, pi
import re


def tous_pays() -> dict:
    """
    Appelle le client pour avoir tous les id et noms du pays de la DB tlca.db.

    PRE : -
    POST : Appelle la fonction client avec le paramètre 'tous', retourne un dictionnaire.
    """
    return cl.client_function("tous")


def un_pays(nom_pays: str) -> dict:
    """
    Appelle le client pour avoir tous les id et noms du pays de la DB tlca.db où le nom du pays commence par 'nom_pays'.

    PRE : 'nom_pays' est une string.
    POST : Appelle la fonction client avec le paramètre 'pays' + les lettres. Retourne un dictionnaire.
    """
    return cl.client_function("pays " + nom_pays)


def caracteristique_pays(liste_choix: list) -> dict:
    """
    Permet de récupérer certaines informations de plusieurs pays (de 2 à 4 pays).

    PRE : 'liste_choix' est une liste avec des pays ou des strings vides pour les 4 premiers indices, et le type
    d'information comme 5e paramètre.
    POST : Renvoie une dictionnaire contenant l'information, selon le type précisé, comme valeur et l'id du pays comme
    clé. Passe par une fonction client accédant au serveur qui détient la DB. Retourne un dictionnaire.
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


def coordonnees_affichage_4_pays(indice: int) -> Tuple[int, int]:
    """
    Permet d'avoir les coordonnées où se placer en fonction du nombre entré.

    PRE : 'indice' est un entier.
    POST : Retourne les coordonnées 'x' et 'y' où se placer.
    """
    x = 496
    y = 363
    if indice % 2 == 1:
        x = 130
    if indice // 3 == 0:
        y = 10

    return x, y


def tri(donnees: dict, cle: int) -> list:
    """
    Permet de trier des données d'un dictionnaire selon un paramètre.

    PRE : 'dict' est un dictionnaire reprenant les différentes données des pays, la clé est l'id du pays, la valeur est
    un dictionnaire, dans ce dictionnaire, il y a d'autres données. 'cle' est le paramètre sur lequel la fonction
    se base pour trier.
    POST : Retourne une liste comprenant les id des pays, triée sur base de 'cle'.
    """
    print("donn ", donnees)
    print("cle ", cle)
    cles_dictionnaire = list(donnees.keys())
    tri_intermediaire = sorted(cles_dictionnaire, key=lambda x: donnees[x][cle], reverse=True)

    tri_final = []
    for i in cles_dictionnaire:
        tri_final.append(tri_intermediaire.index(i))
    return tri_final


def distance_coordonnees(pays1: list, pays2: list) -> float:
    """
    Permet de calculer la distance entre deux coordonnees Latitude et Longitude en Km.

    PRE : 'pays1' et 'pays2' sont des listes ; [latitude_degré, latitude_minute, latitude_direction, longitude_degré,
                                                longitude_minute, longitude_direction]
    POST : Retourne la distance entre 2 pays en km (c'est un float).
    """
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


def format_coordonnees(coord: str) -> list:
    """
    Permet de traduire une coordonnée sous forme de string en une liste de string.

    PRE : 'coord' est une coordonnée.
    POST : Retourne une liste contenant 6 valeurs.
    """
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


def verif_coordonnees(coord: str) -> bool:
    """
    Permet de vérifier qu'une coordonnée correspond au format attendu.

    PRE : 'coord' est une string tel que '50 51 N 4 2 O'.
    POST : Retourne un booléen.
    """
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


def ajout_pays_client(id: str, nom: str, coo: str, hab: int, sup: int, dens: float) -> None:
    """
    Appelle le client pour ajouter un pays dans la DB tlca.db.

    PRE : 'id' est une string représente le code code ISO 3166-1 alpha-2 du pays. 'nom' est une string
    représentant le nom du pays. 'coo' est une string représentant les coordonnées de la capitale du pays. 'hab'
    est un entier représentant le nombre d'habitants du pays en 2020. 'sup' est un entier représentant la superficie
    totale du pays. 'dens' est un nombre flotant représentant la densité du pays.
    POST : Appelle la fonction client avec le paramètre 'creation', et les données du nouveau pays.
    """
    cl.client_function("creation " + id + "  " + nom + "  " + coo + "  " + str(hab) + "  " + str(sup) + "  " +
                       str(dens))


def format_nom_pays(nom: str) -> str:
    """
    Formate le nom du pays entré afin qu'il correspondent à certains critères.

    PRE : 'nom' est une string contenant le nom du pays.
    POST : Retourne le nouveau nom du pays respectant certains critères.
    """
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
