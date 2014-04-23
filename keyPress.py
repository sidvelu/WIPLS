import pygame

pygame.init()
pygame.display.set_mode((1,1), pygame.NOFRAME)

# to spam the pygame.KEYDOWN event every 100ms while key being pressed
pygame.key.set_repeat(100, 100)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print 'up'
            elif event.key == pygame.K_DOWN:
                print 'down'
            elif event.key == pygame.K_SPACE or event.key == pygame.K_q:
                print 'quitting'
                done = True
        if event.type == pygame.KEYUP:
            print 'stop'
