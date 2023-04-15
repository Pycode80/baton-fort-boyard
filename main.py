from random import randint
import tkinter as tk
import pygame
from tkinter import Spinbox
import os
import sys


class JeuDesBatons(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("Jeu des bâtonnets")
        self.parent.resizable(width=False, height=False)
        self.grid(padx=10, pady=10)
        self.creer_widgets()

    def creer_widgets(self):
        self.lbl_batons = tk.Label(self, text="")
        self.lbl_batons.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        self.btn_joueur1 = tk.Button(self, text="Joueur 1", command=self.tour_joueur1)
        self.btn_joueur1.grid(row=1, column=0, padx=5, pady=5)
        self.btn_joueur2 = tk.Button(self, text="Joueur 2", command=self.tour_joueur2, state=tk.DISABLED)
        self.btn_joueur2.grid(row=1, column=1, padx=5, pady=5)
        self.lbl_resultat = tk.Label(self, text="")
        self.lbl_resultat.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.nbr_batons = randint(10, 30)
        self.lbl_batons.config(text=f"Il y a {self.nbr_batons} bâtonnets.")
        self.tour = 0

    def tour_joueur1(self):
        self.nbr_batons -= int(self.var_batons.get())
        self.lbl_batons.config(text=f"Il reste {self.nbr_batons} bâtonnets.")
        self.sp_nb_batons.delete(0, 'end')
        if self.nbr_batons <= 1:
            self.fin_de_partie()
        else:
            self.btn_joueur1.config(state=tk.DISABLED)
            self.btn_joueur2.config(state=tk.NORMAL)
            self.tour = 1

    def tour_joueur2(self):
        self.nbr_batons -= int(self.var_batons.get())
        self.lbl_batons.config(text=f"Il reste {self.nbr_batons} bâtonnets.")
        self.sp_nb_batons.delete(0, 'end')
        if self.nbr_batons <= 1:
            self.fin_de_partie()
        else:
            self.btn_joueur1.config(state=tk.NORMAL)
            self.btn_joueur2.config(state=tk.DISABLED)
            self.tour = 0


    def fin_de_partie(self):
        self.btn_joueur1.config(state=tk.DISABLED)
        self.btn_joueur2.config(state=tk.DISABLED)
        if self.tour == 0:
            self.lbl_resultat.config(text="Le joueur 1 a gagné.")
        else:
            self.lbl_resultat.config(text="Le joueur 2 a gagné.")

    def jouer(self):
        self.var_batons = tk.StringVar()
        self.var_batons.set(0)
        self.lbl_nb_batons = tk.Label(self, text="Combien de bâtonnets voulez-vous prendre (1-3) ?")
        self.lbl_nb_batons.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        self.sp_nb_batons = Spinbox(self, from_=1, to=3, textvariable=self.var_batons)
        self.sp_nb_batons.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        self.btn_valider = tk.Button(self, text="Valider", command=self.valider)
        self.btn_valider.grid(row=5, column=0, columnspan=2, padx=5, pady=5)


    def valider(self):
        if int(self.var_batons.get()) in [1, 2, 3]:
            if self.tour == 0:
                self.tour_joueur1()
            else:
                self.tour_joueur2()
        else:
            self.lbl_resultat.config(text="Veuillez entrer un nombre entre 1 et 3.")

# Création de la fenêtre principale
fenetre = tk.Tk()
jeu = JeuDesBatons(fenetre)
jeu.jouer()
pygame.init()



def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
musique = pygame.mixer.Sound(resource_path('musique.wav'))
musique.play(-1)

fenetre.mainloop()
