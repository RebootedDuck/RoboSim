import random
import math

class Misc:
    def randompositions(amount, boundaries):
        randompositions = []
        for i in range(0, amount):
            randompositions.append((random.randint(0, boundaries[0]), random.randint(0, boundaries[1])))
        return randompositions
    
    def fpscounter(window, clock, font):
        fps = str(math.floor(clock.get_fps()))
        fps_surface = font.render(fps, True, (255,255,255))
        window.blit(fps_surface, (window.get_width()-70,0))