import pygame
import sys

pygame.init()
res = (1280, 720)
screen = pygame.display.set_mode(res)

clock = pygame.time.Clock()
delta = 0.0
max_tps = 90
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

game_over_element_x = 700
game_over_element_y = 300
box = pygame.Rect(game_over_element_x, game_over_element_y, 100, 50)

game_over = False

red = (255, 0, 0)

while True:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    # TICK RATE
    delta += clock.tick()/1000.0
    while delta > 1 / max_tps:
        delta -= 1 / max_tps

        # KEYBOARD OPERATION
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            player_pos.x += 2
        if keys[pygame.K_s]:
            player_pos.y += 2
        if keys[pygame.K_a]:
            player_pos.x -= 2
        if keys[pygame.K_w]:
            player_pos.y -= 2

        if keys[pygame.K_ESCAPE]:
            sys.exit(0)

    pygame.display.update()

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, red, box)
    #COLLISION HANDLING
    if player_pos.x + 20 >= game_over_element_x and player_pos.x - 20 <= game_over_element_x + 100:
        if player_pos.y + 20 >= game_over_element_y and player_pos.y - 15 <= game_over_element_y + 50:
            game_over = True

    #TEXT RENDERING
    if game_over:
        font = pygame.font.Font(None, 36)
        text = font.render("Koniec gry. Naciśnij R, aby zresetować.", True, red)
        screen.blit(text, ((screen.get_width() - 350) / 2, (screen.get_height() - 450) / 2))

        if keys[pygame.K_r]:
            #RESET
            player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
            game_over = False

    pygame.draw.circle(screen, "red", player_pos, 20)
    pygame.display.flip()
