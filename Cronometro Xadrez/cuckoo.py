import pygame as pg
import math
import datetime

pg.init()

X = 460
Y = 750
X_center = 236
Y_center = 368
center = (X_center, Y_center)

grey = (30, 30, 30)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

pg.mixer.init(frequency=48000)
cuckoo_sound = pg.mixer.Sound('cuckoo_sound.mp3')

pg.display.set_caption("Clock")
display = pg.display.set_mode((X, Y))
clock = pg.time.Clock()
FPS = 60

def printNumbers(text, position):
    font = pg.font.SysFont("Castellar", 25, True, False)
    surface = font.render(text, True, (0, 0, 0))
    display.blit(surface, position)

def grausPygame(R, theta):
    y = math.cos(2*math.pi*theta/360) * R
    x = math.sin(2*math.pi*theta/360) * R

    return x+236-9, 368-y-12                # Valores para ajustar ao centro

pg.display.flip()

def game():

    isPlaying = False

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
        current_time = datetime.datetime.now()
        seconds = current_time.second
        minute = current_time.minute
        hour = current_time.hour
        
        display.fill(white)
        
        # Background image
        bg_image = pg.image.load("cuckoo-clock.png").convert()
        width = bg_image.get_rect().width
        height = bg_image.get_rect().height
        bg_image = pg.transform.scale(bg_image, (width*1.5, height*1.5)) 
        display.blit(bg_image, (0, 0))
        
        pg.draw.circle(display, (0, 0, 0), center, 127, 4)

        for clockNumber in range(1, 13):
            printNumbers(str(clockNumber), grausPygame(105, clockNumber * 30))

        if (seconds == 1 and isPlaying == False):
            isPlaying = True
            cuckoo_sound.play()

        if (seconds == 10 and isPlaying):
            isPlaying = False
            cuckoo_sound.stop()

        # Horas
        R = 60
        theta = (hour+minute/60+seconds/3600)*(360/12)
        pg.draw.line(display, red, center, grausPygame(R, theta), 8)

        # Minutos
        R = 80
        theta = (minute+seconds/60) * (360/60)
        pg.draw.line(display, black, center, grausPygame(R, theta), 8)

        # Segundos
        R = 80
        theta = seconds * (360/60)
        pg.draw.line(display, black, center, grausPygame(R, theta), 5)

        pg.display.update()
        clock.tick(FPS)

game()
pg.quit()