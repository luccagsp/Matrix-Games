import numpy as np
from numpy import sin, cos
import pygame 
global  angle
angle = 0.3
points = np.array([
    np.array([50,50,0]),
    np.array([50,0,0]),
    np.array([0,50,0]),
    np.array([0,0,0])
])
projection = np.array([
    np.array([1,0,0]),
    np.array([0,1,0])
])
WHITE = (255,255,255)
pygame.init()
window = pygame.display.set_mode((400,500))
pygame.display.set_caption("3D tests")
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #Lógica
    window.fill("red")

    for array in points:
        rotatedArray = np.matmul(rotation, array)
        projectedArray = np.matmul(projection, rotatedArray)
        print(rotatedArray,array)
        print(projectedArray)
        x = projectedArray[0]+50
        y = projectedArray[1]+50
        pygame.draw.circle(window, WHITE, (x,y), 5)
    pygame.time.delay(100)
    angle+=0.3
    print(angle)
    pygame.display.flip()


