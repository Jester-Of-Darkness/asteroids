import pygame
import sys
from score import Score
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable,   drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    score = Score()
    score_font = pygame.font.Font(None, 36)
    Shot.containers = (shots, updatable, drawable)

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    game_over = False
    
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if game_over == True:
                    if event.key == pygame.K_r:
                        score.reset_score()
                        game_over = False

                        asteroids.empty()
                        shots.empty()
                        updatable.empty()
                        drawable.empty()

                        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                        asteroid_field = AsteroidField()

                    elif event.key == pygame.K_q:
                        sys.exit()

        
        screen.fill("black")

        if game_over:
            game_over_text_surface = score_font.render("GAME OVER!", True, (255, 0, 0))
            go_x = (SCREEN_WIDTH - game_over_text_surface.get_width()) / 2
            go_y = (SCREEN_HEIGHT - game_over_text_surface.get_height()) / 2 - 20 # A bit above center
            screen.blit(game_over_text_surface, (go_x, go_y))

            final_score_text_surface = score_font.render(f"Final Score: {score.score}", True, (255, 255, 255)) # White text
            fs_x = (SCREEN_WIDTH - final_score_text_surface.get_width()) / 2
            fs_y = go_y + game_over_text_surface.get_height() + 10 # Below "GAME OVER"
            screen.blit(final_score_text_surface, (fs_x, fs_y))

            restart_quit_message_surface = score_font.render("Press 'R' to Restart or 'Q' to Quit", True, (255, 0, 0))
            rq_x = (SCREEN_WIDTH - restart_quit_message_surface.get_width()) / 2
            rq_y = fs_y + final_score_text_surface.get_height() + 10
            screen.blit(restart_quit_message_surface, (rq_x, rq_y))

        else:
            updatable.update(dt)
            score_text_surface = score_font.render(str(score.score), True, (255, 255, 255))
            screen.blit(score_text_surface, (10, 10))
        
            for asteroid in asteroids:
                for shot in shots:
                    if asteroid.collision(shot):
                        shot.kill()
                        score.points(asteroid.radius)
                        asteroid.split()

            for object in drawable:
                object.draw(screen)

            for asteroid in asteroids:
                    if asteroid.collision(player):
                        game_over = True


        pygame.display.flip()

        # limits the game to 60 fps
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main() 


