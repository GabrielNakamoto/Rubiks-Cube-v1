import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

pygame.display.set_caption("OpenGl Rubiks Cube")

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

surfaces = (
        (0,1,2,3),
        (3,2,7,6),
        (6,7,5,4),
        (4,5,1,0),
        (1,5,7,2),
        (4,0,3,6)
    )

colors = (
    (1, 0, 0), #RED
    (0, 0, 1), #BLUE
    (1, 0.65, 0), #ORANGE
    (0, 1, 0), #GREEN
    (1, 1, 1), #WHITE
    (1, 1, 0), #YELLOW
    (0, 0, 0) #BLACK
    )

def newCube(x_change, y_change, z_change):

    new_vertices = []

    for vertex in verticies:
        new_vert = []

        new_x = vertex[0] + x_change
        new_y = vertex[1] + y_change
        new_z = vertex[2] + z_change

        new_vert.append(new_x)
        new_vert.append(new_y)
        new_vert.append(new_z)

        new_vertices.append(new_vert)

    return new_vertices

def Cube(vertices):
    # glColor3fv(0 min, 1 max RGB (1, 0, 0) == RED ex.)
    # sets color for a GL block
    glBegin(GL_QUADS)
    x = 0
    for surface in surfaces:
        glColor3fv(colors[x])
        for vertex in surface:
            glVertex3fv(vertices[vertex])
        x += 1
    glEnd()

    # telling it were drawing lines

    glBegin(GL_LINES)
    glColor3fv(colors[6])
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

cubeRefs = []

n = -2
for i in range(3):
    m = -2
    for j in range(3):
        o = -2
        for k in range(3):
            for i in range(8):
                cubeRefs.append(newCube(m,o,n))
            o +=2
        m +=2
    n += 2

def main():
    pygame.init()
    display = (1200,800)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    #fov / aspect ratio / clipping planes? (as you zoom out objects dissapear cause too small)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    # moving the cube x, y, z
    glTranslatef(0,0, -20)
    glRotatef(25, 2, 1, 0)
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LINE_SMOOTH)
        glLineWidth(6)
        # degrees, x / y / z
        glRotatef(4, 0.5, 2, 0.5)
        # clears frame like screen.fill()
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        for cube in cubeRefs:
                Cube(cube)

        # basically .update() but it works?
        pygame.display.flip()
main()