import typing 
import pygame 


"""Constants"""
TILE_SIZE = 25
N_ROWS = 500 // TILE_SIZE
N_COLS = 500 // TILE_SIZE


"""Type Aliases"""
Size: typing.TypeAlias = tuple[int, int]
Pos: typing.TypeAlias = pygame.Vector2 | tuple | list | typing.Sequence
PgEventList: typing.TypeAlias = list[pygame.event.Event]
GridStructure: typing.TypeAlias = list[list[int, N_COLS], N_ROWS]
