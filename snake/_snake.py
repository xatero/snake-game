import pygame
import time

from snake.abc import Builder
from snake.common import (N_COLS, N_ROWS, TILE_SIZE, GridStructure,
                          PgEventList, Pos)
from snake.enum import SnakeDirection


class BodyPart:
    def __init__(self, pos: Pos) -> None:
        self.pos = pos
        self.surf = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.surf.fill("#FFC482")

    def __repr__(self) -> str:
        return f"<BodyPart({self.pos = })>"


class Snake:
    def __init__(self) -> None:
        self.head = BodyPart(pygame.Vector2((3, 4)))
        self.body: list[BodyPart] = [
            self.head,
        ]
        self.antispeed = None 
        self._last_time = time.time()
        self._last_snake_direction = SnakeDirection.RIGHT
        self.alive = True
        

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
                    self._last_snake_direction = SnakeDirection.RIGHT
                elif event.key == pygame.K_LEFT:
                    self._last_snake_direction = SnakeDirection.LEFT
                elif event.key == pygame.K_UP:
                    self._last_snake_direction = SnakeDirection.UP
                elif event.key == pygame.K_DOWN:
                    self._last_snake_direction = SnakeDirection.DOWN
        
        if (time.time() - self._last_time) > self.antispeed:
            self.move_snake(self._last_snake_direction)
            self._last_time = time.time()

    def process_input(self, grid: GridStructure) -> None:
        if self.head.pos.x == len(grid):
            self.head.pos.x = 0

        elif self.head.pos.y == len(grid[int(self.head.pos.x)]):
            self.head.pos.y = 0

        elif self.head.pos.x < 0:
            self.head.pos.x = N_ROWS - 1

        elif self.head.pos.y < 0:
            self.head.pos.y = N_COLS - 1

    def handle_self_collision(self, grid: GridStructure) -> None:
        row, column = int(self.head.pos.x), int(self.head.pos.y)
        if grid[row][column] == 2:
            self.alive = False

    def update(self, events: PgEventList, grid: GridStructure) -> None:
        self.handle_input(events)
        self.process_input(grid)
        self.handle_self_collision(grid)


    def draw(self, screen: pygame.Surface) -> None:
        for part in self.body:
            screen.blit(part.surf, (part.pos.x * TILE_SIZE, part.pos.y * TILE_SIZE))


    def grow(self) -> None:
        # We take the position of the last body part in the body, 
        # and get the position of the new body part by subtracting
        # one from the x coordinate
        pos = self.body[-1].pos - (1, 0)
        self.body.append(BodyPart(pos))


class SnakeBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self):
        self._snake = Snake()

    def set_antispeed(self, antispeed: float):
        self._snake.antispeed = antispeed
        return self

    def get_result(self) -> Snake:
        return self._snake
