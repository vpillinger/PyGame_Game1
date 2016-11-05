import sys, pygame

pygame.init()

screen_size = width, height = 720, 540
ball_speed = [1, 1]
black = 0, 0, 0


screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock();

ball = pygame.image.load("asteroid.png").convert()
ball = pygame.transform.scale(ball, (60,60))
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(ball_speed)
    if ballrect.left < 0 or ballrect.right > width:
        ball_speed[0] = -ball_speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        ball_speed[1] = -ball_speed[1]

    # Draw Screen
    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()

    # FPS measuring
    clock.tick(60)
    pygame.display.set_caption("fps: " + str(clock.get_fps()))