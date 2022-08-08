import pygame 
import sys
from snake.common import Size
from snake.abc import Builder
import typing


pygame.init()

class Game:
    def __init__(self) -> None:
        self._run = True
        self._screen = None

    def add(self, attribute: str, value: typing.Any) -> None:
        self.__dict__[attribute] = value

    def loop(self) -> None:
        while self._run:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    sys.exit()

            self._screen.fill("black")
            pygame.display.flip()

class GameBuilder(Builder):
    """Builds the game"""

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._game = Game()

    def set_screen(self, size: Size, flags: int = 0) -> None:
        self._game.add(
            "_screen",
            pygame.display.set_mode(size, flags)
        )
        return self

    def set_caption(self, title: str) -> None:
        pygame.display.set_caption(f"Snake | {title}")
        return self

    def get_result(self) -> Game:
        return self._game


def main():
    game = (GameBuilder()
            .set_caption("Gameplay")
            .set_screen((500, 500))
            .get_result()
            )
    game.loop()

if __name__ == "__main__":
    main()
