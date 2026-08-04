from circleshape import *
from constants import *
from shot import *

class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.cooldown = 0

    # in the Player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()
    
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.cooldown > 0:
                self.cooldown -= dt
            else:
                self.shoot()
            


    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1)
        facing_dir = shot.velocity.rotate(self.rotation)
        if self.cooldown > 0:
            return
        else:
            self.cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
            shot.velocity = facing_dir * PLAYER_SHOOT_SPEED