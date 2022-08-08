import pygame

from snake.abc import Builder
from snake.common import (N_COLS, N_ROWS, TILE_SIZE, GridStructure,
                          PgEventList, Pos)
from snake.enum import SnakeDirection


class BodyPart:
    def __init__(self, pos: Pos) -> None:
        self.pos = pos
        self.surf = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.surf.fill("red")

    def __repr__(self) -> str:
        return f"<BodyPart({self.pos = })>"


class Snake:
    def __init__(self) -> None:
        self.head = BodyPart(pygame.Vector2((3, 4)))
        self.body: list[BodyPart] = [
            self.head,
            BodyPart(pygame.Vector2((2, 4))),
            BodyPart(pygame.Vector2((1, 4))),
        ]

    def move_snake(self, direction: SnakeDirection):
        # Move the head
        next_poses = [part.pos.copy() for part in self.body[:-1]]
        self.head.pos += direction.value

        # Move the rest of the body
        for part, next_pos in zip(self.body[1:], next_poses):
            part.pos = next_pos

    def handle_input(self, events: PgEventList) -> None:
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.move_snake(SnakeDirection.RIGHT)
                elif event.key == pygame.K_LEFT:
                    self.move_snake(SnakeDirection.LEFT)
                elif event.key == pygame.K_UP:
                    self.move_snake(SnakeDirection.UP)
                elif event.key == pygame.K_DOWN:
                    self.move_snake(SnakeDirection.DOWN)

    def process_input(self, grid: GridStructure) -> None:
        if self.head.pos.x == len(grid):
            self.head.pos.x = 0

        elif self.head.pos.y == len(grid[int(self.head.pos.x)]):
            self.head.pos.y = 0

        elif self.head.pos.x < 0:
            self.head.pos.x = N_ROWS - 1
            print(self.head.pos.x)

        elif self.head.pos.y < 0:
            self.head.pos.y = N_COLS - 1

    def update(self, events: PgEventList, grid: GridStructure) -> None:
        self.handle_input(events)
        self.process_input(grid)

    def draw(self, screen: pygame.Surface) -> None:
        for part in self.body:
            screen.blit(part.surf, (part.pos.x * TILE_SIZE, part.pos.y * TILE_SIZE))


class SnakeBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self):
        self._snake = Snake()

    def get_result(self) -> Snake:
        return self._snake
