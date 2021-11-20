import pygame

class PyGameImage:
    """
    Image/Asset Handler for PyGame images and assets

    Parameters
    ----------
    dir : str
        local directory of the asset/image

    Attributes
    ----------
    x : int
        Current Asset's X coordinate
    y : int
        Current Asset's Y coordinate
    x_bound_lower : int
        Current Asset's Lower Bound X coordinate. To limit position of asset
    x_bound_upper : int
        Current Asset's Upper Bound X coordinate. To limit position of asset
    y_bound_lower : int
        Current Asset's Lower Bound Y coordinate. To limit position of asset
    y_bound_upper : int
        Current Asset's Upper Bound Y coordinate. To limit position of asset
    """
    def __init__(self, dir):
        self._image = pygame.image.load(dir)

        self.x = None
        self.y = None

        self.x_bound_lower = None
        self.x_bound_upper = None
        self.y_bound_lower = None
        self.y_bound_upper = None

    def start_coords(self, x, y):
        self.x = x
        self.y = y

    def render(self, screen, x=None, y=None):
        if x is None and y is None:
            screen.blit(self._image, (self.x, self.y))
        else:
            screen.blit(self._image, (x,y))

    def set_boundary(self, x_lower=None, x_upper=None, y_upper=None, y_lower=None):
        """
        Set's the boundary of the asset. Can be used to limit the movement and possible positions an asset can be located.

        Parameters
        ----------
        x_lower : int
            Lower X coordinate boundary
        x_upper : int
            Upper X coordinate boundary
        y_lower : int
            Lower Y coordinate boundary
        y_upper : int
            Upper Y coordinate boundary
        """
        self.x_bound_lower = x_lower
        self.x_bound_upper = x_upper
        self.y_bound_lower = y_lower
        self.y_bound_upper = y_upper

    def move(self, axis: bool, amount: int, ignore_boundaries=False):
        # axis == 1 is x axis
        if axis:
            self.x += amount
        else:
            self.y += amount

        if not ignore_boundaries:
            if not self.x_bound_lower is None:
                if self.x <= self.x_bound_lower:
                    self.x = self.x_bound_lower
            if not self.x_bound_upper is None:
                if self.x >= self.x_bound_upper:
                    self.x = self.x_bound_upper
            if not self.y_bound_lower is None:
                if self.y <= self.y_bound_lower:
                    self.y = self.y_bound_lower
            if not self.y_bound_upper is None:
                if self.y >= self.y_bound_upper:
                    self.y = self.y_bound_upper
