import pygame, threading

WIDTH = 480 # 375(125 for each box: Attack, Bag, Run) + 40 (10 between each box and the borders1wof the screen)
HEIGHT = 320 # 
DBS = WIDTH / 20 # Display Border Size
RBS = 6 # Rect Border Size
FPS = 60
EVENTS = 0

pygame.init()  # initiates pygame
pygame.display.set_caption("Battle Prototype")
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))  # creates a window

