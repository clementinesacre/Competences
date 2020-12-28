import tkinter as tk
from creation_db import utilisation_db as udb
from web import client
from web import user

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
    def __init__(self):
        self.__racine = tk.Tk(className='projet')
        self.__canv = tk.Canvas(self.__racine, bg=c_bg_principal, height=700, width=725)
        self.__canv.pack()

        # à supprimer à terme
        def donothing():
            filewin = tk.Toplevel(self.__racine)
            button = tk.Button(filewin, text="Do nothing button")
            button.pack()

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
        self.__button_pays = tk.Button()
        self.__barre_recherche = tk.Label()
        self.__lb = tk.Listbox()
        self.__liste_pays_selectionnes = ["", "", "", ""]
        self.__bouton_retirer = tk.Button()
        self.__liste_label_selection = ["", "", "", ""]
        self.__bouton_lancer_comparaison = tk.Button()
        self.__pays_choisi = tk.Label()
        self.__pays1 = tk.LabelFrame()
        self.__pays2 = tk.LabelFrame()
        self.__pays3 = tk.LabelFrame()
        self.__pays4 = tk.LabelFrame()
        self.__entree_utilisateur = tk.Entry()
        self.__bouton_comparer_habitants = tk.Button()
        self.__bouton_comparer_superficie = tk.Button()
        self.__bouton_comparer_coordonnees = tk.Button()
        self.__choix_comparaison = tk.Label()
        self.__titre_pays = tk.Label()
        self.__liste_widgets_pays_compare = ["", "", "", ""]
        self.__pays_donnees = tk.Label()
        self.__pays_densite = tk.Label()
        self.__cadre_place = tk.Canvas()
        self.__numero_place = tk.Label()
        self.__distance_km = tk.Label()
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

        self.initialisation()

    def initialisation(self):
        self.__button_menu_comparaison = tk.Button(self.__racine, text="Comparer des pays", height=2, width=16,
                                                   bg=c_bouton_principal,
                                                   fg=c_ecriture, bd=1, activebackground=c_ecriture,
                                                   activeforeground=c_bouton_principal, font=police_base,
                                                   cursor=mouse, command=lambda: self.comparer_pays())
        self.__button_pays = tk.Button(self.__racine, text="Ajouter un pays", height=2, width=16, bg=c_bouton_principal,
                                       fg=c_ecriture, bd=1, activebackground=c_ecriture,
                                       activeforeground=c_bouton_principal, cursor=mouse,
                                       command=lambda: self.ajouter_pays(), font=police_base)
        self.__button_menu_comparaison.place(x=275, y=250)
        self.__button_pays.place(x=275, y=350)

        self.__racine.mainloop()

    def comparer_pays(self):
        self.__button_menu_comparaison.destroy()
        self.__button_pays.destroy()

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
        self.__entree_utilisateur = tk.Entry(show=None, textvariable=value, font=police_base, width=15)
        self.__entree_utilisateur.place(x=12, y=60)

        def on_change(a, b, c):
            value.get()
            self.afficher_liste_pays(self.__entree_utilisateur.get())

        value.trace('w', on_change)

    def afficher_liste_pays(self, lettres):
        pays_correspondants = sorted(list(user.un_pays(lettres).values()))
        var = tk.StringVar(value=pays_correspondants)
        self.__lb.destroy()
        self.__lb = tk.Listbox(self.__racine, listvariable=var, selectmode='extended')

        if lettres == "":
            self.__lb.destroy()
        else:
            self.__lb.place(x=12, y=86)
            self.__lb.bind('<<ListboxSelect>>', lambda x: self.afficher_pays_choisi())

    def afficher_pays_choisi(self):
        pays_selectionne = self.__lb.curselection()[0]

        if self.__liste_pays_selectionnes[0] == "":
            self.__liste_pays_selectionnes[0] = self.__lb.get(pays_selectionne)
            self.__pays_choisi = tk.Label(self.__racine, text=self.__lb.get(pays_selectionne), bg=c_ecriture, height=1,
                                          width=13, fg=c_ligne_label_frame, font=police_base)
            self.__pays_choisi.place(x=25 + position_x_pays_place, y=55)
            self.__bouton_retirer = tk.Button(self.__racine, text="Supprimer", height=1, width=12,
                                              bg=c_bouton_principal, fg=c_ecriture, bd=1, activebackground=c_ecriture,
                                              activeforeground=c_bouton_principal,
                                              cursor=mouse, font=('Helvitiva', 10),
                                              command=lambda: self.retirer_choix(0))
            self.__bouton_retirer.place(x=position_x_pays_place + 7, y=98)
            self.__liste_label_selection[0] = [self.__pays_choisi, self.__bouton_retirer]

        elif self.__liste_pays_selectionnes[1] == "":
            self.__liste_pays_selectionnes[1] = self.__lb.get(pays_selectionne)
            self.__pays_choisi = tk.Label(self.__racine, text=self.__lb.get(pays_selectionne), bg=c_ecriture, height=1,
                                          width=13, fg=c_ligne_label_frame, font=police_base)
            self.__pays_choisi.place(x=25 + position_x_pays_place, y=55 + 1 * espace_y_pays_place)
            self.__bouton_retirer = tk.Button(self.__racine, text="Supprimer", height=1, width=12,
                                              bg=c_bouton_principal, fg=c_ecriture, bd=1, activebackground=c_ecriture,
                                              activeforeground=c_bouton_principal,
                                              cursor=mouse, font=('Helvitiva', 10),
                                              command=lambda: self.retirer_choix(1))
            self.__bouton_retirer.place(x=position_x_pays_place + 7, y=98 + 1 * espace_y_pays_place)
            self.__liste_label_selection[1] = [self.__pays_choisi, self.__bouton_retirer]

        elif self.__liste_pays_selectionnes[2] == "":
            self.__liste_pays_selectionnes[2] = self.__lb.get(pays_selectionne)
            self.__pays_choisi = tk.Label(self.__racine, text=self.__lb.get(pays_selectionne), bg=c_ecriture, height=1,
                                          width=13, fg=c_ligne_label_frame, font=police_base)
            self.__pays_choisi.place(x=25 + position_x_pays_place, y=55 + 2 * espace_y_pays_place)
            self.__bouton_retirer = tk.Button(self.__racine, text="Supprimer", height=1, width=12,
                                              bg=c_bouton_principal, fg=c_ecriture, bd=1, activebackground=c_ecriture,
                                              activeforeground=c_bouton_principal,
                                              cursor=mouse, font=('Helvitiva', 10),
                                              command=lambda: self.retirer_choix(2))
            self.__bouton_retirer.place(x=position_x_pays_place + 7, y=98 + 2 * espace_y_pays_place)
            self.__liste_label_selection[2] = [self.__pays_choisi, self.__bouton_retirer]

        elif self.__liste_pays_selectionnes[3] == "":
            self.__liste_pays_selectionnes[3] = self.__lb.get(pays_selectionne)
            self.__pays_choisi = tk.Label(self.__racine, text=self.__lb.get(pays_selectionne), bg=c_ecriture, height=1,
                                          width=13, fg=c_ligne_label_frame, font=police_base)
            self.__pays_choisi.place(x=25 + position_x_pays_place, y=55 + 3 * espace_y_pays_place)
            self.__bouton_retirer = tk.Button(self.__racine, text="Supprimer", height=1, width=12,
                                              bg=c_bouton_principal, fg=c_ecriture, bd=1, activebackground=c_ecriture,
                                              activeforeground=c_bouton_principal,
                                              cursor=mouse, font=('Helvitiva', 10),
                                              command=lambda: self.retirer_choix(3))
            self.__bouton_retirer.place(x=position_x_pays_place + 7, y=98 + 3 * espace_y_pays_place)
            self.__liste_label_selection[3] = [self.__pays_choisi, self.__bouton_retirer]

        if self.__liste_pays_selectionnes.count("") <= 2:
            self.__bouton_lancer_comparaison.destroy()
            self.__bouton_lancer_comparaison = tk.Button(self.__racine, text="Comparer", height=1, width=12,
                                                         bg=c_bouton_principal, activebackground=c_ecriture,
                                                         fg=c_ecriture, bd=1, activeforeground=c_bouton_principal,
                                                         cursor=mouse, font=police_base,
                                                         command=lambda: self.type_comparaison())
            self.__bouton_lancer_comparaison.place(x=580, y=550)

    def retirer_choix(self, indice):
        self.__liste_label_selection[indice][0].destroy()
        self.__liste_label_selection[indice][1].destroy()
        self.__liste_label_selection[indice] = ""
        self.__liste_pays_selectionnes[indice] = ""
        if self.__liste_pays_selectionnes.count("") > 2:
            self.__bouton_lancer_comparaison.destroy()

    def type_comparaison(self):
        nbr_pays_choisis = 4 - self.__liste_pays_selectionnes.count("")
        for i in range(nbr_pays_choisis):
            self.__liste_label_selection[i][0].destroy()
            self.__liste_label_selection[i][1].destroy()
            self.__bouton_lancer_comparaison.destroy()
        self.__pays1.destroy()
        self.__pays2.destroy()
        self.__pays3.destroy()
        self.__pays4.destroy()
        self.__barre_recherche.destroy()
        self.__entree_utilisateur.destroy()
        self.__lb.destroy()

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

    def comparaison_finale(self, type):
        self.__choix_comparaison.destroy()
        self.__bouton_comparer_habitants.destroy()
        self.__bouton_comparer_superficie.destroy()
        self.__bouton_comparer_coordonnees.destroy()

        if type == "habitants":
            self.comparaison_habitants()
        elif type == "superficie":
            self.comparaison_superficie()
        elif type == "distance":
            self.comparaison_distance()

    def comparaison_habitants(self):
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

    def comparaison_superficie(self):
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

    def comparaison_distance(self):
        liste_choix = self.__liste_pays_selectionnes + ["coordonnee"]
        donnees = user.caracteristique_pays(liste_choix)
        self.quadrillage()

        podium = user.tri(donnees, "info")

        indice = 1
        for id in donnees:
            self.__liste_widgets_pays_compare[indice - 1] = []
            position_x_comparaison, position_y_comparaison = user.coordonnees_affichage_4_pays(indice)
            self.__titre_pays = tk.Label(self.__racine, text=donnees[id]["nom_pays"], bg=c_bg_principal,
                                         height=1, width=15, fg=c_ecriture, font=('Helvitiva', 16), anchor='w')
            self.__liste_widgets_pays_compare[indice - 1].append(self.__titre_pays)
            self.__pays_donnees = tk.Label(self.__racine, text="Coordonnee : " + str(donnees[id]["info"]), anchor='w',
                                           bg=c_bg_principal, width=25, fg=c_ecriture, font=('Helvitiva', 11), height=1)
            self.__liste_widgets_pays_compare[indice - 1].append(self.__pays_donnees)
            self.__titre_pays.place(x=position_x_comparaison, y=position_y_comparaison)
            self.__pays_donnees.place(x=position_x_comparaison - 120, y=position_y_comparaison + 100)

            emplacement_label = 0
            for i in range(0, 4 - self.__liste_pays_selectionnes.count("")):
                if i != (indice - 1):
                    distance = user.distance_coordonnees(user.format_coordoonnees(donnees[id]["info"]),
                                                         user.format_coordoonnees([donnees[pays]["info"] for pays in
                                                                                   donnees][i]))
                    self.__distance_km = tk.Label(self.__racine, text="Distance avec " +
                                                                      [donnees[pays]["nom_pays"] for pays in donnees][i]
                                                                      + " : " + str(distance) + " km",
                                                  bg=c_bg_principal, height=1, width=30, fg=c_ecriture,
                                                  font=('Helvitiva', 11), anchor='w')
                    self.__liste_widgets_pays_compare[indice - 1].append(self.__distance_km)
                    self.__distance_km.place(x=position_x_comparaison - 120,
                                             y=position_y_comparaison + 130 + emplacement_label * 30)
                    emplacement_label += 1

            indice += 1

    def quadrillage(self):
        dessin = tk.Canvas(self.__racine, bg=c_bg_principal, height=700, width=725)
        dessin.place(x=0, y=0)
        dessin.create_line(2, 350, 727, 350, fill="black", width=4)
        dessin.create_line(362, 2, 362, 702, fill="black", width=4)

    def emplacement_podium(self, position, x, y):
        numero_place = tk.Label(self.__racine, text=str(position), height=1, width=2, bg=c_bouton_principal,
                                fg=c_ecriture, font=('Helvitiva', 20), anchor='center', borderwidth=5, relief="ridge")
        numero_place.place(x=x + 186, y=y + 294)
        return numero_place

    def ajouter_pays(self):
        self.__button_menu_comparaison.destroy()
        self.__button_pays.destroy()

        self.__ajout_pays_id_entry = tk.Entry(show=None, textvariable="test", font=police_base, width=15)
        self.__ajout_pays_id_label = tk.Label(self.__racine, text="Entrez le code ISO \n 3166-1 alpha-2 du pays : ",
                                              height=2, width=21, bg=c_bg_principal, fg=c_ecriture,
                                              font=('Helvitiva', 13), anchor='w')
        self.__ajout_pays_id_entry.place(x=350, y=150)
        self.__ajout_pays_id_label.place(x=50, y=150)

        self.__ajout_pays_nom_entry = tk.Entry(show=None, textvariable="test", font=police_base, width=15)
        self.__ajout_pays_nom_label = tk.Label(self.__racine, text="Entrez le nom du pays : ", height=2, width=21,
                                               bg=c_bg_principal, fg=c_ecriture, font=('Helvitiva', 13), anchor='w')
        self.__ajout_pays_nom_entry.place()
        self.__ajout_pays_nom_label.place(x=50, y=210)

        self.__ajout_pays_coo_entry = tk.Entry(show=None, textvariable="test", font=police_base, width=15)
        self.__ajout_pays_coo_label = tk.Label(self.__racine, text="Entrez les coordonnées de la capitale du pays : ",
                                               height=2, width=21, bg=c_bg_principal, fg=c_ecriture, anchor='w',
                                               font=('Helvitiva', 13))
        self.__ajout_pays_coo_entry.place()
        self.__ajout_pays_coo_label.place(x=50, y=270)

        self.__ajout_pays_hab_entry = tk.Entry(show=None, textvariable="test", font=police_base, width=15)
        self.__ajout_pays_hab_label = tk.Label(self.__racine, text="Entrez le nombre d'habitants du pays en 2020 : ",
                                               height=2, width=21, bg=c_bg_principal, fg=c_ecriture, anchor='w',
                                               font=('Helvitiva', 13))
        self.__ajout_pays_hab_entry.place()
        self.__ajout_pays_hab_label.place(x=50, y=330)

        self.__ajout_pays_sup_entry = tk.Entry(show=None, textvariable="test", font=police_base, width=15)
        self.__ajout_pays_sup_label = tk.Label(self.__racine, text="Entrez la superficie du pays (en km²) : ", height=2,
                                               width=21, bg=c_bg_principal, fg=c_ecriture, font=('Helvitiva', 13),
                                               anchor='w')
        self.__ajout_pays_sup_entry.place()
        self.__ajout_pays_sup_label.place(x=50, y=390)

        self.__ajout_pays_dens_entry = tk.Entry(show=None, textvariable="test", font=police_base, width=15)
        self.__ajout_pays_dens_label = tk.Label(self.__racine, text="Entrez la densité du pays (en hab/km²): ",
                                                height=2, width=21, bg=c_bg_principal, fg=c_ecriture, anchor='w',
                                                font=('Helvitiva', 13))
        self.__ajout_pays_dens_entry.place()
        self.__ajout_pays_dens_label.place(x=50, y=450)

        """id_pays
        coordonnee
        habitants_2020
        superficie
        densite"""

    def menu_principal(self):
        self.initialisation()

    def menu_comparer(self):
        pass

    def menu_modifier(self):
        pass


Graphique()
