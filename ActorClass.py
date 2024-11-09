import pygame
import ColoursClass as cc

class Actor:
    def __init__(self, window, id, pos=(0,0), size=(100,100), colour=cc.genericColour, actortype="Generic"): # Pos and Size are both tuples, [0] should always be x and y [1]
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

class Robot(Actor):
    def __init__(self, window, id, pos=(0,0), size=(100,100), colour=cc.genericColour, actortype="Robot"):
        Actor.__init__(self, window, id, pos=(0,0), size=(100,100), colour=cc.genericColour, actortype="Robot")
        
class Sheep(Actor):
    def __init__(self, window, id, pos=(0,0), size=(100,100), colour=cc.genericColour, actortype="Sheep"):
        Actor.__init__(self, window, id, pos=(0,0), size=(100,100), colour=cc.genericColour, actortype="Sheep")
        