import sqlite3


def afficher_pays_db():
    """
    Permet de récupérer les données de la table pays dans la db tlca.db.

    PRE : Le tableau pays doit exister dans la DB.
    POST : Renvoie les données dans un dictionnaire.
    """
    connexion = sqlite3.connect("../db/tlca.db")

    sql = connexion.execute("SELECT * from pays")
    donnees = {}
    for colonne in sql:  # colonne = tuple
        donnees[colonne[0]] = colonne[1]
    connexion.close()
    return donnees


def informations_un_pays(nom_pays):
    connexion = sqlite3.connect("../db/tlca.db")
    # sql = connexion.execute("SELECT * from infoPays where id_pays = '" + nom_pays + "';")
    sql = connexion.execute(
        "SELECT infoPays.id_pays, nom_pays, coordonnee, habitants_2020, superficie, densite from infoPays "
        "JOIN pays on infoPays.id_pays=pays.id_pays where infoPays.id_pays = '" + nom_pays + "';")

    donnees = {}
    for colonne in sql:
        donnees[colonne[0]] = {"nom": colonne[1], "coordonee": colonne[2], "habitants_2020": colonne[3],
                               "superficie": colonne[4], "densite": colonne[5]}
    connexion.close()
    return donnees


def info_pays(lettres):
    connexion = sqlite3.connect("../db/tlca.db")

    sql = connexion.execute("SELECT * from pays where nom_pays like '" + lettres + "%'")
    donnees = {}
    for colonne in sql:
        donnees[colonne[0]] = colonne[1]
    connexion.close()
    return donnees

