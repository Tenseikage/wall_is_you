import fltk as tk
from random import choice, randint
import sys




class Button:
    """
    Classe permettant de gérer les boutons
    """

    def __init__(self, coordxplace, coordyplace, xtaille, ytaille, image_button, tag,scale):
        self.coordxplace = coordxplace
        self.coordyplace = coordyplace
        self.xtaille = xtaille
        self.ytaille = ytaille
        self.image_button = image_button
        self.tag = tag
        self.scale = scale


    def get_coordsplace(self):
        """
        Retourne les coordonnées x (abcisses) et y (ordonée) de là où est placé le bouton
        """
        return self.coordxplace, self.coordyplace


    def get_coords(self):
        """
        Renvoie les coordonnées x et y minimale du bouton
        """
        return self.coordxplace - self.xtaille // 2, self.coordyplace - self.ytaille // 2


    def get_taille(self):
        """
        Renvoie la taille de l'image
        """
        return self.xtaille, self.ytaille


    def create_button1(self):
        """
        Créer le button à partir d'une image avec pour point d'ancrage le milieu
        """
        tk.image(self.coordxplace, self.coordyplace, self.image_button,largeur = 100*self.scale//600,hauteur = 100*self.scale//600, tag = self.tag)


    def create_button2(self):
        """
        Créer le button à partir d'une image avec pour point d'ancrage le milieu
        """
        tk.image(self.coordxplace, self.coordyplace, self.image_button,largeur = 200*self.scale//600,hauteur = 75*self.scale//600, tag = self.tag)

    def destroy_button(self):
        """
        Efface le bouton
        """
        tk.efface(self.tag)

    
    def is_touched(self, coords):
        """
        Vérifie si le boutton est cliqué
        
        """
        x, y = coords
        if (self.get_coords()[0] < x < self.get_coords()[0] +
            self.xtaille and self.get_coords()[1] < y <
            self.get_coords()[1] + self.ytaille):
            return True


def present_text(string,centre,taille_x,taille_y,police):
        """Cette fonction permet de cadrer le texte de présentation"""
        a= centre[0]-taille_x
        b= centre[1]-taille_y
        c = centre[0]+taille_x
        d = centre[1]+taille_y
        tk.texte(a+(c-a)//2,b+(d-b)//2,chaine=string,taille=police,couleur= 'black', ancrage='center',
    	      tag = 'text')
        

def menu(scale):
    """
    Menu de jeu avec création des boutons jouer et quitter 
    et gestion des évènements des souris lors du clic sur un des boutons
    """
    buttonjouer = Button(300*scale//600, 200*scale//600, 200*scale//600, 75*scale//600, 'fichiers_wall_is_you/media/jouer.gif', 'jouer',scale)
    buttonquitter = Button(300*scale//600, 350*scale//600, 200*scale//600, 75*scale//600, 'fichiers_wall_is_you/media/quitter.gif', 'quitter',scale)
    buttonjouer.create_button2() # creation du bouton jouer
    buttonquitter.create_button2() # creration du bouton quitter
    tk.mise_a_jour()
    choosing_event = True
    while choosing_event:
        event = tk.donne_ev()
        tev = tk.type_ev(event)
        tk.mise_a_jour()
        if tev == "ClicGauche": # Regarde si le clique gauche a été apuuyé
            coords_clickx, coords_clicky = tk.abscisse(event), tk.ordonnee(event)
            if buttonjouer.is_touched((coords_clickx,coords_clicky)):
            # Regarde si le clique à été effectué sur le bouton jouer
                buttonjouer.destroy_button()
                buttonquitter.destroy_button()
                return True
            if buttonquitter.is_touched((coords_clickx,coords_clicky)):
            # Regarde si le bouton quitter a été appuyé
                buttonjouer.destroy_button()
                buttonquitter.destroy_button()
                sys.exit()
        
def menu2(scale):
    """
    Menu du jeu avec ajout d'un fond pour le plateau et 
    de boutons pour permettre au joueur de choisir le jeu
    """
    tk.rectangle(0, 0, 1000, 1000, '', '#eee2b0', 0, 'background')
    present_text('Choisissez un donjon ', (300*scale//600, 100*scale//600), 300*scale//600, 400*scale//600,30*scale//600)
    buttonred = []
    choice_dungeon = ['map_test','map1','map2','map3','map4']
    for i in range(5):
        button = Button((60*scale//600) + (120*scale//600)*i, 250*scale//600, 101*scale//600, 101*scale//600, 'fichiers_wall_is_you/media/'+choice_dungeon[i]+'.png', 'red',scale)
        button.create_button1()
        buttonred.append(button)
        if i == 0:
            present_text('Donjon \n test', ((60*scale//600)+(120*scale//600)*i, 350*scale//600), 200*scale//600, 100*scale//600,20*scale//600)
        else:
           present_text(f'Donjon{i}', ((60*scale//600)+(120*scale//600)*i, 350*scale//600), 200*scale//600, 100*scale//600,20*scale//600)
    tk.mise_a_jour()   
    choosing_event = True
    while choosing_event:
        event = tk.donne_ev()
        tev = tk.type_ev(event)
        tk.mise_a_jour()
        if tev == "ClicGauche": # Regarde si le clique gauche a été apuuyé
            coords_clickx, coords_clicky = tk.abscisse(event), tk.ordonnee(event)
            if buttonred[0].is_touched((coords_clickx,coords_clicky)):
                for b in buttonred:
                    b.destroy_button()
                    tk.efface('text')
                return 'map_test'
            if buttonred[1].is_touched((coords_clickx,coords_clicky)):
                for b in buttonred:
                    b.destroy_button()
                    tk.efface('text')
                return 'map1'
            if buttonred[2].is_touched((coords_clickx,coords_clicky)):
                for b in buttonred:
                    b.destroy_button()
                    tk.efface('text')
                return 'map2'
            if buttonred[3].is_touched((coords_clickx,coords_clicky)):
                for b in buttonred:
                    b.destroy_button()
                    tk.efface('text')
                return 'map3'
            if buttonred[4].is_touched((coords_clickx,coords_clicky)):
                for b in buttonred:
                    b.destroy_button()
                    tk.efface('text')
                return 'map4'
        if tev == 'Touche':
            if tk.touche(event) == 'w':
                sys.exit()
            
   
    


def presentation(centre,taille_x,taille_y,scale): # centre : position centrale du rectangle
    '''Cette fonction permet d'avoir un menu du jeu''' # creation de la fenêtre
    colors = ['blue','yellow' , 'pink', 'purple','cyan']
    tk.rectangle(centre[0]-taille_x,centre[1]-taille_y,centre[0]+taille_x,centre[1]+taille_y,couleur= choice(colors), remplissage = choice(colors) ,
    	      tag = 'Rectangle')
    present_text('Wall-is-you', (300*scale//600, 100*scale//600), 100*scale//600, 100*scale//600,60*scale//600)
    
    



      

