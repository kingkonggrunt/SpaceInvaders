from src.PyGameAssets import PyGameImage
from random import randint

class Alien(PyGameImage):
    def __init__(self):
        super().__init__(dir="assets/001-alien-pixelated-shape-of-a-digital-game.png")
        super().set_boundary(x_lower=0, x_upper=736)
        super().start_coords(randint(0,736), randint(50,150))
        self.speed = 0.20
        self.step_down = 20

    def move_to_player(self):
        """
        Once the alien has reach one of it's x boundaries. Flip the direction
        That the alien goes in the x direction and move the alien downwards.
        """
        super().move(axis=1, amount=self.speed)
        if self.x == self.x_bound_upper:
            self.speed = self.speed/-1
            super().move(axis=0, amount=self.step_down)
        if self.x == self.x_bound_lower:
            self.speed = self.speed/-1
            super().move(axis=0, amount=self.step_down)

    def respawn(self):
        """
        Respawn alien at a new position.

        Respawn alien within the x_bound_lower and x_bound_upper values to prevent
        a bug where respawning on the boundary will not cause the alien to change
        directions and continuously move downards
        """
        super().start_coords(randint(1,735), randint(50,150))
