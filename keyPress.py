import pygame

pygame.init()

# to spam the pygame.KEYDOWN event every 100ms while key being pressed
#pygame.key.set_repeat(100, 100)

while True:
    #events = pygame.event.get()
    #print events
    #if events:
    #    break
    for event in pygame.event.get():
        print event
        if event.type == pygame.KEYDOWN:
            break
            print "key down"
            if event.key == pygame.K_w:
                print 'go forward'
            if event.key == pygame.K_s:
                print 'go backward'
        if event.type == pygame.KEYUP:
            print 'stop'
