import sqlite3


def creation_db():
    """
    Permet de créer des tableaux dans la base de données 'tlca.db'.

    PRE : -
    POST : Crée le tableau et lui donne des valeurs.
    """
    connexion = sqlite3.connect("../db/tlca.db")

    connexion.execute(''' CREATE TABLE pays(
        id_pays VARCHAR(10) NOT NULL,
        nom_pays VARCHAR(30) NOT NULL,

        CONSTRAINT pk_pays PRIMARY KEY(id_pays));''')

    connexion.execute('''INSERT INTO pays(id_pays, nom_pays)
                    VALUES
                    ('BE', 'Belgique'),
                    ('DE', 'Allemagne'),
                    ('FR', 'France'),
                    ('ES', 'Espagne'),
                    ('IT', 'Italie');''')

    connexion.execute(''' CREATE TABLE infoPays(
        id_pays VARCHAR(10) NOT NULL,
        coordonnee VARCHAR(30) NOT NULL, 
        habitants_2020 INTEGER NOT NULL,
        superficie FLOAT NOT NULL,
        densite INTEGER NOT NULL,

        CONSTRAINT pk_infoPays_pays FOREIGN KEY(id_pays) REFERENCES pays (id_pays));''')

    connexion.execute('''INSERT INTO infoPays(id_pays, coordonnee, habitants_2020, superficie, densite)
                    VALUES
                    ('BE', '50° 51′ N, 4° 21′ E', 11476279, 30688, 374),
                    ('DE', '52° 31′ N, 13° 25′ E', 83149300, 357386, 233), 
                    ('FR', '48° 52′ N, 2° 19,59′ E', 67848156, 632734, 107.2),
                    ('ES', '40° 26′ N, 3° 42′ O', 46934632,	505911, 93),
                    ('IT', '41° 53′ N, 12° 29′ E', 60359546, 301336, 200);''')

    connexion.commit()
    connexion.close()


def suppression_tableau(nom_tableau):
    """
    Permet de supprimer un tableau dans la base de données 'tlca.db'.

    PRE : 'nom_tableau' est le nom du tableau à supprimer.
    POST : Supprime le tableau de la db.
    """
    connexion = sqlite3.connect("../db/tlca.db")

    connexion.execute('''DROP TABLE ''' + nom_tableau)


# creation_db()
# suppression_tableau("pays")
# suppression_tableau("infoPays")
