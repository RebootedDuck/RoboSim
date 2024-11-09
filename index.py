import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1024,1024))
clock = pygame.time.Clock()
pygame.display.set_caption('RoboSimulation')
running = True
sheep_amount = 5

# Colours
robocolour = (3, 252, 119)
bgcolour = (40, 40, 40)

def random_positions(amount: int):
    randpositions = []
    for i in range(0, amount):
        randposx = random.randint(0, 1024)
        randposy = random.randint(0, 1024)
        randpositions.append((randposx,randposy))
    return randpositions

randsheepositions = random_positions(sheep_amount)
       
def drawsheep(randsheepositions): # I know this is horrible
    randpositions = randsheepositions
    sheep = []
    for i in randpositions:
        sheep.append(Robot(robotid=random.randint(0,255), window=screen, posx=i[0], posy=i[1], colour=robocolour))
    for x in sheep:
        x.draw()
        

class Robot:
    def __init__(self, robotid: int, window, posx, posy, colour):
        self.robotid = robotid
        self.posx = posx
        self.posy = posy
        self.window = window
        self.colour = colour
        print(f"New robot with ID {self.robotid}")
    def get_info(self):
        print(self.robotid)
    def draw(self):
        pygame.draw.rect(self.window, self.colour, [self.posx-50, self.posy-50, 100,100], 2)
    def setpos(self, posx, posy):
        self.posx = posx
        self.posy = posy
    def changepos(self, posx, posy):
        self.posx = self.posx + posx
        self.posy = self.posy + posy

robot = Robot(robotid=random.randrange(0, 255), window=screen, posx=0, posy=0, colour=robocolour)
print(robot.get_info)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    drawsheep(randsheepositions)
    screen.fill(bgcolour)
    robot.setpos(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    robot.draw()
    pygame.display.flip()
    clock.tick(120)