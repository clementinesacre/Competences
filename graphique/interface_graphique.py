import tkinter as tk
from creation_db import utilisation_db as udb


class Graphique:
    def __init__(self):
        self.__racine = tk.Tk(className='Application')
        # F3F3F3
        self.__canv = tk.Canvas(self.__racine, bg="#424142", height=700, width=725)
        self.__canv.pack()

        self.initialisation()

        self.__button_comparaison = tk.Button()
        self.__button_pays = tk.Button()
        self.__barre_recherche = tk.Label()
        self.__lb = ""

    def initialisation(self):
        self.__button_comparaison = tk.Button(self.__racine, text="Comparer des pays", height=2, width=15, bg='#E8BAE5',
                                              fg='#FFFFFF', bd=1, activebackground='#FFFFFF',
                                              activeforeground='#E8BAE5',
                                              cursor='circle', command=lambda: self.comparer_pays())
        self.__button_pays = tk.Button(self.__racine, text="Ajouter un pays", height=2, width=15, bg='#E8BAE5',
                                       fg='#FFFFFF', bd=1, activebackground='#FFFFFF', activeforeground='#E8BAE5',
                                       cursor='circle', command=lambda: self.ajouter_pays())
        self.__button_comparaison.place(x=300, y=270)
        self.__button_pays.place(x=300, y=350)

        self.__racine.mainloop()

    def comparer_pays(self):
        self.__button_comparaison.destroy()
        self.__button_pays.destroy()

        self.__lb = tk.Listbox(self.__racine, listvariable=[], selectmode='extended')

        self.__barre_recherche = tk.Label(self.__racine, text="Chercher le pays :", bg='#424142', height=2, width=13,
                                          fg='#FFFFFF')
        self.__barre_recherche.place(x=10, y=15)

        value = tk.StringVar()
        value.set("")
        entree = tk.Entry(show=None, textvariable=value, font=('Arial', 14), width=15)
        entree.place(x=11, y=50)

        def on_change(a, b, c):
            value.get()
            self.afficher_liste_pays(entree.get())

        value.trace('w', on_change)

    def afficher_liste_pays(self, lettres):
        kk = list(udb.info_pays(lettres).values())
        var = tk.StringVar(value=kk)
        self.__lb.destroy()
        self.__lb = tk.Listbox(self.__racine, listvariable=var, selectmode='extended')

        if lettres == "":
            self.__lb.destroy()
        else:
            self.__lb.place(x=11, y=76)

        # #label = tk.Label(self.__racine)
        # #label.place(x=100, y=150)

        # lb.bind('<<ListboxSelect>>', cb)

    def ajouter_pays(self):
        pass


Graphique()
