############################# programme jeu du Pierre Feuille Ciseaux ######################################

#importation des bibliothèques necéssaires
from tkinter import *
from random import *
from tkmacosx import Button

def game ():
    #création de la fenetre
    fenetre = Tk()
    fenetre.title("Pierre Feuille Ciseau")
    fenetre.config(bg='#e7caa8')
    #importation des images nécessaires
    pierre = PhotoImage(file="pierre.gif")
    feuille = PhotoImage(file="feuille.gif")
    ciseau = PhotoImage(file="ciseau.gif")
    exit = PhotoImage(file="quitter.gif")
    rejouer = PhotoImage(file="rejouer.gif")
    #scores
    global score
    score = 0
    global score_ordi
    score_ordi = 0
    #vérification si score = 3 pour trouver si il y as un gagnant
    def gagnant() :
        if score >= 3 :
            infobar.config(text = "Vous avez gagné !")
        elif score_ordi >= 3 :
            infobar.config(text = "L'ordinateur a gagné !")
    #fonction pour la case pierre
    def choix_pierre() :
        global score
        global score_ordi
        a = randint(1,3)
        if score >= 3 :
            return None
        if score_ordi >= 3 :
            return None
        if a == 1 :
            infobar.config(text="Vous avez choisis pierre et l'ordinateur aussi donc c'est égalité, aucun point pour personne rejouez !")
        if a == 2 :
            infobar.config(text="Vous avez choisis pierre et l'ordinateur a choisis feuille donc c'est Perdu ! +1 point pour l'ordinateur")
            score_ordi += 1
            aff_score_ordi.config(text="Score Adverse : "+str(score_ordi))
        if a == 3 :
            infobar.config(text="Vous avez choisis pierre et l'ordinateur a choisis ciseau donc c'est Gagné ! +1 point pour vous")
            score +=1
            aff_score.config(text="Votre Score : "+str(score))
        gagnant()
    #fonction pour la case feuille
    def choix_feuille() :
        global score
        global score_ordi
        a = randint(1,3)
        if score >= 3 :
            return None
        if score_ordi >= 3 :
            return None
        if a == 1 :
            infobar.config(text="Vous avez choisis feuille et l'ordinateur a choisis pierre donc c'est Gagné ! +1 point pour vous")
            score += 1
            aff_score.config(text="Votre Score : "+str(score))
        if a == 2 :
            infobar.config(text="Vous avez choisis feuille et l'ordinateur aussi donc c'est égalité, aucun point pour personne rejouez !")
        if a == 3 :
            infobar.config(text="Vous avez choisis feuille et l'ordinateur a choisis ciseau donc c'est Perdu ! +1 point pour l'ordinateur")
            score_ordi += 1
            aff_score_ordi.config(text="Score Adverse : "+str(score_ordi))
        gagnant()
    #fonction pour la case ciseau
    def choix_ciseau() :
        global score
        global score_ordi
        a = randint(1,3)
        if score >= 3 :
            return None
        if score_ordi >= 3 :
            return None
        if a == 1 :
            infobar.config(text="Vous avez choisis ciseau et l'ordinateur a choisis pierre donc c'est Perdu ! +1 point pour l'ordinateur")
            score_ordi +=1
            aff_score_ordi.config(text="Score Adverse : "+str(score_ordi))
        if a == 2 :
            infobar.config(text="Vous avez choisis ciseau et l'ordinateur a choisis feuille donc c'est Gagné ! +1 point pour vous")
            score +=1
            aff_score.config(text="Votre Score : "+str(score))
        if a == 3 :
            infobar.config(text="Vous avez choisis ciseau et l'ordinateur aussi donc c'est égalité, aucun point pour personne rejouez !")
        gagnant()
    #fonction pour remettre les scores a 0 et pouvoir rejouer
    def frejouer():
        global score
        global score_ordi
        score = 0
        score_ordi = 0
        aff_score.config(text="Votre Score : "+str(score))
        aff_score_ordi.config(text="Score Adverse : "+str(score_ordi))
        infobar.config(text="Cliquer sur une des cases pour jouer le signe que vous voulez, le premier a 3 points gagne !")
    #partie graphique: mise en place des frames, boutons et barre d'info
    frame1 = Frame(fenetre, bg='#e7caa8')
    frame1.pack(side=TOP, pady= 100)
    frame2 = Frame(fenetre, bg='#e7caa8')
    frame2.pack(expand=YES)
    frame3 = Frame(fenetre, bg='#e7caa8')
    frame3.pack(side=BOTTOM, pady=10)
    b1= Button(frame1, image=pierre, bg='black', height=200, width=200, command=choix_pierre).pack(side=LEFT, padx= 25)
    b2= Button(frame1, image=feuille, bg='black', height=200, width=200, command=choix_feuille).pack(side=LEFT, padx= 25)
    b3= Button(frame1, image=ciseau, bg='black', height=200, width=200, command=choix_ciseau).pack(side=LEFT, padx= 25)
    brejouer = Button(frame3, image=rejouer, bg='#e7caa8', height=40, width=40, command=frejouer).pack(side=LEFT, padx= 10)
    bquitter = Button(frame3, image=exit, bg='#e7caa8', height=40, width=40, command=fenetre.destroy).pack(side=LEFT)
    infobar = Label(frame2, text="Cliquer sur une des cases pour jouer le signe que vous voulez, le premier a 3 points gagne !", font=("Showcard Gothic", 15), bg='#e7caa8')
    infobar.pack(expand=YES, pady=15)
    aff_score = Label(frame2, text="Votre Score : "+str(score), font=("Showcard Gothic", 12), bg='#e7caa8', fg='green')
    aff_score.pack(pady=5)
    aff_score_ordi = Label(frame2, text="Score Adverse : "+str(score_ordi), font=("Showcard Gothic", 12), bg='#e7caa8', fg='red')
    aff_score_ordi.pack(pady=5)
    fenetre.mainloop()

#executer la fonction acceuil des le debut quand le programme se lance
game()
