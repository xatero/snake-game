import pygame
import random

from snake._snake import SnakeBuilder
from snake._food import FoodBuilder
from snake.abc import Builder
from snake.common import PgEventList, N_ROWS, N_COLS


class World:
    def __init__(self) -> None:
        self._snake = SnakeBuilder().set_antispeed(0.1).get_result()
        self._grid = None
        self.gen_food()

    def gen_food(self):
        pos_x = random.randrange(N_ROWS)
        pos_y = random.randrange(N_COLS)
        food = (
            FoodBuilder()
            .set_pos(pygame.Vector2(pos_x, pos_y))
            .get_result()
        )
        self._food = food

    def handle_food_snake_collision(self):
        if self._snake.head.pos == self._food.pos:
            self._snake.grow()
            self.gen_food()

    def update(self, events: PgEventList) -> None:
        self._snake.update(events, self._grid)
        self.handle_food_snake_collision()

    def draw(self, screen: pygame.Surface) -> None:
        self._snake.draw(screen)
        self._food.draw(screen)


class WorldBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self):
        self._world = World()

    def set_grid(self, rows: int, cols: int):
        self._world._grid = [[0 for _ in range(cols)] for _ in range(rows)]
        return self

    def get_result(self):
        return self._world
