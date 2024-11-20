import fltk as tk
from graphic_game import pivoter, affiche_porte
from os import system



def file_open(files):
    file = open("fichiers_wall_is_you/maps/"+files+".txt","r",encoding='utf-8')
    return cook_dungeon(file)

def cook_dungeon(file):
       """ 
       fonction qui permet la création du donjon
       """
       line = [x.strip('\n') for x in file.readlines()]
       line1 = line [0:6]
       line2 = line[6:]
       coords_ppl = []
       for i in range(len(line2)):
              coords = line2[i].replace(" ","")
              coords_ppl.append(coords)
       return line1,coords_ppl,line2


def convert_map_txt(liste_texte) :
       """
        Convertit les fichiers txt map en liste de liste de tuple de quatre booléen déterminant comment sont toutes les cases du jeu
       """
       list_rooms = []

       dico_rooms = {"═" : (False,True,False,True), "║": (True,False,True,False),"╔": (False,True,True,False), "╗":(False,False,True,True), "╚": (True,True,False,False),
               "╝":(True,False,False,True), "╠":(True,True,True,False), "╣": (True,False,True,True), "╦" :(False,True,True,True), "╩" : (True,True, False,True),
               "╨" : (True,False,False,False), "╡" : (False,False,False,True), "╥" : (False,False,True,False), "╞" : (False,True,False,False), "╬" : (True,True,True,True)}

       for i in range (len(liste_texte)):
                liste1 = []
                for j in range(len(liste_texte[i])):
                        liste1.append(dico_rooms[liste_texte[i][j]])

                list_rooms.append(liste1)
       return list_rooms




def game_state(aventurier,dragons,scale):
       """
       Regarde l'état de la partie, renvoie False si l'aventurier est mort et 
       renvoie True en affichant un écran de victoire si tous les dragons ont été vaincus
       """
       if aventurier == None:
              return False
       elif dragons == []:
              tk.rectangle(200*scale//600,200*scale//600,400*scale//600,300*scale//600,remplissage  =  'white')
              tk.texte(210*scale//600,210*scale//600,"Tu as Gagné", taille = 24*scale//600)
              tk.texte(210*scale//600,240*scale//600,"Appuie sur echap pour \n recommencer",taille  = 10*scale//600)
              return True



def connecte(donjon,pos1,tuple_voisins):
              """
              Connection des salles en fonction des points cardinaux des coordonnées 
              """
              x1,y1 = pos1
              x2 =  tuple_voisins[0][0] 
              y2 =  tuple_voisins[0][1] 
              if tuple_voisins[1] == 'O':
                            if donjon[x1][y1][3] and donjon[x2][y2][1]:
                                   return [True,(x2,y2)]
                            else: 
                                   return False

              elif tuple_voisins[1] == 'E':
                            if donjon[x1][y1][1] and donjon[x2][y2][3]:
                                 return [True,(x2,y2)]
                            else: 
                                  return False
                            
              elif tuple_voisins[1] == 'N':
                            if donjon[x1][y1][0] and donjon[x2][y2][2]:
                                   return [True,(x2,y2)]
                            else: 
                                   return False

              elif tuple_voisins[1] == 'S':
                            if donjon[x1][y1][2] and donjon[x2][y2][0]:
                                 return [True,(x2,y2)]
                            else: 
                                  return False

def rencontre(aventurier,dragons,scale):
       """
       Fonction qui regarde si l'aventurier et un dragon se rencontre et regarde si l'aventurier et assez haut niveau pour l'affronter,
       si il est assez haut niveau le dragon disparait, sinon c'est l'aventurier qui disparait.
       """
       scale_sq = scale//6
       for i in range(len(dragons)):
              if aventurier['position']  == dragons[i]['position'] and aventurier['niveau']  == dragons[i]['niveau']:
                   lvl_aventurier  = aventurier['niveau'] 
                   tag_x=dragons[i]['position'][0]*scale_sq
                   tag_y=dragons[i]['position'][1]*scale_sq
                   tag_dragon = '#'+str(tag_y)+str(tag_x)
                   tag_dragon1 = '+'+tag_dragon
                   tag_dragon2 = '-'+ tag_dragon
                   tk.efface(tag_dragon)
                   tk.efface(tag_dragon1)
                   tk.efface(tag_dragon2)
                   dragons.pop(i)
                   aventurier['niveau'] = lvl_aventurier+1
                   cheval_x = aventurier['position'][0]*scale_sq
                   cheval_y  = aventurier['position'][1]*scale_sq
                   niv_chevalier  =str(aventurier['niveau'])
                   tk.rectangle((75*scale//600)+cheval_y,(15*scale//600)+cheval_x,(85*scale//600)+cheval_y,(35*scale//600)+cheval_x,remplissage = 'white',tag  = 'niv_chevalier')
                   tk.texte((77*scale//600)+cheval_y,(18*scale//600)+cheval_x,niv_chevalier,taille  = 10*scale//600,tag = 'text_chevalier')
                   return aventurier,dragons
              
              elif aventurier['position']  == dragons[i]['position'] and aventurier['niveau']  < dragons[i]['niveau']:
                     tk.efface('hero')
                     aventurier  = None
                     tk.rectangle(200*scale//600,200*scale//600,400*scale//600,300*scale//600,remplissage  =  'white')
                     tk.texte(210*scale//600,210*scale//600,"Tu as perdu" ,taille = 24*scale//600)
                     tk.texte(210*scale//600,240*scale//600,"Appuie sur echap pour \n recommencer",taille  = 10*scale//600)
                     return aventurier


def applique_chemin(aventurier,dragons,chemin,scale):
       """
        Fonction qui fait que l'aventurier se déplace
       """
       scale_sq = scale//6
       for k in range(0,len(chemin[0]),1):
              tk.attente(0.25)
              tk.efface('hero')
              tk.efface('tag'+str(k))
              coord_x = chemin[0][k][0]*scale_sq
              coord_y = chemin[0][k][1]*scale_sq
              tk.image(coord_y+(45*scale//600),coord_x+(50*scale//600),'fichiers_wall_is_you/media/Knight_s.png',largeur = 60*scale//600,hauteur = 60*scale//600,tag = 'hero')
              if k == len(chemin[0])-1:
                  aventurier['position'] = chemin[0][k]
                  return rencontre(aventurier,dragons,scale)
                
            


        
      
              

             
              

      
              
def voisines(i, j):
    """
    Voisins pour la connection des salles  dictionnaire avec les coordonnées et leur points cardinaux (NOSE)
    """
    if i ==  0 and j == 0:
           return {(i,j+1):'E',(i+1,j):'S'}
    elif i == 5 and j == 0:
           return {(i-1,j):'N',(i,j+1):'E'}
    elif i == 0  and j == 5:
           return {(i,j-1):'O',(i+1,j):'S'}
    elif i == 5 and j == 5:
           return {(i-1,j):'N',(i,j-1):'O'}
    elif i == 0:
           return {(i,j-1):'O',(i,j+1):'E',(i+1,j):'S'}
    elif i == 5:
           return {(i,j-1):'O',(i,j+1):'E',(i-1,j):'N'}
    elif j == 5:
           return {(i,j-1):'O',(i-1,j):'N',(i+1,j):'S'}
    elif j == 0 :
           return {(i-1,j):'N',(i,j+1):'E',(i+1,j):'S'}

    else:
       return {(i-1,j): 'N', (i+1,j):'S', (i,j+1): 'E', (i, j-1): 'O'} # Nord, Sud,Est, Ouest






def affiche_intention(chemin,scale):
       """
       Fonction permettant d'afficher l'intention
       """
       scale_sq = scale//6
       scale_sq_half = scale_sq//2
       list_tags = []
       for i in range(0,len(chemin[0])-1,1):
              coord_path = chemin[0][i]
              coord_path2 = chemin[0][i+1]
              tags = 'tag'+str(i)
              tk.ligne(scale_sq_half+scale_sq*coord_path[1],scale_sq_half+scale_sq*coord_path[0],scale_sq_half+scale_sq*coord_path2[1],scale_sq_half+scale_sq*coord_path2[0],tag = tags)
              list_tags.append(tags)
       return list_tags
       



          

            

def clic_case(donjon,scale,liste_dragons,aventurier):
       """
       Fonction permettant de pivoter les salles
       """
       scale_sq = scale//6
       list_tag  = []
       clic =True
       while clic:
              ev = tk.donne_ev()
              tev = tk.type_ev(ev)
              
              if tev == 'ClicGauche':
                     if list_tag != []:
                            for truc in list_tag:
                                   tk.efface(truc)
                     x = tk.ordonnee(ev)//(scale_sq)
                     y = tk.abscisse(ev)//(scale_sq)
                     tk.efface(str(x)+str(y)+'#')
                            
                     room = pivoter(donjon,(x,y))
                            
                     tag = str(x)+str(y)+'#'
                     affiche_porte((x*scale_sq,y*scale_sq),tag,room,scale)
                            
                            
                            
                     path = intention(donjon,aventurier['position'],liste_dragons,set())
                     if path != None:
                            list_tag  = affiche_intention(path,scale)
                    

                        
              elif tev == 'Touche':
                     if tk.touche(ev) == 'space':
                            tk.efface('niv_chevalier')
                            tk.efface('text_chevalier')
                            if path != None:
                                   aventure = applique_chemin(aventurier,liste_dragons,path,scale)
                                   if not game_state(aventure,liste_dragons,scale):
                                      tev != 'ClicGauche'
                                  
                     elif tk.touche(ev) == 'Escape':
                           tk.ferme_fenetre()
                           system('python wallisyou.py')
                           
                                  
              elif tev == 'Quitte':  
                        break
                
              tk.mise_a_jour()
    
    



def intention(donjon, position, dragons,visite):
    """
    Fonction permettant de trouver un chemin à l'aventurier
    """
    x, y = position
    
    
    # Si la position correspond à un dragon de niveau donné, on a trouvé un chemin trivial
   
    for i in range (len(dragons)):
           if position == dragons[i]['position']:
                  return ([position], dragons[i]['niveau'])
    
    # Si la position est déjà visitée, on arrête la recherche
    if position in visite:
        return None
    
    # On ajoute la position à l'ensemble des cases visitées
    visite.add(position)
    
    
    # On recherche récursivement sur chaque position voisine ouverte
    voisins = voisines(x,y)
    new_list = []
    for i in voisins.items():
                    if connecte(donjon,position,i):
                           new_list.append(i[0])

                        
    
    
    results = []
    for voisin in new_list:
        result = intention(donjon, voisin, dragons, visite)
        if result:
            results.append(result)
    
    # Si aucune recherche n'a produit de résultat, on renvoie None
    if not results:
        return None
    
    # On récupère le résultat de plus haut niveau
    chemin, niveau = max(results, key=lambda r: r[1])
    
    # On renvoie le chemin jusqu'au dragon le plus fort
    return ([position] + chemin, niveau)  




