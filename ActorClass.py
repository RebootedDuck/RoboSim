import pygame
import random
from ColoursClass import Colours as cc



class Actor:
    def __init__(self, window, id, pos, size, colour, actortype): # Pos and Size are both tuples, [0] should always be x and y [1]
        self.window = window
        self.id = id
        self.pos = pos
        self.size = size
        self.window = window
        self.colour = colour
        self.actortype = actortype
        
        print(f"New actor of ID {self.id}, and of type {self.actortype} created")
        
    def getinfo(self):
        return {"id": self.id, "actortype": self.actortype, "pos": self.pos, "size": self.size}
        
    def setpos(self, pos):
        self.pos[0] = pos[0]
        self.pos[1] = pos[1]
        
    def changepos(self, pos):
        self.pos[0] = self.pos[0] + pos[0]
        self.pos[1] = self.pos[1] + pos[1]
        
    def draw(self):
        pygame.draw.rect(self.window, self.colour, [self.pos[0]-(self.size[0]/2),self.pos[1]-(self.size[1]/2),self.size[0],self.size[1]]) # Calculate the middle position, more intuitive
        #print(f"A {self.actortype} with positions {self.pos} is being drawn")
        
class Robot(Actor):
    def __init__(self, window, id, pos, size, colour):
        Actor.__init__(self, window, id, pos, size, colour, actortype="Robot")
        
class Sheep(Actor):
    def __init__(self, window, id, pos, size, colour):
        Actor.__init__(self, window, id, pos, size, colour, actortype="Sheep")
        
class ActorManager:
    def __init__(self, window):
        self.actors = {"Robot": [], "Sheep": [], "Arena": []}
        self.ids = []
        self.window = window
        print("New Actor Manager created")
        
    def addactor(self, pos, size, colour, actortype):
        id = random.choice([x for x in range(1024) if x not in self.ids])
        if actortype == "Robot":
            robot = Robot(self.window, id, pos, size, colour)
            self.actors["Robot"].append(robot)
            return robot
        if actortype == "Sheep":
            sheep = Sheep(self.window, id, pos, size, colour)
            self.actors["Sheep"].append(sheep)
            return sheep
            
    def destroyactor(self, actor):
        self.actors[actor.actortype] = self.actors[actor.actortype].remove(actor)
    
    def actors(self):
        return self.actors