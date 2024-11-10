import pygame
import random
import time

import ActorClass
from ColoursClass import Colours as cc
from MiscClass import Misc as ms

pygame.init()
window = pygame.display.set_mode((1920,1080))
clock = pygame.time.Clock()
pygame.display.set_caption("RoboSimulation")
running = True
sheepamount = 1

# CRITICAL
am = ActorClass.ActorManager(window) # This manages everything, DO NOT ACCESS ACTORS DIRECTLY >:((((, also give it a window so it knows how to make actors

robot = am.addactor(pos=[100,100], size=[100,100], colour=cc.robotColour, actortype="Robot")
roboposset = False

sheepositions = ms.randompositions(sheepamount, [1920,1080])
sheep = [am.addactor(pos=[i[0], i[1]], size=[100,100], colour=cc.sheepColour, actortype="Sheep") for i in sheepositions]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            roboposset = True
    
    window.fill(cc.backgroundColour)
    
    if not roboposset:
        robot.setpos([pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]])
    else:
        pass
    
    robot.draw()
    
    for i in sheep:
        i.setpos(sheepositions[sheep.index(i)])
        i.draw()
    
    ms.fpscounter(window, clock, cc.font)
    
    pygame.display.flip()
    clock.tick(60)