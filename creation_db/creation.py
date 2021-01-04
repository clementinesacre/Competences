import sqlite3


def creation_db() -> None:
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
                    ('IT', 'Italie'),
                    ('BR', 'Brésil'),
                    ('MV', 'Maldives'),
                    ('GB-ENG', 'Angleterre'),
                    ('RU', 'Russie'),
                    ('PE', 'Pérou'),
                    ('AO', 'Angola'),
                    ('MG', 'Madagascar'),
                    ('PA', 'Panama'),
                    ('PY', 'Paraguay'),
                    ('DZ', 'Algérie'),
                    ('PT', 'Portugal'),
                    ('PL', 'Pologne'),
                    ('AL', 'Albanie'),
                    ('MR', 'Mauritanie'),
                    ('CN', 'Chine'),
                    ('VN', 'Vietnam');''')

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
                    ('IT', '41° 53′ N, 12° 29′ E', 60359546, 301336, 200),
                    ('BR', '15° 47′ S, 47° 52′ W', 210147125, 8515767, 25),
                    ('MV', '4° 10′ N, 73° 30′ E', 391904, 298, 1315),
                    ('GB-ENG', '51° 30′ N, 0° 7′ W', 56286961, 130279, 432),
                    ('RU', '55° 45′ N, 37° 37′ E', 146751300, 17098246, 8.4),
                    ('PE', '12° 02′ S, 77° 01′ O', 31914989, 1285216 , 25),
                    ('AO', '8° 50′ S, 13° 20′ E', 31127674, 1246700, 24.97),
                    ('MG', '18° 55′ S, 47° 31′ E', 26262313, 35.2, 587041),
                    ('PA', '8° 58′ N, 79° 32′ W', 4176869, 75417, 56),
                    ('PY', '25° 16′ S, 57° 40′ W', 7292672, 406757, 17.93),
                    ('DZ', '36° 42′ N, 3° 13′ E', 43900000, 2381741, 17.7),
                    ('PT', '38° 46′ N, 9° 9′ W', 10295909, 92226, 114.5),
                    ('PL', '52° 13′ N, 21° 00′ E', 38282325 , 312679, 122),
                    ('AL', '41° 19′ N, 19° 49′ E', 2845955, 28748, 98),
                    ('MR', '18° 09′ N, 15° 58′ W', 4403313, 1030000, 3.4),
                    ('CN', '39° 55′ N, 116° 23′ E', 1400050000, 9596961, 145),
                    ('VN', '21° 2′ N, 105° 51′ E', 96208984, 331212, 290.48);''')

    connexion.commit()
    connexion.close()


def suppression_tableau(nom_tableau: str) -> None:
    """
    Permet de supprimer un tableau dans la base de données 'tlca.db'.

    PRE : 'nom_tableau' est le nom du tableau à supprimer.
    POST : Supprime le tableau de la db.
    """
    connexion = sqlite3.connect("../db/tlca.db")

    connexion.commit()
    connexion.execute('''DROP TABLE ''' + nom_tableau)

# creation_db()
# suppression_tableau("pays")
# suppression_tableau("infoPays")
