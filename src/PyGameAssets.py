import pygame

class PyGameImage:
    def __init__(self, dir):
        self.__image = pygame.image.load(dir)

        self.__x = None
        self.__y = None

        self.__x_bound_lower = None
        self.__x_bound_upper = None
        self.__y_bound_lower = None
        self.__y_bound_upper = None

    def start_coords(self, x, y):
        self.__x = x
        self.__y = y

    def render(self, screen, x=None, y=None):
        if x is None and y is None:
            screen.blit(self.__image, (self.__x, self.__y))
        else:
            screen.blit(self.__image, (x,y))

    def set_boundary(self, x_lower=None, x_upper=None, y_upper=None, y_lower=None):
        self.__x_bound_lower = x_lower
        self.__x_bound_upper = x_upper
        self.__y_bound_lower = y_upper
        self.__y_bound_upper = y_lower

    def move(self, axis: bool, amount: int, ignore_boundaries=False):
        # axis == 1 is x axis
        if axis:
            self.__x += amount
        else:
            self.__y += amount

        if not ignore_boundaries:
            if not self.__x_bound_lower is None:
                if self.__x <= self.__x_bound_lower:
                    self.__x = self.__x_bound_lower
            if not self.__x_bound_upper is None:
                if self.__x >= self.__x_bound_upper:
                    self.__x = self.__x_bound_upper
            if not self.__y_bound_lower is None:
                if self.__y <= self.__y_bound_lower:
                    self.__y = self.__y_bound_lower
            if not self.__y_bound_upper is None:
                if self.__y >= self.__y_bound_upper:
                    self.__y = self.__y_bound_upper
