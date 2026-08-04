import pygame, sys
from constants import *
from logger import log_state
from circleshape import *
from player import *
from asteroidfield import *
from asteroid import *
from logger import *
from shot import *

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, drawable, updatable)
    asteroidfield = AsteroidField()
    
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2), PLAYER_RADIUS)
    

    while True:
        log_state()
        for event in pygame.event.get():
            pass
        screen.fill("black")
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60)/1000
        updatable.update(dt)
        for a in asteroids:
            if player.collides_with(a):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for s in shots:
                if s.collides_with(a):
                    log_event("asteroid_shot")
                    s.kill()
                    a.split()
        print(dt)

if __name__ == "__main__":
    main()
