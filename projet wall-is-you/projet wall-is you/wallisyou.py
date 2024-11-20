import fltk as tk
from graphic_game import*
from logic_game import*
import game_menu as gm

scale = [700,700] # taille de fenêtre
tk.cree_fenetre(scale[0],scale[1])

def init_dungeon(line1,coords_ppl):
    """
    Initialise le donjon
    """
    affiche_case(scale[0])
    affichage_croix(scale[0])
    affiche_donjon(line1,scale[0])
    affiche_images(coords_ppl,scale[0])
    aventurier,liste_dragons = represent_persos(coords_ppl)
    clic_case(line1,scale[0],liste_dragons,aventurier)
  





gm.presentation((100, 100), 1000, 1000,scale[0])
if gm.menu(scale[0]):   
    file = gm.menu2(scale[0])
dungeon,coord_ppl,line2 = file_open(file)
line1 = convert_map_txt(dungeon)
init_dungeon(line1,coord_ppl)

 

tk.attend_ev()
tk.ferme_fenetre()



