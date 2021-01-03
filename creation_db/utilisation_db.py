import sqlite3


def afficher_pays_db() -> dict:
    """
    Permet de récupérer les données de la table pays dans la DB tlca.db.

    PRE : La table 'pays' doit exister dans la DB.
    POST : Renvoie les données dans un dictionnaire.
    """
    connexion = sqlite3.connect("../db/tlca.db")

    sql = connexion.execute("SELECT id_pays, nom_pays from pays")
    donnees = {}
    for colonne in sql:  # colonne = tuple
        donnees[colonne[0]] = colonne[1]
    connexion.close()
    return donnees


def afficher_info_db() -> dict:
    """
    Permet de récupérer les données de la table 'infoPays' dans la DB tlca.db.

    PRE : La table 'infoPays' doit exister. Il doit y avoir au moins 5 colonnes dans cette dernière.
    POST : Renvoie les données dans un dictionnaire.
    """
    connexion = sqlite3.connect("../db/tlca.db")

    sql = connexion.execute("SELECT * from infoPays")
    donnees = {}
    for colonne in sql:  # colonne = tuple
        donnees[colonne[0]] = {"coordonnee": colonne[1], "habitants_2020": colonne[2],
                               "superficie": colonne[3], "densite": colonne[4]}
    connexion.close()
    return donnees


def informations_un_pays(nom_pays: str) -> dict:
    """
    Permet de récupérer toutes les informations d'un pays précis, informations récupérées dans la DB tlca.db.

    PRE : 'nom_pays' est le nom d'un pays sous forme de string.
    POST : Renvoie les données dans un dictionnaire rempli si le pays existe dans la DB, vide si pas.
    """
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


def info_pays(lettres: str) -> dict:
    """
    Permet de récupérer certains noms des pays, ainsi que leur id ; trouvés dans la DB tlca.db.

    PRE : 'lettres' est une string.
    POST : Renvoie les id des différents pays commençants par les lettres 'lettres', ainsi que leur nom. Le dictionnaire
    est vide dans le cas où aucun pays ne correspond.
    """
    connexion = sqlite3.connect("../db/tlca.db")

    sql = connexion.execute("SELECT * from pays where nom_pays like '" + lettres + "%'")
    donnees = {}
    for colonne in sql:
        donnees[colonne[0]] = colonne[1]
    connexion.close()
    return donnees


def pays_comparaison_type(pays) -> dict:
    """
    Permet de récupérer certaines données de pays précis.

    PRE : 'pays' est une liste ; les 4 premiers paramètres sont des pays où des strings vides, et le dernier paramètre
    est le type de données que l'on souhaite (superficie, habitants_2020 ou coordonnée.
    POST : Renvoie les données dans un dictionnaire.
    """
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


def ajout_pays(donnees: list) -> None:
    """
    Permet d'ajouter des données dans la DB tlca.db'.

    PRE : 'donnees' est une liste ; [id_pays, nom_pays, coordonnées_pays, nbr_habitants, superficie, densité]
    POST : Ajoute les données dans la table infoPays ainsi que la table pays.
    """
    connexion = sqlite3.connect("../db/tlca.db")
    connexion.execute('INSERT INTO pays(id_pays, nom_pays) VALUES ("' + donnees[0] + '", "' + donnees[1] + '");')
    connexion.execute('INSERT INTO infoPays(id_pays, coordonnee, habitants_2020, superficie, densite) '
                      'VALUES ("' + donnees[0] + '", "' + str(donnees[2]) + '", ' + donnees[3] + ', ' + donnees[4]
                      + ', ' + donnees[4] + ');')
    connexion.commit()
    connexion.close()


def suppression_pays(id: str) -> None:
    """
    Permet de supprimer des données dans la table pays de la DB tlca.db'.

    PRE : 'id' est l'id (code ISO 3166-1 alpha-2) du pays que l'on souhaite supprimer.
    POST : Supprime le pays sur base de son id.
    """
    connexion = sqlite3.connect("../db/tlca.db")
    connexion.execute("DELETE FROM pays WHERE id_pays = '" + id + "';")
    connexion.commit()
    connexion.close()
