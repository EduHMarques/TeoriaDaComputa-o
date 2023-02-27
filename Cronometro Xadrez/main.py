import pygame

def main():
    pygame.init()
    pygame.display.set_caption('Relogio Analogico')

    X = 720
    Y = 480

    X_relogio = 580
    Y_relogio = 260
    
    white = (255, 255, 255)
    green = (0, 255, 0)
    grey = (30, 30, 30)
    blue = (0, 0, 128)

    initialTime = 600
    startTime = 0
    clock = pygame.time.Clock()

    SCREEN = pygame.display.set_mode((X, Y))

    # Teste de texto de fonte
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('Cronometro', True, green, grey)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)

    # Retangulo do relogio
    retangulo = pygame.Rect(0, 0, X_relogio, Y_relogio)
    retangulo.center = (X // 2, Y // 2)



    while True:
        
        clock.tick(60)
        startTime += clock.get_fps()
        textoTempo = font.render(str(startTime), True, green, grey)

        # Elementos na ordem de exibição, como camadas (baixo pra cima)
        SCREEN.fill(white)
        pygame.draw.rect(SCREEN, grey, retangulo)
        SCREEN.blit(textoTempo, textRect)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.flip()


main()