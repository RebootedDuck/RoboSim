import pygame
import random
import time

import ActorClass
import ColoursClass as cc
import MiscClass

pygame.init()
window = pygame.display.set_mode((1024,1024))
clock = pygame.time.Clock()
pygame.display.set_caption("RoboSimulation")
running = True
sheepamount = 5

robot = ActorClass.Robot(window=window, id=1, pos=(100,100), size=(100,100), colour=cc.robotColour)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    window.fill(cc.backgroundColour)
    
    robot.setpos(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    robot.draw()
    
    pygame.display.flip()
    clock.tick(60)