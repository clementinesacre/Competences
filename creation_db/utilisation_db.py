import sqlite3


def afficher_db():
    """
    Permet de récupérer les données de la table pays dans la db tlca.db.

    PRE : Le tableau pays doit exister dans la DB.
    POST : Renvoie les données dans un dictionnaire.
    """
    connexion = sqlite3.connect("../db/tlca.db")

    sql = connexion.execute("SELECT * from pays")
    donnees = {}
    index = 0
    for colonne in sql:  # colonne = tuple
        donnees[index] = {'id': colonne[0], 'pays': colonne[1]}
        index += 1
    connexion.close()
    return donnees
