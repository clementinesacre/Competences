import tkinter as tk
from web import user
import re

position_x_pays_place = 500
position_y_pays_place = 20
espace_y_pays_place = 130

c_bg_principal = '#424142'
c_bouton_principal = '#E8BAE5'
c_ecriture = '#FFFFFF'
c_ligne_label_frame = '#000000'
mouse = 'circle'
police_base = ('Helvitiva', 15)


class Graphique:
    def __init__(self) -> None:
        """
        Instancie tous les widgets / paramètres utiles pour le bon fonctionnement de l'application

        PRE : -
        POST : Appelle la fonction suivante ; self.initialisation().
        """
        self.__racine = tk.Tk(className='projet')
        self.__canv = tk.Canvas(self.__racine, bg=c_bg_principal, height=700, width=725)
        self.__canv.pack()

        # création et installation du menu de navigation
        menubar = tk.Menu(self.__racine)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Menu principal", command=lambda: self.menu_principal())
        filemenu.add_command(label="Comparer", command=lambda: self.menu_comparer())
        filemenu.add_command(label="Modifier", command=lambda: self.menu_modifier())
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.__racine.destroy)
        menubar.add_cascade(label="Naviguer", menu=filemenu)
        self.__racine.config(menu=menubar)

        # initialisation des widgets
        self.__button_menu_comparaison = tk.Button()
        self.__button_ajouter_pays = tk.Button()

        # Comparer
        self.__barre_recherche = tk.Label()
        self.__lb = tk.Listbox()
        self.__liste_pays_selectionnes = ["", "", "", ""]
        self.__bouton_retirer = tk.Button()
        self.__liste_label_selection = ["", "", "", ""]
        self.__bouton_lancer_comparaison = tk.Button()
        self.__pays_choisi = tk.Label()
        self.__aucun_pays = tk.Label()

        self.__pays1 = tk.LabelFrame()
        self.__pays2 = tk.LabelFrame()
        self.__pays3 = tk.LabelFrame()
        self.__pays4 = tk.LabelFrame()
        self.__entree_utilisateur = tk.Entry()
        self.__liste_labelframe = [self.__pays1, self.__pays2, self.__pays3, self.__pays4, self.__barre_recherche,
                                   self.__entree_utilisateur]

        self.__bouton_comparer_habitants = tk.Button()
        self.__bouton_comparer_superficie = tk.Button()
        self.__bouton_comparer_coordonnees = tk.Button()
        self.__choix_comparaison = tk.Label()
        self.__liste_type_comparaison = [self.__choix_comparaison, self.__bouton_comparer_habitants,
                                         self.__bouton_comparer_superficie, self.__bouton_comparer_coordonnees]

        self.__titre_pays = tk.Label()
        self.__pays_donnees = tk.Label()
        self.__pays_densite = tk.Label()
        self.__numero_place = tk.Label()
        self.__distance_km = tk.Label()
        self.__liste_widgets_pays_compare = [[self.__titre_pays], [self.__pays_donnees], [self.__pays_densite],
                                             [self.__numero_place]]

        self.__dessin = tk.Canvas()

        # Modifier
        self.__ajout_pays_info_entry = tk.Entry()
        self.__ajout_pays_info_label = tk.Label()
        self.__ajout_pays_nom_entry = tk.Entry()
        self.__ajout_pays_nom_label = tk.Label()
        self.__ajout_pays_id_entry = tk.Entry()
        self.__ajout_pays_id_label = tk.Label()
        self.__ajout_pays_coo_entry = tk.Entry()
        self.__ajout_pays_coo_label = tk.Label()
        self.__ajout_pays_hab_entry = tk.Entry()
        self.__ajout_pays_hab_label = tk.Label()
        self.__ajout_pays_sup_entry = tk.Entry()
        self.__ajout_pays_sup_label = tk.Label()
        self.__ajout_pays_dens_entry = tk.Entry()
        self.__ajout_pays_dens_label = tk.Label()
        self.__liste_info_nv_pays = [[self.__ajout_pays_id_entry, self.__ajout_pays_id_label],
                                     [self.__ajout_pays_nom_entry, self.__ajout_pays_nom_label],
                                     [self.__ajout_pays_coo_entry, self.__ajout_pays_coo_label],
                                     [self.__ajout_pays_hab_entry, self.__ajout_pays_hab_label],
                                     [self.__ajout_pays_sup_entry, self.__ajout_pays_sup_label],
                                     [self.__ajout_pays_dens_entry, self.__ajout_pays_dens_label]]

        self.__bouton_ajouter_pays = tk.Button()
        self.__ajout_pays_id_valid = tk.Canvas()
        self.__ajout_pays_nom_valid = tk.Canvas()
        self.__ajout_pays_coo_valid = tk.Canvas()
        self.__ajout_pays_hab_valid = tk.Canvas()
        self.__ajout_pays_sup_valid = tk.Canvas()
        self.__ajout_pays_dens_valid = tk.Canvas()
        self.__explication_pays_id = tk.Label()
        self.__explication_pays_nom = tk.Label()
        self.__explication_pays_coo = tk.Label()
        self.__explication_pays_hab = tk.Label()
        self.__explication_pays_sup = tk.Label()
        self.__explication_pays_dens = tk.Label()
        self.__liste_carre_nv_pays = [[self.__ajout_pays_id_valid, self.__explication_pays_id],
                                      [self.__ajout_pays_nom_valid, self.__explication_pays_nom],
                                      [self.__ajout_pays_coo_valid, self.__explication_pays_coo],
                                      [self.__ajout_pays_hab_valid, self.__explication_pays_hab],
                                      [self.__ajout_pays_sup_valid, self.__explication_pays_sup],
                                      [self.__ajout_pays_dens_valid, self.__explication_pays_dens]]

        self.initialisation()

    def initialisation(self) -> None:
        """
        Crée et place les boutons du menu principal.

        PRE : -
        POST : Crée les boutons 'comparer' et 'ajouter' et lance également la boucle de l'application.
        """
        self.__button_menu_comparaison = tk.Button(self.__racine, text="Comparer des pays", height=2, width=16,
                                                   bg=c_bouton_principal,
                                                   fg=c_ecriture, bd=1, activebackground=c_ecriture,
                                                   activeforeground=c_bouton_principal, font=police_base,
                                                   cursor=mouse, command=lambda: self.comparer_pays())
        self.__button_ajouter_pays = tk.Button(self.__racine, text="Ajouter un pays", height=2, width=16,
                                               bg=c_bouton_principal,
                                               fg=c_ecriture, bd=1, activebackground=c_ecriture,
                                               activeforeground=c_bouton_principal, cursor=mouse,
                                               command=lambda: self.creer_pays(), font=police_base)
        self.__button_menu_comparaison.place(x=275, y=250)
        self.__button_ajouter_pays.place(x=275, y=350)

        self.__racine.mainloop()

    def comparer_pays(self) -> None:
        """
        Permet de choisir les pays que l'on souhaite comparer, via une zone de texte accessible par l'utilisateur.

        PRE : -
        POST : Appelle une autre fonction, à chaque fois que l'utilisateur change la zone de texte.
        """
        self.remise_a_zero()

        width_lf = 200
        height_lf = 110

        self.__pays1 = tk.LabelFrame(self.__racine, text="Pays 1 :", bg=c_bg_principal, width=width_lf,
                                     height=height_lf, fg=c_ecriture, font=police_base)
        self.__pays1.place(x=position_x_pays_place, y=position_y_pays_place)
        self.__pays2 = tk.LabelFrame(self.__racine, text="Pays 2 :", bg=c_bg_principal, width=width_lf,
                                     height=height_lf, fg=c_ecriture, font=police_base)
        self.__pays2.place(x=position_x_pays_place, y=position_y_pays_place + 1 * espace_y_pays_place)
        self.__pays3 = tk.LabelFrame(self.__racine, text="Pays 3 :", bg=c_bg_principal, width=width_lf,
                                     height=height_lf, fg=c_ecriture, font=police_base)
        self.__pays3.place(x=position_x_pays_place, y=position_y_pays_place + 2 * espace_y_pays_place)
        self.__pays4 = tk.LabelFrame(self.__racine, text="Pays 4 :", bg=c_bg_principal, width=width_lf,
                                     height=height_lf, fg=c_ecriture, font=police_base)
        self.__pays4.place(x=position_x_pays_place, y=position_y_pays_place + 3 * espace_y_pays_place)

        self.__barre_recherche = tk.Label(self.__racine, text="Chercher le pays :", bg=c_bg_principal, height=2,
                                          width=15, fg=c_ecriture, font=police_base)
        self.__barre_recherche.place(x=11, y=15)

        value = tk.StringVar()
        value.set("")
        self.__entree_utilisateur = tk.Entry(show=None, textvariable=value, font=police_base, width=16)
        self.__entree_utilisateur.place(x=12, y=60)

        self.__liste_labelframe = [self.__pays1, self.__pays2, self.__pays3, self.__pays4, self.__barre_recherche,
                                   self.__entree_utilisateur]

        def on_change(a, b, c) -> None:
            value.get()
            self.afficher_liste_pays(self.__entree_utilisateur.get())

        value.trace('w', on_change)

    def afficher_liste_pays(self, lettres: str) -> None:
        """
        Crée et place la liste déroulante en affichant les pays, selon les lettres entrées par l'utilisateur.

        PRE : 'lettres' est une string.
        POST : Affiche soit les pays correspondants aux lettres, soit un message précisant qu'aucun pays ne correspond.
        """
        pays_correspondants = sorted(list(user.un_pays(lettres).values()))
        var = tk.StringVar(value=pays_correspondants)
        self.__lb.destroy()
        affichage_pays = (len(pays_correspondants), 10)[len(pays_correspondants) > 10]
        self.__lb = tk.Listbox(self.__racine, listvariable=var, selectmode='single', height=affichage_pays,
                               width=29, bd=0, selectbackground=c_bouton_principal)

        if lettres == "":
            self.__lb.destroy()
            self.__aucun_pays.destroy()
        else:
            if len(pays_correspondants) == 0:
                self.__lb.destroy()
                self.__aucun_pays = tk.Label(self.__racine, text="Aucun résultat", bg=c_bg_principal, height=1,
                                             width=10, fg=c_ecriture, anchor='w', font=('Helvitiva', 11),
                                             justify="left")
                self.__aucun_pays.place(x=12, y=87)
            else:
                self.__aucun_pays.destroy()
                self.__lb.place(x=13, y=87)
                self.__lb.bind('<<ListboxSelect>>', lambda x: self.afficher_pays_choisi())

    def afficher_pays_choisi(self) -> None:
        """
        Affiche les pays sélectionnés par l'utilisateur.

        PRE : -
        POST : Place le nom des pays dans la case adéquate ainsi qu'un bouton permettant de supprimer le pays choisi
        pour en mettre un autre. A partir de 2 pays sélectionnés, le bouton de comparaison apparait et il est possible
        de comparer les pays sélectionnés.
        """
        if len(self.__lb.curselection()) > 0 and self.__liste_pays_selectionnes.count("") > 0 \
                and self.__lb.get(self.__lb.curselection()[0]) not in self.__liste_pays_selectionnes:
            pays_selectionne = self.__lb.curselection()[0]
            index = self.__liste_pays_selectionnes.index("")

            self.__liste_pays_selectionnes[index] = self.__lb.get(pays_selectionne)
            self.__pays_choisi = tk.Label(self.__racine, text=self.__lb.get(pays_selectionne), bg=c_ecriture,
                                          height=1, width=13, fg=c_ligne_label_frame, font=police_base)
            self.__pays_choisi.place(x=25 + position_x_pays_place, y=55 + index * espace_y_pays_place)
            self.__bouton_retirer = tk.Button(self.__racine, text="Supprimer", activeforeground=c_bouton_principal,
                                              height=1, width=12, bg=c_bouton_principal, fg=c_ecriture, bd=1,
                                              activebackground=c_ecriture, cursor=mouse, font=('Helvitiva', 10),
                                              command=lambda: self.retirer_choix(index))
            self.__bouton_retirer.place(x=position_x_pays_place + 7, y=98 + index * espace_y_pays_place)
            self.__liste_label_selection[index] = [self.__pays_choisi, self.__bouton_retirer]

            if self.__liste_pays_selectionnes.count("") <= 2:
                self.__bouton_lancer_comparaison.destroy()
                self.__bouton_lancer_comparaison = tk.Button(self.__racine, text="Comparer", height=1, width=12,
                                                             bg=c_bouton_principal, activebackground=c_ecriture,
                                                             fg=c_ecriture, bd=1, activeforeground=c_bouton_principal,
                                                             cursor=mouse, font=police_base,
                                                             command=lambda: self.type_comparaison())
                self.__bouton_lancer_comparaison.place(x=580, y=550)

    def retirer_choix(self, indice: int) -> None:
        """
        Permet de supprimer le choix de l'utilisateur.

        PRE : 'indice' est un entier et représente l'indice du pays voulant être supprimé, il se trouve entre 0 et 3.
        POST : Selon le nombre de pays choisi restant, le bouton de comparaison reste (minimum 2 pays) ou est supprimé.
        """
        self.__liste_label_selection[indice][0].destroy()
        self.__liste_label_selection[indice][1].destroy()
        self.__liste_label_selection[indice] = ""
        self.__liste_pays_selectionnes[indice] = ""
        if self.__liste_pays_selectionnes.count("") > 2:
            self.__bouton_lancer_comparaison.destroy()

    def type_comparaison(self) -> None:
        """
        Permet de choisir le type sur lequel on va se baser pour comparer les pays sélectionnés.

        PRE : -
        POST : Crée et place 3 boutons avec les 3 types (nbr_habitants, superficie, coordonnées).
        """
        copie = list(self.__liste_pays_selectionnes)
        self.remise_a_zero()
        self.__liste_pays_selectionnes = list(copie)

        self.__choix_comparaison = tk.Label(self.__racine, text="Types de comparaisons :", bg=c_bg_principal,
                                            height=1, width=20, fg=c_ecriture, font=('Helvitiva', 20))
        self.__choix_comparaison.place(x=80, y=190)

        self.__bouton_comparer_habitants = tk.Button(self.__racine, text="Habitants", height=1, width=12,
                                                     bg=c_bouton_principal, fg=c_ecriture, bd=1, cursor=mouse,
                                                     activebackground=c_ecriture, font=police_base,
                                                     activeforeground=c_bouton_principal,
                                                     command=lambda: self.comparaison_finale('habitants'))
        self.__bouton_comparer_habitants.place(x=275, y=250)
        self.__bouton_comparer_superficie = tk.Button(self.__racine, text="Superficie", height=1, width=12,
                                                      bg=c_bouton_principal, fg=c_ecriture, bd=1,
                                                      activebackground=c_ecriture, cursor=mouse,
                                                      activeforeground=c_bouton_principal, font=police_base,
                                                      command=lambda: self.comparaison_finale('superficie'))
        self.__bouton_comparer_superficie.place(x=275, y=310)
        self.__bouton_comparer_coordonnees = tk.Button(self.__racine, text="Coordonnées", height=1, width=12,
                                                       bg=c_bouton_principal, fg=c_ecriture, bd=1, cursor=mouse,
                                                       activebackground=c_ecriture, font=police_base,
                                                       activeforeground=c_bouton_principal,
                                                       command=lambda: self.comparaison_finale('distance'))
        self.__bouton_comparer_coordonnees.place(x=275, y=370)

        self.__liste_type_comparaison = [self.__choix_comparaison, self.__bouton_comparer_habitants,
                                         self.__bouton_comparer_superficie, self.__bouton_comparer_coordonnees]

    def comparaison_finale(self, type: str) -> None:
        """
        Appelle la fonction adéquate selon le type de comparaison voulue.

        PRE : 'type' est une string, ayant comme valeur soit 'habitants', 'superficie', ou soit 'distance'.
        POST : Appelle la fonction adéquate.
        """
        copie = list(self.__liste_pays_selectionnes)
        self.remise_a_zero()
        self.__liste_pays_selectionnes = list(copie)

        if type == "habitants":
            self.comparaison_habitants()
        elif type == "superficie":
            self.comparaison_superficie()
        elif type == "distance":
            self.comparaison_distance()

    def comparaison_habitants(self) -> None:
        """
        Permet de comparer les pays sur base de leur nombre d'habitants.

        PRE : -
        POST : Place les pays, ainsi que des informations sur ces derniers. Place des numéros représentants l'ordre des
        pays selon le nombre d'habitants. Le premier est celui ayant le plus grand nombre d'habitants.
        """
        liste_choix = self.__liste_pays_selectionnes + ["habitants_2020,densite"]
        donnees = user.caracteristique_pays(liste_choix)
        self.quadrillage()

        podium = user.tri(donnees, "info")

        indice = 1
        for id in donnees:
            position_x_comparaison, position_y_comparaison = user.coordonnees_affichage_4_pays(indice)
            self.__titre_pays = tk.Label(self.__racine, text=donnees[id]["nom_pays"], bg=c_bg_principal,
                                         height=1, width=15, fg=c_ecriture, font=('Helvitiva', 16), anchor='w')
            self.__pays_donnees = tk.Label(self.__racine, text="Nombre d'habitants : " + str(donnees[id]["info"]),
                                           bg=c_bg_principal, height=1, width=23, fg=c_ecriture, font=('Helvitiva', 11),
                                           anchor='w')
            self.__pays_densite = tk.Label(self.__racine, text="Densité : " + str(donnees[id]["densite"]) + " hab/km²",
                                           bg=c_bg_principal, height=1, width=17, fg=c_ecriture, font=('Helvitiva', 11),
                                           anchor='w')

            self.__titre_pays.place(x=position_x_comparaison, y=position_y_comparaison)
            self.__pays_donnees.place(x=position_x_comparaison - 120, y=position_y_comparaison + 100)
            self.__pays_densite.place(x=position_x_comparaison - 120, y=position_y_comparaison + 130)

            self.__numero_place = self.emplacement_podium(int(podium[indice - 1]) + 1, position_x_comparaison,
                                                          position_y_comparaison)

            self.__liste_widgets_pays_compare[indice - 1] = [self.__titre_pays, self.__pays_donnees,
                                                             self.__pays_densite, self.__numero_place]
            indice += 1

    def comparaison_superficie(self) -> None:
        """
        Permet de comparer les pays sur base de leur superficie.

        PRE : -
        POST : Place les pays, ainsi que des informations sur ces derniers. Place des numéros représentants l'ordre des
        pays selon leur superficie. Le premier est celui ayant le plus grand nombre de km².
        """
        liste_choix = self.__liste_pays_selectionnes + ["superficie,densite"]
        donnees = user.caracteristique_pays(liste_choix)
        self.quadrillage()

        podium = user.tri(donnees, "info")

        indice = 1
        for id in donnees:
            position_x_comparaison, position_y_comparaison = user.coordonnees_affichage_4_pays(indice)
            self.__titre_pays = tk.Label(self.__racine, text=donnees[id]["nom_pays"], bg=c_bg_principal,
                                         height=1, width=15, fg=c_ecriture, font=('Helvitiva', 16), anchor='w')
            self.__pays_donnees = tk.Label(self.__racine, text="Superficie : " + str(donnees[id]["info"]) + " km²",
                                           bg=c_bg_principal, height=1, width=23, fg=c_ecriture, font=('Helvitiva', 11),
                                           anchor='w')
            self.__pays_densite = tk.Label(self.__racine, text="Densité : " + str(donnees[id]["densite"]) + " hab/km²",
                                           bg=c_bg_principal, height=1, width=17, fg=c_ecriture, font=('Helvitiva', 11),
                                           anchor='w')

            self.__titre_pays.place(x=position_x_comparaison, y=position_y_comparaison)
            self.__pays_densite.place(x=position_x_comparaison - 120, y=position_y_comparaison + 130)
            self.__pays_donnees.place(x=position_x_comparaison - 120, y=position_y_comparaison + 100)

            self.__numero_place = self.emplacement_podium(int(podium[indice - 1]) + 1, position_x_comparaison,
                                                          position_y_comparaison)

            self.__liste_widgets_pays_compare[indice - 1] = [self.__titre_pays, self.__pays_donnees,
                                                             self.__pays_densite, self.__numero_place]
            indice += 1

    def comparaison_distance(self) -> None:
        """
        Permet de comparer les coordonnées des différents pays ainsi que la distance de chaque pays entre eux.

        PRE : -
        POST : Place les pays, ainsi que des informations sur ces derniers (dont la distance avec les autres pays).
        """
        liste_choix = self.__liste_pays_selectionnes + ["coordonnee"]
        donnees = user.caracteristique_pays(liste_choix)
        self.quadrillage()

        indice = 1
        for id in donnees:
            # self.__liste_widgets_pays_compare[indice - 1] = []
            position_x_comparaison, position_y_comparaison = user.coordonnees_affichage_4_pays(indice)
            self.__titre_pays = tk.Label(self.__racine, text=donnees[id]["nom_pays"], bg=c_bg_principal,
                                         height=1, width=15, fg=c_ecriture, font=('Helvitiva', 16), anchor='w')
            # self.__liste_widgets_pays_compare[indice - 1].append(self.__titre_pays)
            self.__pays_donnees = tk.Label(self.__racine, text="Coordonnee : " + str(donnees[id]["info"]), anchor='w',
                                           bg=c_bg_principal, width=25, fg=c_ecriture, font=('Helvitiva', 11), height=1)
            # self.__liste_widgets_pays_compare[indice - 1].append(self.__pays_donnees)
            self.__titre_pays.place(x=position_x_comparaison, y=position_y_comparaison)
            self.__pays_donnees.place(x=position_x_comparaison - 120, y=position_y_comparaison + 100)

            emplacement_label = 0
            sous_liste = []
            for i in range(0, 4 - self.__liste_pays_selectionnes.count("")):
                if i != (indice - 1):
                    distance = user.distance_coordonnees(user.format_coordonnees(donnees[id]["info"]),
                                                         user.format_coordonnees([donnees[pays]["info"] for pays in
                                                                                  donnees][i]))
                    self.__distance_km = tk.Label(self.__racine, text="Distance avec " +
                                                                      [donnees[pays]["nom_pays"] for pays in donnees][i]
                                                                      + " : " + str(distance) + " km",
                                                  bg=c_bg_principal, height=1, width=30, fg=c_ecriture,
                                                  font=('Helvitiva', 11), anchor='w')
                    sous_liste.append(self.__distance_km)
                    self.__distance_km.place(x=position_x_comparaison - 120,
                                             y=position_y_comparaison + 130 + emplacement_label * 30)
                    emplacement_label += 1

            self.__liste_widgets_pays_compare[indice - 1] = [self.__titre_pays, self.__pays_donnees, sous_liste]
            indice += 1

    def quadrillage(self) -> None:
        """
        Permet de placer un quadrillage sur l'écran (écran divisé en 4 parties égales).

        PRE : -
        POST : Place 2 tirets noir épais au centre de la fenêtre. L'un est placé horizontalement, l'autre verticalement,
        et ils traversent tous deux la fenêtre.
        """
        self.__dessin = tk.Canvas(self.__racine, bg=c_bg_principal, height=700, width=725)
        self.__dessin.place(x=0, y=0)
        self.__dessin.create_line(2, 350, 727, 350, fill="black", width=4)
        self.__dessin.create_line(362, 2, 362, 702, fill="black", width=4)

    def emplacement_podium(self, position: int, x: int, y: int) -> tk.Label:
        """
        Permet de créer et placer le numéro du podium du pays.

        PRE : 'position' représente la place sur le podium du pays. 'x' est la coordonnée x du titre du pays. 'y' est
        la coordonnée y du titre du pays.
        POST : Crée et place le numéro du pays dans le coin inférieur droit, et retourne le widget (pour pouvoir le
        supprimer le moment nécessaire).
        """
        numero_place = tk.Label(self.__racine, text=str(position), height=1, width=2, bg=c_bouton_principal,
                                fg=c_ecriture, font=('Helvitiva', 20), anchor='center', borderwidth=5, relief="ridge")
        numero_place.place(x=x + 186, y=y + 294)
        return numero_place

    def creer_pays(self) -> None:
        """
        Permet de placer les champs qui recevront les informations du pays à créer.

        PRE : -
        POST : Créer les différents champs ainsi que le bouton permettant d'ajouter le pays à la DB tcla.db.
        """
        self.remise_a_zero()

        liste = [["Entrez le code ISO\n3166-1 alpha-2 du pays : ", 21], ["Entrez le nom du pays : ", 21],
                 ["Entrez les coordonnées de la\ncapitale du pays : ", 24],
                 ["Entrez le nombre d'habitants\ndu pays en 2020 : ", 23],
                 ["Entrez la superficie du\npays (en km²) : ", 21], ["Entrez la densité du pays\n(en hab/km²): ", 21]]

        index = 0
        for champs in liste:
            self.__ajout_pays_info_entry = tk.Entry(show=None, textvariable=str(index), font=police_base, width=15)
            self.__ajout_pays_info_label = tk.Label(self.__racine, text=champs[0], height=2, width=champs[1],
                                                    bg=c_bg_principal, fg=c_ecriture, font=('Helvitiva', 13),
                                                    anchor='w', justify="left")
            self.__ajout_pays_info_entry.place(x=350, y=150 + index * 70)
            self.__ajout_pays_info_label.place(x=50, y=150 + index * 70)
            self.__liste_info_nv_pays[index] = [self.__ajout_pays_info_entry, self.__ajout_pays_info_label]
            index += 1

        self.__bouton_ajouter_pays = tk.Button(self.__racine, text="Ajouter", height=1, width=10, bg=c_bouton_principal,
                                               fg=c_ecriture, bd=1, activebackground=c_ecriture, font=police_base,
                                               activeforeground=c_bouton_principal, cursor=mouse,
                                               command=lambda: self.creation_pays())
        self.__bouton_ajouter_pays.place(x=510, y=580)

    def creation_pays(self) -> None:
        """
        Permet de vérifier les informations du nouveau pays ajoutées par l'utilisateur et d'ajouter le pays.

        PRE : -
        POST : Si les informations respectent les conventions, le pays est ajouté. Sinon des messages d'explications
        sont placés près des erreurs commises. Si un information respecte la convention, le carré à côté est vert.
        Sinon le carré est rouge.
        """
        for carre in self.__liste_carre_nv_pays:
            for info in carre:
                info.destroy()

        nbr_carres_corrects = 0

        ##
        if self.__liste_info_nv_pays[0][0].get().isalpha() and self.__liste_info_nv_pays[0][0].get().upper() not in \
                user.tous_pays() and len(self.__liste_info_nv_pays[0][0].get()) == 2:
            couleur = "green"
            nbr_carres_corrects += 1
        else:
            couleur = "red"
            self.__explication_pays_id = tk.Label(self.__racine, text="Format attendu : BE", height=1, width=15,
                                                  bg=c_bg_principal, fg="red", anchor='w', font=('Helvitiva', 11),
                                                  justify="left")
            self.__explication_pays_id.place(x=50, y=190)
        self.__ajout_pays_id_valid = tk.Canvas(self.__racine, width=10, height=10, borderwidth=0, highlightthickness=0,
                                               bg=couleur)
        self.__ajout_pays_id_valid.place(x=540, y=157)

        ##
        if "".join(re.split("[' -]", self.__liste_info_nv_pays[1][0].get())).isalpha():
            couleur = "green"
            nbr_carres_corrects += 1
        else:
            couleur = "red"
            self.__explication_pays_nom = tk.Label(self.__racine, text="Format attendu : Belgique",
                                                   height=1, width=19, bg=c_bg_principal, fg="red", anchor='w',
                                                   font=('Helvitiva', 11), justify="left")
            self.__explication_pays_nom.place(x=50, y=250)
        self.__ajout_pays_nom_valid = tk.Canvas(self.__racine, width=10, height=10, borderwidth=0, highlightthickness=0,
                                                bg=couleur)
        self.__ajout_pays_nom_valid.place(x=540, y=227)

        #
        if user.verif_coordonnees(self.__liste_info_nv_pays[2][0].get()):
            couleur = "green"
            nbr_carres_corrects += 1
        else:
            couleur = "red"
            self.__explication_pays_coo = tk.Label(self.__racine, text="Format attendu : 50 51 N 4 21 E",
                                                   height=1, width=23, bg=c_bg_principal, fg="red", anchor='w',
                                                   font=('Helvitiva', 11), justify="left")
            self.__explication_pays_coo.place(x=50, y=330)
        self.__ajout_pays_coo_valid = tk.Canvas(self.__racine, width=10, height=10, borderwidth=0, highlightthickness=0,
                                                bg=couleur)
        self.__ajout_pays_coo_valid.place(x=540, y=297)

        #
        if self.__liste_info_nv_pays[3][0].get().isnumeric():
            couleur = "green"
            nbr_carres_corrects += 1
        else:
            couleur = "red"
            self.__explication_pays_hab = tk.Label(self.__racine, text="Format attendu : 11476279",
                                                   height=1, width=20, bg=c_bg_principal, fg="red", anchor='w',
                                                   font=('Helvitiva', 11), justify="left")
            self.__explication_pays_hab.place(x=50, y=400)
        self.__ajout_pays_hab_valid = tk.Canvas(self.__racine, width=10, height=10, borderwidth=0, highlightthickness=0,
                                                bg=couleur)
        self.__ajout_pays_hab_valid.place(x=540, y=367)

        #
        if self.__liste_info_nv_pays[4][0].get().isnumeric():
            couleur = "green"
            nbr_carres_corrects += 1
        else:
            couleur = "red"
            self.__explication_pays_sup = tk.Label(self.__racine, text="Format attendu : 30688",
                                                   height=1, width=17, bg=c_bg_principal, fg="red", anchor='w',
                                                   font=('Helvitiva', 11), justify="left")
            self.__explication_pays_sup.place(x=50, y=470)
        self.__ajout_pays_sup_valid = tk.Canvas(self.__racine, width=10, height=10, borderwidth=0, highlightthickness=0,
                                                bg=couleur)
        self.__ajout_pays_sup_valid.place(x=540, y=437)

        #
        if self.__liste_info_nv_pays[5][0].get().isnumeric():
            couleur = "green"
            nbr_carres_corrects += 1
        else:
            couleur = "red"
            self.__explication_pays_dens = tk.Label(self.__racine, text="Format attendu : 374",
                                                    height=1, width=15, bg=c_bg_principal, fg="red", anchor='w',
                                                    font=('Helvitiva', 11), justify="left")
            self.__explication_pays_dens.place(x=50, y=540)
        self.__ajout_pays_dens_valid = tk.Canvas(self.__racine, width=10, height=10, borderwidth=0,
                                                 highlightthickness=0, bg=couleur)
        self.__ajout_pays_dens_valid.place(x=540, y=507)

        self.__liste_carre_nv_pays = [[self.__ajout_pays_id_valid, self.__explication_pays_id],
                                      [self.__ajout_pays_nom_valid, self.__explication_pays_nom],
                                      [self.__ajout_pays_coo_valid, self.__explication_pays_coo],
                                      [self.__ajout_pays_hab_valid, self.__explication_pays_hab],
                                      [self.__ajout_pays_sup_valid, self.__explication_pays_sup],
                                      [self.__ajout_pays_dens_valid, self.__explication_pays_dens]]

        if nbr_carres_corrects == 6:
            liste_coo = self.__liste_info_nv_pays[2][0].get().split()
            string = liste_coo[0] + "° " + liste_coo[1] + "' " + liste_coo[2] + ", " + liste_coo[3] + "° " + \
                     liste_coo[4] + "' " + liste_coo[5]
            nom_pays = user.format_nom_pays(self.__liste_info_nv_pays[1][0].get())
            self.ajouter_pays(self.__liste_info_nv_pays[0][0].get().upper(), nom_pays, string,
                              self.__liste_info_nv_pays[3][0].get(), self.__liste_info_nv_pays[4][0].get(),
                              self.__liste_info_nv_pays[5][0].get())

            self.remise_a_zero()
            self.initialisation()

    def ajouter_pays(self, id: str, nom: str, coo: str, hab: int, sup: int, dens: float) -> None:
        """
        Permet d'appeler une fonction qui ajoutera les nouvelles données du nouveau pays dans la DB tlca.db

        PRE : 'id' est une string représente le code code ISO 3166-1 alpha-2 du pays. 'nom' est une string
        représentant le nom du pays. 'coo' est une string représentant les coordonnées de la capitale du pays. 'hab'
        est un entier représentant le nombre d'habitants du pays en 2020. 'sup' est un entier représentant la superficie
        totale du pays. 'dens' est un nombre flotant représentant la densité du pays.
        POST : Appelle la fonction adéquate pour rajouter les données.
        """
        user.ajout_pays_client(id, nom, coo, hab, sup, dens)

    def menu_principal(self) -> None:
        """
        Permet d'aller au menu principal.

        PRE : -
        POST : Appelle une fonction supprimant tous les widgets puis la fonction représentant le menu principal.
        """
        self.remise_a_zero()
        self.initialisation()

    def menu_comparer(self) -> None:
        """
        Permet d'aller au menu de comparaison de pays.

        PRE : -
        POST : Appelle une fonction supprimant tous les widgets puis la fonction représentant le menu comparer.
        """
        self.remise_a_zero()
        self.comparer_pays()

    def menu_modifier(self) -> None:
        """
        Permet d'aller au menu d'ajout d'un pays.

        PRE : -
        POST : Appelle une fonction supprimant tous les widgets puis la fonction représentant le menu ajouter.
        """
        self.remise_a_zero()
        self.creer_pays()

    def remise_a_zero(self) -> None:
        """
        Supprime la plupart des widgets et des listes.

        PRE : -
        POST : Supprime tous les widgets et réinitialise les listes nécessaires.
        """
        # Widget menu
        self.__button_menu_comparaison.destroy()
        self.__button_ajouter_pays.destroy()

        # Choix des pays à comparer
        for widget in self.__liste_label_selection:
            if widget != "":
                for element in widget:
                    element.destroy()
        self.__liste_label_selection = ["", "", "", ""]
        self.__bouton_lancer_comparaison.destroy()
        for widget in self.__liste_labelframe:
            widget.destroy()
        self.__lb.destroy()
        self.__aucun_pays.destroy()
        for widget in self.__liste_type_comparaison:
            widget.destroy()
        for widget in self.__liste_widgets_pays_compare:
            for element in widget:
                if type(element) == list:
                    for km in element:
                        km.destroy()
                else:
                    element.destroy()
        self.__dessin.destroy()
        self.__liste_pays_selectionnes = ["", "", "", ""]

        # Widget dans l'option ajouter
        for widget in self.__liste_info_nv_pays:
            for element in widget:
                element.destroy()

        for widget in self.__liste_carre_nv_pays:
            for element in widget:
                element.destroy()

        self.__bouton_ajouter_pays.destroy()


Graphique()
