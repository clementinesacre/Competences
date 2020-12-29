import sqlite3


def afficher_pays_db():
    """
    Permet de récupérer les données de la table pays dans la db tlca.db.

    PRE : Le tableau pays doit exister dans la DB.
    POST : Renvoie les données dans un dictionnaire.
    """
    connexion = sqlite3.connect("../db/tlca.db")

    sql = connexion.execute("SELECT id_pays, nom_pays from pays")
    donnees = {}
    for colonne in sql:  # colonne = tuple
        donnees[colonne[0]] = colonne[1]
    connexion.close()
    return donnees


def afficher_info_db():
    connexion = sqlite3.connect("../db/tlca.db")

    sql = connexion.execute("SELECT * from infoPays")
    donnees = {}
    for colonne in sql:  # colonne = tuple
        donnees[colonne[0]] = {"coordonnee": colonne[1], "habitants_2020": colonne[2],
                               "superficie": colonne[3], "densite": colonne[4]}
    connexion.close()
    return donnees


def informations_un_pays(nom_pays):
    connexion = sqlite3.connect("../db/tlca.db")
    sql = connexion.execute(
        "SELECT infoPays.id_pays, nom_pays, coordonnee, habitants_2020, superficie, densite from infoPays "
        "JOIN pays on infoPays.id_pays=pays.id_pays where pays.nom_pays = '" + nom_pays + "';")

    donnees = {}
    for colonne in sql:
        donnees[colonne[0]] = {"nom": colonne[1], "coordonnee": colonne[2], "habitants_2020": colonne[3],
                               "superficie": colonne[4], "densite": colonne[5]}
    connexion.close()
    return donnees


# print(informations_un_pays("SriLanka"))

def info_pays(lettres):
    connexion = sqlite3.connect("../db/tlca.db")

    sql = connexion.execute("SELECT * from pays where nom_pays like '" + lettres + "%'")
    donnees = {}
    for colonne in sql:
        donnees[colonne[0]] = colonne[1]
    connexion.close()
    return donnees


def pays_comparaison_type(pays):
    connexion = sqlite3.connect("../db/tlca.db")

    sql = connexion.execute("SELECT pays.id_pays, nom_pays, " + pays[4] +
                            " FROM infoPays JOIN pays ON infoPays.id_pays = pays.id_pays WHERE pays.nom_pays = '"
                            + pays[0] + "' or pays.nom_pays = '" + pays[1] + "' " "or pays.nom_pays = '" + pays[2] +
                            "' or pays.nom_pays = '" + pays[3] + "';")
    donnees = {}
    for colonne in sql:
        if "habitants_2020" in pays[4] or "superficie" in pays[4]:
            donnees[colonne[0]] = {"nom_pays": colonne[1], "info": colonne[2], "densite": colonne[3]}
        else:
            donnees[colonne[0]] = {"nom_pays": colonne[1], "info": colonne[2]}
    connexion.close()
    return donnees


def ajout_pays(donnees):
    connexion = sqlite3.connect("../db/tlca.db")
    connexion.execute('INSERT INTO pays(id_pays, nom_pays) VALUES ("' + donnees[0] + '", "' + donnees[1] + '");')
    connexion.execute('INSERT INTO infoPays(id_pays, coordonnee, habitants_2020, superficie, densite) '
                      'VALUES ("' + donnees[0] + '", "' + str(donnees[2]) + '", ' + donnees[3] + ', ' + donnees[4]
                      + ', ' + donnees[4] + ');')
    connexion.commit()
    connexion.close()


# ajout_pays(['AM', 'Vdlgk', "50° 51' S, 4° 2' O", '46581', '35689', '4988'])


def suppression_pays(id):
    connexion = sqlite3.connect("../db/tlca.db")
    connexion.execute("DELETE FROM pays WHERE id_pays = '" + id + "';")
    connexion.commit()
    connexion.close()

# suppression_pays("AM")
