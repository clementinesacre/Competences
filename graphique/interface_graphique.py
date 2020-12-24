import tkinter as tk


class Graphique:
    def __init__(self):
        self.__racine = tk.Tk(className='Application')
        self.__canv = tk.Canvas(self.__racine, bg="#E7EBD6", height=500, width=525)
        self.__canv.pack()