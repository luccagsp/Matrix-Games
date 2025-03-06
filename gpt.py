import numpy as np
from numpy import sin, cos
import pygame 

angle = 0
points = np.array([
    [1, 1, 0.5],
    [1, 0, 0.5],
    [0, 1, 0.5],
    [0, 0, 0.5],
    [1, 1, -0.5],
    [1, 0, -0.5],
    [0, 1, -0.5],
    [0, 0, -0.5],

    [0.5, 0.5, 0.5],
    [0.5, 0.5, -0.5],
    [0.5, 1, 0],
    [0.5, 0, 0],
    [1, 0.5, 0],
    [0, 0.5, 0],
])
rows, cols = points.shape

WHITE = (255, 255, 255)
RED = (255, 0, 0)

pygame.init()
window = pygame.display.set_mode((400, 500))
pygame.display.set_caption("3D tests")
running = True
center = np.mean(points, axis=0)  # Centroide del cuadrado: [25,25,0]

def connect(i,j, points, color = WHITE):
    a = points[i]
    b = points[j]
    pygame.draw.line(window,color, a,b)

asd = 0
while running:
    rotationX = np.array([
        np.array([1,0,0]),
        np.array([0,cos(angle),-sin(angle)]),
        np.array([0,sin(angle),cos(angle)]),
    ])
    rotationY = np.array([
        np.array([cos(angle),0,sin(angle)]),
        np.array([0,1,0]),
        np.array([-sin(angle),0,cos(angle)]),
    ])
    rotationZ = np.array([
        np.array([cos(angle),-(sin(angle)),0]),
        np.array([sin(angle),cos(angle),0]),
        np.array([0,0,1])
    ])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:  # Detectar si una tecla fue presionada
            if event.key == pygame.K_ESCAPE:  # Si se presiona la tecla 'Esc'
                asd=1
    window.fill("black")
    projectedPoints = np.array([])
    projectedPoints = np.zeros((rows,2))
    facePoints = []
    for i,array in enumerate(points):
        # 1️⃣ Trasladar al origen
        translated = array - center
        
        # 2️⃣ Aplicar rotación
        rotatedArray = np.matmul(rotationX, translated)
        rotatedArray = np.matmul(rotationY, rotatedArray)
        rotatedArray = np.matmul(rotationZ, rotatedArray)

        # 4️⃣ Aplicar proyección
        distance = 2
        z = 1 / (distance - rotatedArray[2])

        projection = np.array([  # Projection matrix
            [z, 0, 0],
            [0, z, 0]
        ])

        projectedArray = np.matmul(projection, rotatedArray)
        projectedArray*=500
        # Dibujar
        width, height = window.get_size()

        x = projectedArray[0]+width/2
        y = projectedArray[1]+height/2
        
        projectedPoints[i] = [x,y]

        pygame.draw.circle(window, WHITE, (int(x), int(y)), 5)
        if i > 7:
            facePoints.append(float(rotatedArray[2]))
        
    pygame.time.delay(5)

    for i,e in enumerate(facePoints):
        if max(facePoints) == e:            
            x,y = projectedPoints[8+i]
            pygame.draw.circle(window, RED, (int(x), int(y)), 5)

            print(e,i)
    # print(facePoints)
    connect(0,1,projectedPoints)
    connect(0,2,projectedPoints)
    connect(3,1,projectedPoints)
    connect(3,2,projectedPoints)

    connect(4,5,projectedPoints)
    connect(4,6,projectedPoints)
    connect(7,5,projectedPoints)
    connect(7,6,projectedPoints)

    connect(4,0,projectedPoints)
    connect(1,5,projectedPoints)
    connect(2,6,projectedPoints)
    connect(3,7,projectedPoints)
    
    angle += 0.01
    pygame.display.flip()
