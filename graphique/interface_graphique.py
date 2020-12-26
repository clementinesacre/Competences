import tkinter as tk
from creation_db import utilisation_db as udb
from web import client

position_x_pays_place = 500
position_y_pays_place = 20
espace_y_pays_place = 130


class Graphique:
    def __init__(self):
        self.__racine = tk.Tk(className='Application')
        self.__canv = tk.Canvas(self.__racine, bg="#424142", height=700, width=725)
        self.__canv.pack()

        # initialisation des widgets
        self.__button_menu_comparaison = tk.Button()
        self.__button_pays = tk.Button()
        self.__barre_recherche = tk.Label()
        self.__lb = tk.Listbox(self.__racine, listvariable=[], selectmode='extended')
        self.__liste_pays_selectionnes = ["", ""]
        self.__bouton_retirer = tk.Button()
        self.__liste_label_selection = ["", ""]
        self.__bouton_lancer_comparaison = tk.Button()
        self.__pays_choisi = tk.Label()
        self.__pays1 = tk.LabelFrame()
        self.__pays2 = tk.LabelFrame()
        self.__entree_utilisateur = tk.Entry()
        self.__bouton_comparer_habitants = tk.Button()
        self.__bouton_comparer_superficie = tk.Button()
        self.__bouton_comparer_coordonnees = tk.Button()
        self.__choix_comparaison = tk.Label()

        self.initialisation()

    def initialisation(self):
        self.__button_menu_comparaison = tk.Button(self.__racine, text="Comparer des pays", height=2, width=16,
                                                   bg='#E8BAE5',
                                                   fg='#FFFFFF', bd=1, activebackground='#FFFFFF',
                                                   activeforeground='#E8BAE5', font=('Helvitiva', 15),
                                                   cursor='circle', command=lambda: self.comparer_pays())
        self.__button_pays = tk.Button(self.__racine, text="Ajouter un pays", height=2, width=16, bg='#E8BAE5',
                                       fg='#FFFFFF', bd=1, activebackground='#FFFFFF', activeforeground='#E8BAE5',
                                       cursor='circle', command=lambda: self.ajouter_pays(), font=('Helvitiva', 15))
        self.__button_menu_comparaison.place(x=275, y=250)
        self.__button_pays.place(x=275, y=350)

        self.__racine.mainloop()

    def comparer_pays(self):
        self.__button_menu_comparaison.destroy()
        self.__button_pays.destroy()

        self.__pays1 = tk.LabelFrame(self.__racine, text="Pays 1 :", bg='#424142', width=200, height=110, fg='#FFFFFF',
                                     font=('Helvitiva', 15))
        self.__pays1.place(x=position_x_pays_place, y=position_y_pays_place)
        self.__pays2 = tk.LabelFrame(self.__racine, text="Pays 2 :", bg='#424142', width=200, height=110, fg='#FFFFFF',
                                     font=('Helvitiva', 15))
        self.__pays2.place(x=position_x_pays_place, y=position_y_pays_place + 1 * espace_y_pays_place)

        self.__barre_recherche = tk.Label(self.__racine, text="Chercher le pays :", bg='#424142', height=2, width=15,
                                          fg='#FFFFFF', font=('Helvitiva', 15))
        self.__barre_recherche.place(x=11, y=15)

        value = tk.StringVar()
        value.set("")
        self.__entree_utilisateur = tk.Entry(show=None, textvariable=value, font=('Helvitiva', 15), width=15)
        self.__entree_utilisateur.place(x=12, y=60)

        def on_change(a, b, c):
            value.get()
            self.afficher_liste_pays(self.__entree_utilisateur.get())

        value.trace('w', on_change)

    def afficher_liste_pays(self, lettres):
        pays_correspondants = sorted(list(client.client_function("pays " + lettres).values()))
        var = tk.StringVar(value=pays_correspondants)
        self.__lb.destroy()
        self.__lb = tk.Listbox(self.__racine, listvariable=var, selectmode='extended')

        if lettres == "":
            self.__lb.destroy()
        else:
            self.__lb.place(x=12, y=86)
            self.__lb.bind('<<ListboxSelect>>', lambda x: self.afficher_pays_choisi())

        # #label = tk.Label(self.__racine)
        # #label.place(x=100, y=150)

    def afficher_pays_choisi(self):
        pays_selectionne = self.__lb.curselection()[0]

        if self.__liste_pays_selectionnes[0] == "":
            self.__liste_pays_selectionnes[0] = pays_selectionne
            self.__pays_choisi = tk.Label(self.__racine, text=self.__lb.get(pays_selectionne), bg='#FFFFFF', height=1,
                                          width=13, fg='#000000', font=('Helvitiva', 15))
            self.__pays_choisi.place(x=25 + position_x_pays_place, y=55)
            self.__bouton_retirer = tk.Button(self.__racine, text="Supprimer", height=1, width=12, bg='#E8BAE5',
                                              fg='#FFFFFF', bd=1, activebackground='#FFFFFF',
                                              activeforeground='#E8BAE5',
                                              cursor='circle', font=('Helvitiva', 10),
                                              command=lambda: self.retirer_choix(0))
            self.__bouton_retirer.place(x=position_x_pays_place + 7, y=98)
            self.__liste_label_selection[0] = [self.__pays_choisi, self.__bouton_retirer]

        elif self.__liste_pays_selectionnes[1] == "":
            self.__liste_pays_selectionnes[1] = pays_selectionne
            self.__pays_choisi = tk.Label(self.__racine, text=self.__lb.get(pays_selectionne), bg='#FFFFFF', height=1,
                                          width=13, fg='#000000', font=('Helvitiva', 15))
            self.__pays_choisi.place(x=25 + position_x_pays_place, y=55 + espace_y_pays_place)
            self.__bouton_retirer = tk.Button(self.__racine, text="Supprimer", height=1, width=12, bg='#E8BAE5',
                                              fg='#FFFFFF', bd=1, activebackground='#FFFFFF',
                                              activeforeground='#E8BAE5',
                                              cursor='circle', font=('Helvitiva', 10),
                                              command=lambda: self.retirer_choix(1))
            self.__bouton_retirer.place(x=position_x_pays_place + 7, y=98 + espace_y_pays_place)
            self.__liste_label_selection[1] = [self.__pays_choisi, self.__bouton_retirer]

        if self.__liste_pays_selectionnes[0] != "" and self.__liste_pays_selectionnes[1] != "":
            self.__bouton_lancer_comparaison.destroy()
            self.__bouton_lancer_comparaison = tk.Button(self.__racine, text="Comparer", height=1, width=12,
                                                         bg='#E8BAE5', fg='#FFFFFF', bd=1, activebackground='#FFFFFF',
                                                         activeforeground='#E8BAE5',
                                                         cursor='circle', font=('Helvitiva', 15),
                                                         command=lambda: self.type_comparaison())
            self.__bouton_lancer_comparaison.place(x=580, y=300)

    def retirer_choix(self, indice):
        self.__liste_label_selection[indice][0].destroy()
        self.__liste_label_selection[indice][1].destroy()
        self.__liste_label_selection[indice] = ""
        self.__liste_pays_selectionnes[indice] = ""
        self.__bouton_lancer_comparaison.destroy()

    def type_comparaison(self):
        self.retirer_choix(0)
        self.retirer_choix(1)
        self.__pays1.destroy()
        self.__pays2.destroy()
        self.__barre_recherche.destroy()
        self.__entree_utilisateur.destroy()
        self.__lb.destroy()

        self.__choix_comparaison = tk.Label(self.__racine, text="Choisir le type de comparaison =", bg='#FFFFFF',
                                            height=1, width=13, fg='#000000', font=('Helvitiva', 15))
        self.__choix_comparaison.place()

        self.__bouton_comparer_habitants = tk.Button(self.__racine, text="Habitants", height=1, width=12, bg='#E8BAE5',
                                                     fg='#FFFFFF', bd=1, activebackground='#FFFFFF', cursor='circle',
                                                     activeforeground='#E8BAE5', font=('Helvitiva', 15),
                                                     command=lambda: self.comparaison_finale('habitants'))
        self.__bouton_comparer_habitants.place()
        self.__bouton_comparer_superficie = tk.Button(self.__racine, text="Habitants", height=1, width=12, bg='#E8BAE5',
                                                      fg='#FFFFFF', bd=1, activebackground='#FFFFFF', cursor='circle',
                                                      activeforeground='#E8BAE5', font=('Helvitiva', 15),
                                                      command=lambda: self.comparaison_finale('superficie'))
        self.__bouton_comparer_superficie.place()
        self.__bouton_comparer_coordonnees = tk.Button(self.__racine, text="Habitants", height=1, width=12,
                                                       bg='#E8BAE5',
                                                       fg='#FFFFFF', bd=1, activebackground='#FFFFFF', cursor='circle',
                                                       activeforeground='#E8BAE5', font=('Helvitiva', 15),
                                                       command=lambda: self.comparaison_finale('distance'))
        self.__bouton_comparer_coordonnees.place()

    def comparaison_finale(self, type):
        pass

    def ajouter_pays(self):
        pass


Graphique()
