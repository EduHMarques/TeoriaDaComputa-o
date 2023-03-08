import pygame
import math
import datetime

pygame.init()

X_screen = 800
Y_screen = 800

X_half = X_screen // 2
Y_half = Y_screen // 2

grey = (30, 30, 30)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

pygame.display.set_caption('Relogio analogico')
screen = pygame.display.set_mode((X_screen, Y_screen))
clock = pygame.time.Clock()
FPS = 60

def printNumbers(text, position):
    font = pygame.font.SysFont('freesansbold.ttf', 40, True, False)
    surface = font.render(text, True, white)
    screen.blit(surface, position)

def grausPygame(R, theta):
    y = math.cos(2*math.pi * theta / 360) * R
    x = math.sin(2*math.pi * theta / 360) * R
    return x + 400 - 12, -(y - 400) - 12

def relogio():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        currentTime = datetime.datetime.now()
        seconds = currentTime.second
        minute = currentTime.minute
        hour = currentTime.hour
            
        screen.fill(grey)
        pygame.draw.circle(screen, white, (400, 400), 400, 4)

        for clockNumber in range(1, 13):
            printNumbers(str(clockNumber), grausPygame(360, clockNumber * 30))

        # Horas
        R = 280
        theta = (hour + minute / 60) * (360/12)
        pygame.draw.line(screen, red, (X_half, Y_half), grausPygame(R, theta), 8)

        # Minutos
        R = 360
        theta = (minute + seconds / 60) * (360/60)
        pygame.draw.line(screen, white, (X_half, Y_half), grausPygame(R, theta), 8)

        # Segundos
        R = 320
        theta = seconds * (360/60)
        pygame.draw.line(screen, (0, 255, 0), (X_half, Y_half), grausPygame(R, theta), 8)

        pygame.display.update()
        clock.tick(FPS)

relogio()