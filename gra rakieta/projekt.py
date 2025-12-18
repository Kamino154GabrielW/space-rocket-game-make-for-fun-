import pygame
import time
import random
from pygame import mixer



pygame.init()
punkty=0
scor=0
czas=0

x_okna=1300
y_okna=800
x_player=650
x_meteort1=650
y_meteort1=0
x_meteort2=0
y_meteort2=0
x_meteort3=1300
y_meteort3=0
x_mglawica=1300
y_mglawica=0
x_gwiazda=1300
y_gwiazda=0
x_gwiazda2=1300
y_gwiazda2=0
x_kometa=1300
y_kx_gwiazda=1300
y_gwiazda=0
x_gwiazda2=1300
y_gwiazda2=0
x_kometa=1300
y_kometa=0

x_laser=1300
y_laser=0


wstemp = pygame.display.set_mode((x_okna,y_okna))
start = pygame.image.load('Bez tytulu.png')
koniec = pygame.image.load('Bez tytulu2.png')
wstemp.blit(start, (300,100))
pygame.display.update()
pygame.time.wait(4000)
pygame.quit()


okno = pygame.display.set_mode((x_okna,y_okna))
player = pygame.image.load('player.png')
okno.blit(player, (x_player,600))
meteort1 = pygame.image.load('meteort.png')
kometa = pygame.image.load('kometa.png')
mglawica = pygame.image.load('mglawica.png')

gwiazda = pygame.image.load('gwiazda.png')
gwiazda2 = pygame.image.load('gwiazda2.png')
laser = pygame.image.load('laser.png')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           pygame.quit()
           exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_player=x_player-11 - punkty
            if event.key == pygame.K_RIGHT:
                x_player=x_player+11 + punkty
                
    y_meteort1=y_meteort1+punkty+7
    y_meteort2=y_meteort2+punkty+7.5
    y_meteort3=y_meteort3+punkty+8
    y_mglawica=y_mglawica+punkty+6
    y_kometa=y_kometa+punkty+16
    y_gwiazda=y_gwiazda+punkty+7
    y_gwiazda2=y_gwiazda2+punkty+7
    y_laser=y_laser+punkty+4

    
    if y_meteort1 >=y_okna:
        y_meteort1=0
        x_meteort1= random.randint (5,1295)
    if y_meteort1 >=500:
        if x_meteort1+50 <=x_player+100 and x_meteort1+50 >=x_player-40:
            pygame.quit()
            zakoniczenie = pygame.display.set_mode((x_okna,y_okna))
            zakoniczenie.blit(koniec, (300,100))
            pygame.display.update()
            pygame.time.wait(4000)
            pygame.quit()
            print('punkty',scor)
            print('czas',czas,'sekund')
            print('zabito przez meteoryt')
            

   
    if y_meteort2 >=y_okna:
        y_meteort2=0
        x_meteort2= random.randint (5,1295)
    if y_meteort2 >=500:
        if x_meteort2+50 <=x_player+100 and x_meteort2+50 >=x_player-40:
            pygame.quit()
            zakoniczenie = pygame.display.set_mode((x_okna,y_okna))
            zakoniczenie.blit(koniec, (300,100))
            pygame.display.update()
            pygame.time.wait(4000)
            pygame.quit()
            print('punkty',scor)
            print('czas',czas,'sekund')
            print('zabito przez meteoryt')
            

    if y_meteort3 >=y_okna:
        y_meteort3=0
        x_meteort3= random.randint (5,1295)
    if y_meteort3 >=500:
        if x_meteort3+50 <=x_player+100 and x_meteort3+50 >=x_player-40:
            pygame.quit()
            zakoniczenie = pygame.display.set_mode((x_okna,y_okna))
            zakoniczenie.blit(koniec, (300,100))
            pygame.display.update()
            pygame.time.wait(4000)
            pygame.quit()
            print('punkty',scor)
            print('czas',czas,'sekund')
            print('zabito przez meteoryt')
            
    if y_mglawica >=y_okna:
        y_mglawica=0
        x_mglawica= random.randint (5,1295)
    if y_mglawica >=500:
        if x_mglawica+50 <=x_player+100 and x_mglawica+50 >=x_player-40:
            mglawica = pygame.display.set_mode((x_okna,y_okna))
            scor+50
            
            
            


    if y_kometa >=y_okna:
        y_kometa=0
        x_kometa= random.randint (5,1295)
    if y_kometa >=500:
        if x_kometa+50 <=x_player+100 and x_kometa+50 >=x_player-40:
            pygame.quit()
            zakoniczenie = pygame.display.set_mode((x_okna,y_okna))
            zakoniczenie.blit(koniec, (300,100))
            pygame.display.update()
            pygame.time.wait(4000)
            pygame.quit()
            print('punkty',scor)
            print('czas',czas,'sekund')
            print('zabito przez komete')
            
    if y_gwiazda >=y_okna:
        y_gwiazda=0
        x_gwiazda= random.randint (5,1295)
    if y_gwiazda >=500:
        if x_gwiazda+50 <=x_player+100 and x_gwiazda+50 >=x_player-40:

            punkty =  punkty + 0.5

    if y_gwiazda2 >=y_okna:
        y_gwiazda2=0
        x_gwiazda2= random.randint (5,1295)
    if y_gwiazda2 >=500:
        if x_gwiazda2+50 <=x_player+100 and x_gwiazda2+50 >=x_player-40:
            punkty = punkty - 0.5



    if y_laser >=y_okna:
        y_laser=0
        x_laser= x_player
    if y_laser >=500:
        if x_laser+50 <=x_player+100 and x_laser+50 >=x_player-40:
            pygame.quit()
            zakoniczenie = pygame.display.set_mode((x_okna,y_okna))
            zakoniczenie.blit(koniec, (300,100))
            pygame.display.update()
            pygame.time.wait(4000)
            pygame.quit()
            print('punkty',scor)
            print('czas',czas,'sekund')
            print('zabito przez kosmitów')



            
            

 
    scor=scor+punkty+1
    okno.fill((0,0,0))
    czas=czas+0.025
    okno.blit(gwiazda, (x_gwiazda,y_gwiazda))
    okno.blit(gwiazda2, (x_gwiazda2,y_gwiazda2))
    okno.blit(meteort1, (x_meteort1,y_meteort1))
    okno.blit(meteort1, (x_meteort2,y_meteort2))
    okno.blit(meteort1, (x_meteort3,y_meteort3))
    okno.blit(kometa, (x_kometa,y_kometa))
    okno.blit(mglawica, (x_mglawica,y_mglawica))
    okno.blit(laser, (x_laser,y_laser))
    okno.blit(player, (x_player,600))

    pygame.time.wait(40)
    pygame.display.update()

ometa=0

x_laser=1300
y_laser=0


wstemp = pygame.display.set_mode((x_okna,y_okna))
start = pygame.image.load('Bez tytulu.png')
koniec = pygame.image.load('Bez tytulu2.png')
wstemp.blit(start, (300,100))
pygame.display.update()
pygame.time.wait(4000)
pygame.quit()


okno = pygame.display.set_mode((x_okna,y_okna))
player = pygame.image.load('player.png')
okno.blit(player, (x_player,600))
meteort1 = pygame.image.load('meteort.png')
kometa = pygame.image.load('kometa.png')
mglawica = pygame.image.load('mglawica.png')

gwiazda = pygame.image.load('gwiazda.png')
gwiazda2 = pygame.image.load('gwiazda2.png')
laser = pygame.image.load('laser.png')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           pygame.quit()
           exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_player=x_player-11 - punkty
            if event.key == pygame.K_RIGHT:
                x_player=x_player+11 + punkty
                

    y_meteort1=y_meteort1+punkty+7
    y_meteort2=y_meteort2+punkty+7.5
    y_meteort3=y_meteort3+punkty+8
    y_mglawica=y_mglawica+punkty+6
    y_kometa=y_kometa+punkty+16
    y_gwiazda=y_gwiazda+punkty+7
    y_gwiazda2=y_gwiazda2+punkty+7
    y_laser=y_laser+punkty+4


    
    if y_meteort1 >=y_okna:
        y_meteort1=0
        x_meteort1= random.randint (5,1295)
    if y_meteort1 >=500:
        if x_meteort1+50 <=x_player+100 and x_meteort1+50 >=x_player-40:
            pygame.quit()
            zakoniczenie = pygame.display.set_mode((x_okna,y_okna))
            zakoniczenie.blit(koniec, (300,100))
            pygame.display.update()
            pygame.time.wait(4000)
            pygame.quit()
            print('punkty',scor)
            print('czas',czas,'sekund')
            print('zabito przez meteoryt')
            

   
    if y_meteort2 >=y_okna:
        y_meteort2=0
        x_meteort2= random.randint (5,1295)
    if y_meteort2 >=500:
        if x_meteort2+50 <=x_player+100 and x_meteort2+50 >=x_player-40:
            pygame.quit()
            zakoniczenie = pygame.display.set_mode((x_okna,y_okna))
            zakoniczenie.blit(koniec, (300,100))
            pygame.display.update()
            pygame.time.wait(4000)
            pygame.quit()
            print('punkty',scor)
            print('czas',czas,'sekund')
            print('zabito przez meteoryt')
            

    if y_meteort3 >=y_okna:
        y_meteort3=0
        x_meteort3= random.randint (5,1295)
    if y_meteort3 >=500:
        if x_meteort3+50 <=x_player+100 and x_meteort3+50 >=x_player-40:
            pygame.quit()
            zakoniczenie = pygame.display.set_mode((x_okna,y_okna))
            zakoniczenie.blit(koniec, (300,100))
            pygame.display.update()
            pygame.time.wait(4000)
            pygame.quit()
            print('punkty',scor)
            print('czas',czas,'sekund')
            print('zabito przez meteoryt')
            
    if y_mglawica >=y_okna:
        y_mglawica=0
        x_mglawica= random.randint (5,1295)
    if y_mglawica >=500:
        if x_mglawica+50 <=x_player+100 and x_mglawica+50 >=x_player-40:
            mglawica = pygame.display.set_mode((x_okna,y_okna))
            scor+50
            
            
            


    if y_kometa >=y_okna:
        y_kometa=0
        x_kometa= random.randint (5,1295)
    if y_kometa >=500:
        if x_kometa+50 <=x_player+100 and x_kometa+50 >=x_player-40:
            pygame.quit()
            zakoniczenie = pygame.display.set_mode((x_okna,y_okna))
            zakoniczenie.blit(koniec, (300,100))
            pygame.display.update()
            pygame.time.wait(4000)
            pygame.quit()
            print('punkty',scor)
            print('czas',czas,'sekund')
            print('zabito przez komete')
            
    if y_gwiazda >=y_okna:
        y_gwiazda=0
        x_gwiazda= random.randint (5,1295)
    if y_gwiazda >=500:
        if x_gwiazda+50 <=x_player+100 and x_gwiazda+50 >=x_player-40:

            punkty =  punkty + 0.5

    if y_gwiazda2 >=y_okna:
        y_gwiazda2=0
        x_gwiazda2= random.randint (5,1295)
    if y_gwiazda2 >=500:
        if x_gwiazda2+50 <=x_player+100 and x_gwiazda2+50 >=x_player-40:
            punkty = punkty - 0.5



    if y_laser >=y_okna:
        y_laser=0
        x_laser= x_player
    if y_laser >=500:
        if x_laser+50 <=x_player+100 and x_laser+50 >=x_player-40:
            pygame.quit()
            zakoniczenie = pygame.display.set_mode((x_okna,y_okna))
            zakoniczenie.blit(koniec, (300,100))
            pygame.display.update()
            pygame.time.wait(4000)
            pygame.quit()
            print('punkty',scor)
            print('czas',czas,'sekund')
            print('zabito przez kosmitów')
    



            
            

    scor=scor+punkty+1
    okno.fill((0,0,0))
    czas=czas+0.025
    okno.blit(gwiazda, (x_gwiazda,y_gwiazda))
    okno.blit(gwiazda2, (x_gwiazda2,y_gwiazda2))
    okno.blit(meteort1, (x_meteort1,y_meteort1))
    okno.blit(meteort1, (x_meteort2,y_meteort2))
    okno.blit(meteort1, (x_meteort3,y_meteort3))
    okno.blit(kometa, (x_kometa,y_kometa))
    okno.blit(mglawica, (x_mglawica,y_mglawica))
    okno.blit(laser, (x_laser,y_laser))
    okno.blit(player, (x_player,600))


    pygame.time.wait(40)
    pygame.display.update()
