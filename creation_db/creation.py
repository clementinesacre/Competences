import sqlite3


def creation_db(nom_db):
    connexion = sqlite3.connect(nom_db)

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


def suppression_tableaux(nom_db) :
    connexion = sqlite3.connect(nom_db)

    connexion.execute('''DROP TABLE pays''')


def afficher_db(nom_db):
    connexion = sqlite3.connect(nom_db)

    donnees = connexion.execute("SELECT * from pays")
    for colonne in donnees:
        print("ID = ", colonne[0])
        print("PAYS = ", colonne[1], "\n")
    print(donnees)

    connexion.close()


#creation_db("../db/tlca.db")
#suppression_tableaux("../db/tlca.db")
afficher_db("../db/tlca.db")
