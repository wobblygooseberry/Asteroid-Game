import random
from constants import *
from circleshape import *
from logger import *

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt 

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle1 = random.uniform(20, 50)
        angle2 = random.uniform(20, 50)
        first_move = self.velocity.rotate(angle1)
        second_move = self.velocity.rotate(-angle2)
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        f_ast = Asteroid(self.position.x, self.position.y, new_rad)
        s_ast = Asteroid(self.position.x, self.position.y, new_rad)
        f_ast.velocity = 1.2 * first_move
        s_ast.velocity = 1.2 * second_move