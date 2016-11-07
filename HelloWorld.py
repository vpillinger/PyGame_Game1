import sys, pygame

pygame.init()

screen_size = width, height = 720, 540
ball_speed = [1, 1]
black = 0, 0, 0


screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock();

asteroid = pygame.image.load("asteroid.png").convert()
asteroid = pygame.transform.scale(asteroid, (60, 60))
drawrect = asteroid.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    drawrect = drawrect.move(ball_speed)
    if drawrect.left < 0 or drawrect.right > width:
        ball_speed[0] = -ball_speed[0]
    if drawrect.top < 0 or drawrect.bottom > height:
        ball_speed[1] = -ball_speed[1]

    # Draw Screen
    screen.fill(black)
    screen.

    # Draw asteroid
    screen.blit(asteroid, drawrect)
    pygame.display.flip()

    # FPS measuring
    clock.tick(60)
    pygame.display.set_caption("fps: " + str(clock.get_fps()))