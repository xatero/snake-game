import pygame

from snake._snake import SnakeBuilder
from snake.abc import Builder
from snake.common import PgEventList, Size


class World:
    def __init__(self) -> None:
        self._snake = SnakeBuilder().get_result()
        self._grid = None

    def update(self, events: PgEventList) -> None:
        self._snake.update(events, self._grid)

    def draw(self, screen: pygame.Surface) -> None:
        self._snake.draw(screen)


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
