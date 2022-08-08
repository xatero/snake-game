import sys
import typing

import pygame

from snake._world import WorldBuilder
from snake.abc import Builder
from snake.common import N_COLS, N_ROWS, Size

pygame.init()


class Game:
    def __init__(self) -> None:
        self._run = True
        self._screen = None
        self._world = WorldBuilder().set_grid(N_ROWS, N_COLS).get_result()

    def add(self, attribute: str, value: typing.Any) -> None:
        self.__dict__[attribute] = value

    def loop(self) -> None:
        while self._run:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    sys.exit()

            self._world.update(events)

            self._screen.fill("#496A81")
            self._world.draw(self._screen)
            pygame.display.flip()


class GameBuilder(Builder):
    """Builds the game"""

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._game = Game()

    def set_screen(self, size: Size, flags: int = 0) -> None:
        self._game.add("_screen", pygame.display.set_mode(size, flags))
        return self

    def set_caption(self, title: str) -> None:
        pygame.display.set_caption(f"Snake | {title}")
        return self

    def get_result(self) -> Game:
        return self._game


def main():
    game = GameBuilder().set_caption("Gameplay").set_screen((500, 500)).get_result()
    game.loop()


if __name__ == "__main__":
    main()
