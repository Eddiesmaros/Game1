# -*- coding: cp1252 -*-
# Jag gjorde detta projekt med hjälp av en pygame-tutorial på youtube
#src: https://www.youtube.com/watch?v=ujOTNg17LjI&list=PLQVvvaa0QuDdLkP8MrOXLe_rKuf6r80KO&index=1

from pygame import*
import pygame
import time
import random

pygame.init()
#skapar ett fönster
display_height = 698
display_width = 600
pygame.mixer.music.load("Finlandia.mp3") 
pygame.mixer.music.play(-1,0.0)


#jag definierar färger
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,43,120)
block_color = (53,115,255)

#ställer in bredden på bilden
car_width = 100

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Prehaps one of the most realistic Winter war simulators 11/10")
clock = pygame.time.Clock()
#importerar bilderna går att använda både png och jpg i pygame
carImg = pygame.image.load("car1.png")
sten = pygame.image.load("gomunismos.png")
glom = pygame.image.load("1280px-Flag_of_Finland_1920-1978_(State).sv.png")
blom = pygame.image.load("Voitto-lapissa-2.jpg")
#skapar knappen och
#gör så att det händer något då man klickar på knappen
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
#ställer in stilen
    smallText = pygame.font.SysFont("Arial",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )#var texten placeras
    gameDisplay.blit(textSurf, textRect)


#Skapar en startmeny till spelet
def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #gör så att spelet avslutas korrekt
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #skapar menytexten        
        gameDisplay.blit(glom,(0,-200))
        largeText = pygame.font.SysFont("Arial",25)
        TextSurf, TextRect = text_objects("Undvik kommunism, du styr med sidopilarna", largeText)
        TextRect.center = ((display_width/2),(display_height/3))
        gameDisplay.blit(TextSurf, TextRect)
        #skapar texten till knappen och väljer vilken färg den blir då man för musen över den
        button("Starta spelet!",225,550,150,50,green,green,game_loop)

        pygame.display.update()
        clock.tick(144)
#definierar räknefunktion för antalet hinder man undvikit
def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("År av hungersnöd och gulager undvikta:"+str(count), True, black)
    gameDisplay.blit(text,(0,0)) 

#definierar hindret"
def things(thingx, thingy):
    gameDisplay.blit(sten, (thingx, thingy))

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

 #fixar gameover texten   

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',45)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()
    



#vad som händer om man krashar
def crash():
    message_display("Du förlorade")

#skapar game loopen
def game_loop():
    x =  (display_width * 0.2)
    y = (display_height * 0.8)

    x_change = 0

    thing_startx = random.randrange(0,display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 60
    thing_height = 57

    thingCount = 30
    dodged = 0
    #skapar en while loop som också gör så att spelet stängs då man klickar på x:et
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -15
                if event.key == pygame.K_RIGHT:
                    x_change = 15

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.blit(blom,(0,0))

#gör så att man krashar om man blir träffad av hindret
        things(thing_startx, thing_starty)


        
        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()
#gör så att hindret kommer från olika ställen
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)

        if y < thing_starty+thing_height:
            print('y crossover')

            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                print('x crossover')
                crash()
        #ställer i hur många fps spelet körs i
        pygame.display.update()
        clock.tick(60)
game_intro()
game_loop()
pygame.quit()
quit()



