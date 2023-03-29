import pygame
from threading import Thread

colors = {
    "w": (255, 255, 255),
    "o": (255, 165, 0),
    "g": (0, 255, 0),
    "r": (255, 0, 0),
    "b": (0, 0, 255),
    "y": (255, 255, 0)}

# Set the dimensions of the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# Define the size of each cell
CELL_SIZE = int(min(SCREEN_WIDTH/(4*3),SCREEN_HEIGHT/(3*3)))

def loopy():
    while True:
        pygame.event.get()
        print('lol')
    
def init():
    pygame.init()
    global screen, t1

    # Create the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set the title of the game
    pygame.display.set_caption("Rubik's Cube")
    t1 = Thread(target=loopy)
    t1.start()


    

def print_graphics(cube):
    pygame.event.get()
    screen.fill((0, 0, 0))
    draw_face(cube[0*9:0*9+9],CELL_SIZE*3*1,0)
    draw_face(cube[1*9:1*9+9],CELL_SIZE*3*0,CELL_SIZE*3)
    draw_face(cube[2*9:2*9+9],CELL_SIZE*3*1,CELL_SIZE*3)
    draw_face(cube[3*9:3*9+9],CELL_SIZE*3*2,CELL_SIZE*3)
    draw_face(cube[4*9:4*9+9],CELL_SIZE*3*3,CELL_SIZE*3)
    draw_face(cube[5*9:5*9+9],CELL_SIZE*3*1,CELL_SIZE*3*2)
    # Update the screen
    pygame.display.flip()
    

def draw_face(face, x_left, y_top):
        # Draw a rectangle for a single face
        for i in range(3):
            for j in range(3):
                print(colors[face[i*3+j]],x_left + CELL_SIZE*i,y_top + CELL_SIZE*j, CELL_SIZE)
                pygame.draw.rect(screen,colors[face[i*3+j]],(x_left + CELL_SIZE*i,y_top + CELL_SIZE*j,CELL_SIZE,CELL_SIZE))