# test du donjon
import fltk as tk 




def represent_persos(list_pos):
       """
       Créer les dictionnaires qui permettent de situer l'aventurier et les dragons
       """
       liste_dragons = []
       for i in range(len(list_pos)):
              if list_pos[i][0] == 'A':
                     aventurier = {
                            'position':(int(list_pos[i][1]),int(list_pos[i][2])),
                            'niveau':1
                     }
                     
              else:
                     dragon = {
                            'position':(int(list_pos[i][1]),int(list_pos[i][2])),
                            'niveau':int(list_pos[i][3])
                     }
                     liste_dragons.append(dragon)

       return [aventurier,liste_dragons]

def affiche_images(img_pos,scale):
       """
       Affiche graphiquement l'aventurier et les dragons dans le donjon
       """
       for i in range(len(img_pos)):
              if img_pos[i][0] == 'A':
                     coord_x = int(img_pos[i][1])*scale//6
                     coord_y = int(img_pos[i][2])*scale//6
                     tk.image(coord_y+(45*scale//600),coord_x+(50*scale//600),'fichiers_wall_is_you/media/Knight_s.png',largeur = 60*scale//600,hauteur = 60*scale//600,tag = 'hero')
                     tk.rectangle((75*scale//600)+coord_y,(15*scale//600)+coord_x,(85*scale//600)+coord_y,(35*scale//600)+coord_x,remplissage = 'white',tag  = 'niv_chevalier')
                     tk.texte((77*scale//600)+coord_y,(18*scale//600)+coord_x,'1',taille  = 10*scale//600,tag = 'text_chevalier')
              else:
                     coord_x = int(img_pos[i][1])*scale//6
                     coord_y = int(img_pos[i][2])*scale//6
                     niv_dragon  = img_pos[i][3]
                     tag_dragon = '#'+str(coord_y)+str(coord_x)
                     tag_dragon1 = '+'+tag_dragon
                     tag_dragon2 = '-'+tag_dragon
                     tk.image(coord_y+(45*scale//600),coord_x+(50*scale//600),'fichiers_wall_is_you/media/Dragon_s.png',largeur = 60*scale//600,hauteur = 60*scale//600,tag = tag_dragon)
                     tk.rectangle((75*scale//600)+coord_y,(15*scale//600)+coord_x,(85*scale//600)+coord_y,(35*scale//600)+coord_x,remplissage = 'white',tag  = tag_dragon1)
                     tk.texte((77*scale//600)+coord_y,(18*scale//600)+coord_x,niv_dragon,taille  = 10*scale//600,tag = tag_dragon2)

 

def pivoter(donjon,position):  
        '''
        Cette fonction teste le pivotement d'une salle
        du donjon

        salle type (haut, droite, bas, gauche)
        '''                        
        x, y = position
        room = list(donjon[x][y]) # transforme le tuple en liste pour pouvoir pivoter la salle
        room.insert(0,room.pop())
        donjon[x][y] = tuple(room)
        return donjon[x][y]




        
              







def affichage_croix(scale):
        """
        Affiche graphiquement les quatre rectangles dans les quatre coins d'une case
        """
       
       
        for i in range(0,7):
                for j in range(0,7):
                        ax = scale * (j/6) - scale//24
                        ay = scale * (i/6)-scale//50
                        bx = scale * (j/6) +scale//24
                        by = scale*(i/6)+scale//50
                        tk.rectangle(ax,ay ,bx ,by ,remplissage = 'black')
                        tk.rectangle(ay,ax,by,bx,remplissage = 'black')
                        
                        
        
                       

def affiche_porte (coords,tag1,j,scale): 
        """
        Affiche les portes dans chaque direction
        """
        taille_case  = scale//6
        n = (12*scale//600)
        coord_y,coord_x = coords[0],coords[1]
        tk.efface(tag1)
     
        if  j[0] == False:
                tk.rectangle(coord_x,coord_y+n,coord_x+taille_case,coord_y,remplissage = 'black',tag =tag1)
                        
        if j[1] == False:
                tk.rectangle(coord_x+taille_case-n,coord_y,coord_x+taille_case,coord_y+taille_case,remplissage = 'black',tag = tag1)
                       
        if j[2] == False:
                tk.rectangle(coord_x,coord_y+taille_case,coord_x+taille_case,coord_y+taille_case-n,remplissage = 'black',tag = tag1)
                        
        if  j[3] == False:
                tk.rectangle(coord_x,coord_y,coord_x+n,coord_y+taille_case,remplissage = 'black',tag= tag1)


                
        

def affiche_case(scale):
    """
    Affiche le sol du donjon
    """
    for k in range(6):
        for i in range(6):
            pos_x = scale//12+scale//6*i
            pos_y = scale//12+scale//6*k
            tk.image(pos_x,pos_y,'fichiers_wall_is_you/media/sol.png', largeur = scale//6, hauteur = scale//6)
            
           
            








def affiche_donjon(liste_donjon,scale):
       """
       Utilise la fonction affiche_porte pour créer toutes les portes du donjon
       """
       taille_case = scale//6
       for i in range(6):
              for j  in range(6):
                     tag = str(i)+str(j)+'#'
                     affiche_porte((0+taille_case*i,0+taille_case*j),tag,liste_donjon[i][j],scale)

       




 


















