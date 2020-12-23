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
