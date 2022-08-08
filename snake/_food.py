import pygame

from snake.abc import Builder
from snake.common import Pos, TILE_SIZE


class Food:
    def __init__(self) -> None:
        self.pos = None
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill("#db1f48")
        self.rect = self.image.get_rect()
    
    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (
            self.pos.x * TILE_SIZE,
            self.pos.y * TILE_SIZE
        ))


class FoodBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self):
        self._food = Food()

    def set_pos(self, pos: Pos):
        self._food.pos = pos 
        return self

    def get_result(self):
        return self._food

