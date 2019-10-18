# -*- coding: utf-8 -*-
import random
import JeffersonShell

import pygame
from pygame.locals import *
pygame.init()

RED = (255,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
BLACK = (0,0,0)


def displayCylinder(mySurface,cylinder,i) :      #si on avait un j en plus, qui indique la position ("au bon endroit") pour afficher le ieme dique ca nous aurait fait gagner beaucoup plus de ligne.
    font = pygame.font.Font(None, 20)            #comme on a que i on l'affiche juste a la ieme position
    for j in range(len(cylinder[i])) :
        text = font.render(cylinder[i][j], 1, RED) # 1 c'est la meme chose que true
        mySurface.blit(text, (i*25, j*20))

def displayCylinders(mySurface, cylinder):
    for i in range(1,len(cylinder)+1):
        displayCylinder(mySurface,cylinder,i)
    pygame.display.flip()

def enterKey(mySurface,n) :
    font = pygame.font.Font(None, 20)
    for i in range(1,n+1):
        text = font.render(str(i), 1, RED)
        mySurface.blit(text, ( i * 25, 26 * 20 + 50))
    text = font.render("ENTER THE KEY", 1, RED)
    mySurface.blit(text, (n * 25 + 50, 26 * 20 + 50))
    text = font.render("ANNULER", 1, RED)                #ligne facultative, c'est pour effacer la selection en cas d'erreur
    mySurface.blit(text, (n * 25 + 50, 26 * 20 + 75))    #ligne facultative
    text = font.render("ANNULER TOUT", 1, RED)           #ligne facultative
    mySurface.blit(text, (n * 25 + 150, 26 * 20 + 75))   #ligne facultative
    pygame.display.flip()

    select = 0
    selection = True
    key = []
    while select < n and selection :                    #tant que l'on a pas selectionné n valeur et qu'on veut toujours continuer la selection des clés du dictionnaire
        for event in pygame.event.get():
            if event.type == QUIT:
                selection = False
            elif event.type == MOUSEBUTTONUP :
                for i in range(1, n + 1):                                   #pour toutes les clés du dictionnaire
                    rect_num = pygame.Rect(i * 25, 26 * 20 + 50, 25, 20)     #rappel : pygame.Rect(x,y,largeur,hauteur), recupere le rectangle qui contient le numero i
                    if rect_num.collidepoint(event.pos) and i not in key :  #fonction pygame qui verifie si rect_num contient la position de la souris event.pos et que numero n'est pas encore selectionné
                        select += 1
                        text = font.render(str(i), 1, BLUE)              #on peut se permettre d'utiliser i puisque les clés ont été affiché a l'aide des des indices i (ligne 24) et qui constitue aussi les clés du dictionnaire
                        mySurface.blit(text, (select * 25, 26 * 20 + 75))#affiche le numero selectionné en bas , 25 pixel plus bas (75 = 50 + 25 ), on utilise ici select pour suivre et en meme temps compter le nombre de numero selectionné
                        text = font.render(str(i), 1, WHITE)             #recree le meme numero en blanc
                        mySurface.blit(text, (i * 25, 26 * 20 + 50))     #et l'affiche a la place du numero cliqué pour indiquer qu'on la deja selectionné
                        key.append(i)
                        pygame.display.flip()


                rect_annuler = pygame.Rect(n * 25 + 50, 26 * 20 + 75, 80, 20)     #a partir d'ici c'est moi qui l'ai ajouté pour rendre un peu fun
                rect_annulertout = pygame.Rect(n * 25 + 150, 26 * 20 + 75, 150, 20)
                if rect_annuler.collidepoint(event.pos) and select != 0 :
                    a_supprimer = key.pop()                             #key.pop supprime la derniere valeur ajoutée a la liste key et la renvoie en meme temps
                    text = font.render(str(a_supprimer), 1, BLACK)        #reecrire du texte noir a la place pour effacer, c'est la seule idée que j'ai trouvé
                    mySurface.blit(text, (select * 25, 26 * 20 + 75))
                    text = font.render(str(a_supprimer), 1, RED)        #remettre le numero blanc en rouge
                    mySurface.blit(text, (a_supprimer * 25, 26 * 20 + 50))
                    select -= 1                                        #diminuer le nombre de selection
                    pygame.display.flip()
                elif rect_annulertout.collidepoint(event.pos) :
                    rect_cle= pygame.Rect(25, 26 * 20 + 75, n * 25, 20)   #toute la ligne qui contient les toutes lesclés deja selectionnéés
                    mySurface.fill(BLACK,rect_cle)                        #effacer toute la ligne
                    for i in key :                                        #parcourir toutes les valeurs de la liste key
                        text = font.render(str(i), 1, RED)                #remettre tout a rouge
                        mySurface.blit(text, (i * 25, 26 * 20 + 50))
                    select = 0                                            #mettre le compteur de selection a zero
                    key = []                                              #vider la liste key
                    pygame.display.flip()                                 #jusque la pour la partie facultative





    mySurface.fill(BLACK)                     #effacer toute la surface
    displayCylinders(mySurface, cylinder)     #reafficher le cylindre
    if JeffersonShell.keyOK(key,n) :          #a la sortie de boucle de selection verifier si la clé est bonne , mettre une valeur superieur a n par exemple 40 si on veut verifier le cas ou la clé n'est pas bonne
        return key
    elif selection:                           #sinon si la selection n'etait pas interrompue, reprendre la selection
        text = font.render("KEY NOT OK, GET AGAIN", 1, BLUE)
        mySurface.blit(text, (n * 25 + 50, 26 * 20 ))
        pygame.display.flip()
        enterKey(mySurface,n)

    pygame.display.flip()                      #raffraichir la surface pour montrer les nouvelles ecritures



def rotateCylinder(cylinder,i,up=True) :
    if up :
        rotate = cylinder[i][1:] + cylinder[i][0]
    else :
        rotate = cylinder[i][-1] + cylinder[i][:-1]
    cylinder[i] = rotate

def rotateCylinders(mySurface ,cylinder) :
    key = enterKey(mySurface,len(cylinder))
    print("cylinder :", cylinder)               #pour voir le cylinder dans la console
    print(key)                                  #pour voir le key dans la console

    font = pygame.font.Font(None, 20)
    if JeffersonShell.keyOK(key,len(cylinder)) :

        cylinder_by_key = {}
        for i in range(len(cylinder)):                        # de 0 a n-1 puisque key est une liste te debute par 0
            cylinder_by_key[i+1] = cylinder[key[i]]           # creer une nouvelle cylinder rangée suivant l'ordre du key, par exemple si 7 est le premier element key cylinder_by_key[1] = cylinder[7]

        print("rearrangé:", cylinder_by_key) #pour voir le nouveau cylinder dans la console
        mySurface.fill(BLACK)                         # effacer toute la surface
        displayCylinders(mySurface, cylinder_by_key)  # afficher le cylinder avec un nouvel arrangement

        for i in range(1, len(cylinder) + 1):        #affichage des fleches de rotation
            text = font.render("U", 1, RED)          #  ↑ ne s'affiche pas correctement probleme d'encodage
            print("↑")
            mySurface.blit(text, (i * 25, 26 * 20 + 50))
            text = font.render("D", 1, RED)          #  ↓ ne s'affiche pas correctement
            mySurface.blit(text, (i * 25, 26 * 20 + 75))
            text = font.render(str(key[i-1]), 1, BLUE)     # pour afficher la clé, facultatif
            mySurface.blit(text, (i * 25, 26 * 20 + 100))
            pygame.display.flip()

        clear = random.randint(0,25)          #choix de la ligne du "CLEAR" random.randint(0,25) donne une valeur aleatoire de entre 0 et 25
        cipher = JeffersonShell.shift(clear)  #calcul de la ligne du "CIPHER"
        text = font.render("CLEAR", 1, RED)
        mySurface.blit(text, (len(cylinder) * 25 + 50, clear * 20))
        text = font.render("CIPHER", 1, RED)
        mySurface.blit(text, (len(cylinder) * 25 + 50, cipher * 20))
        text = font.render("FINISH", 1, RED)
        mySurface.blit(text, (len(cylinder) * 25 + 50, 26 * 20 + 50))
        pygame.display.flip()

        # ensuite a partir d'ici travailler avec cylinder_by_key

        rotation = True
        while rotation:
            for event in pygame.event.get():
                if event.type == QUIT:
                    rotation = False
                elif event.type == MOUSEBUTTONUP:
                    for i in range(1, len(cylinder_by_key) + 1):
                        rect_up = pygame.Rect(i * 25, 26 * 20 + 50, 25, 20)   # rappel : pygame.Rect(x,y,largeur,hauteur), recupere le rectangle qui contient une fleche up
                        rect_down = pygame.Rect(i * 25, 26 * 20 + 75, 25, 20) # recupere le rectangle qui contient une fleche down
                        if rect_up.collidepoint(event.pos):                   # fonction pygame qui verifie si rect_num contient la position de la souris event.pos
                            rotateCylinder(cylinder_by_key, i,True)
                        elif rect_down.collidepoint(event.pos):
                            rotateCylinder(cylinder_by_key, i, False)
                        rect_cle = pygame.Rect(i * 25, 0, 25, 26 * 20)  # toute la colonne qui contient un mix
                        mySurface.fill(BLACK, rect_cle)                 # effacer toute la colonne
                        displayCylinder(mySurface,cylinder_by_key,i)
                        pygame.draw.line(mySurface, RED, (25, clear * 20 - 2), (len(cylinder) * 25 + 10, clear * 20 - 2), 2)
                        pygame.draw.line(mySurface, RED, (25, clear * 20 + 12), (len(cylinder) * 25 + 10, clear * 20 + 12), 2)
                        pygame.display.flip()

                    rect_finish = pygame.Rect(len(cylinder) * 25 + 50, 26 * 20 + 50, 80, 20) # recupere le rectangle qui contient le finish
                    if rect_finish.collidepoint(event.pos) :
                        text = ""
                        for i in range(1, len(cylinder_by_key) + 1):     #recuperer les lettres de la ligne clear qui vont constituer le texte a chiffrer
                            text += cylinder_by_key[i][clear]
                        text_cipher = ""
                        for i in range(1, len(cylinder_by_key) + 1):     #recuperer les lettres de la ligne cipher qui vont constituer le texte chiffré
                            text_cipher += cylinder_by_key[i][cipher]

                        # autre possibilité : text_cipher = JeffersonShell.cipherText(cylinder, key,text)  # ici faut prendre le cylindre normal puisque la fonction est créée dans JeffersonShell et utilise un cylinder normal

                        fichier = open("cipher.txt", "w")
                        fichier.write(text_cipher)

                        print(text,text_cipher,JeffersonShell.cipherText(cylinder,key,text))   #pour voir le texte a chiffrer et son resultat dans la console, avec les deux methodes possibles
                        pygame.draw.line(mySurface, RED, (25, cipher * 20 - 2), (len(cylinder) * 25 + 10, cipher * 20 - 2), 2)
                        pygame.draw.line(mySurface, RED, (25, cipher * 20 + 12),(len(cylinder) * 25 + 10, cipher * 20 + 12), 2)
                        pygame.display.flip()
                        rotation = False




# taille du cylinder = nombre de disque
cylinder = JeffersonShell.loadCylinder("data.txt")  #ou mettre MP-1ARI.txt    #creer le cylinder en premier avant de creer la surface
mySurface = pygame.display.set_mode((len(cylinder) * 25 + 300, 700))   #le width de la surface est calculé en fonction de la taille du cylinder pour redimentionnement automatique
pygame.display.set_caption('Jefferson cipher')

displayCylinders(mySurface,cylinder)
rotateCylinders(mySurface ,cylinder)




continuer = True
while continuer:

    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False


pygame.quit()


