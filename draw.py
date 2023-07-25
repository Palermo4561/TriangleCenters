"""
File with functions to draw various graphical components of the program 
"""

import pygame as pg
from pygame import gfxdraw
import draw_math as dm
from settings import *


def thick_aa_line(start:tuple|list, end:tuple|list, color:str, thickness:int) -> None:
    """Draws multiple aalines to create a thickness to the aaline

Parameters:
    start: starting point of the line
    end: ending point of the line 
    color: hex color of the line
    thickness: thickness of the line"""

    screen = pg.display.get_surface()
    top = thickness % 2

    for _ in range(thickness):
        pg.draw.aaline(screen, color, (start[0], start[1] + top), (end[0], end[1] + top), 5)
        pg.draw.aaline(screen, color, (start[0] + top, start[1]), (end[0] + top, end[1]), 5)
        top -= 1


def thick_aa_lines(points:list, color:str, thickness:int) -> None:
    """Draws multiple connected thick aalines

Parameters:
    points: points to be connected with the aalines 
    color: hex color of the line
    thickness: thickness of the line"""

    for p in range(len(points)):
        thick_aa_line(points[p-1], points[p], color, thickness)
        

def aa_filled_circle(center:tuple|list, radius:float, color:str) -> None:
    """Draws a filled aacircle

Parameters:
    center: center point
    radius: radius of the circle
    color: hex color of the circle"""

    screen = pg.display.get_surface()
    
    if all(abs(cordinate) < 1000 for cordinate in center):

        gfxdraw.aacircle(screen, *(map(lambda x : int(x), center)), int(radius), pg.Color(color))
        gfxdraw.filled_circle(screen, *(map(lambda x : int(x), center)), int(radius), pg.Color(color))


def thick_aa_circle(center:tuple|list, radius:float, color_hex_value:str, thickness:int) -> None:
    """Draws multiple aacircle to make one thick aacircle

Parameters:
    center: center point
    radius: radius of the circle
    color_hex_value: hex color of the circle
    thickness: thickness of the line"""

    screen = pg.display.get_surface()
    top = thickness % 2

    for _ in range(thickness):
        for __ in range(10):
            gfxdraw.aacircle(screen, *(map(lambda x : int(x), center)), int(radius + top), pg.Color(color_hex_value))
        top -= 1


def graph() -> None:
    """Draws the grid and axes of the graph

Parameters: None"""

    screen = pg.display.get_surface()
    screen.fill(MAIN_COLORS['background'])

    for i in range(NUM_BOXES + 1):
        current_pos = i * SCALE
        pg.draw.line(screen, MAIN_COLORS['grid'], (current_pos, 0), (current_pos, WIDTH))
        pg.draw.line(screen, MAIN_COLORS['grid'], (0, current_pos), (WIDTH, current_pos))

    pg.draw.line(screen, MAIN_COLORS['axes'], (WIDTH / 2, 0), (WIDTH / 2, WIDTH), 2)
    pg.draw.line(screen, MAIN_COLORS['axes'], (0, WIDTH / 2), (WIDTH, WIDTH / 2), 2)
    pg.draw.rect(screen, MAIN_COLORS['border'], pg.rect.Rect(0, 0, WIDTH, WIDTH), 3)


def label(point:list, label:str, *, offsetX:float=0, offsetY:float=0) -> None:
    """Labels a point

Parameters:
    point: the point being labeled
    label: the string to label the point with 
    offsetX: offset in the x direction
    offsetY: offset in the y direction"""

    label = pg.font.Font(FONT_STYLE, LABEL_FONT_SIZE).render(label, True, 'black')

    center = (point[0] + offsetX, point[1] + offsetY)
    pg.display.get_surface().blit(label, label.get_rect(center=(center)))


def triangle(verticies:list) -> None:
    """Draws the triangle

Parameters:
    verticies: a list of the three points of the triangle"""

    thick_aa_lines(verticies, MAIN_COLORS['triangle'], 3)
    for i, point in enumerate(verticies):
        aa_filled_circle(point, VERTEX_SIZE, MAIN_COLORS['triangle'])
        label(point, f'P{i + 1}', offsetX=LABEL_FONT_SIZE + 3)


def centers(centers:tuple, vertecies:list, *, only_show:int=0) -> None:
    """Draws the center(s)

Parameters:
    centers = a tuple of the center cordinates
    verticies: a list of the three points of the triangle
    only_show: an optional integer specifying which, if any, center should be the only center shown"""
    
    symbol_order = ('G', 'H', 'C', 'I')
    draw_functions = (dm.centroid, dm.orthocenter, dm.circumcenter, dm.incenter)

    if only_show:

        shown = only_show - 1
        cordinates = centers[shown]

        aa_filled_circle(cordinates, POINT_RADIUS, POINT_COLORS[symbol_order[shown]])
        label(cordinates, SYMBOL[symbol_order[shown]], offsetY=-(LABEL_FONT_SIZE // 2))
        draw_functions[shown](cordinates, vertecies)

    else:

        for i, letter in enumerate(symbol_order):
            aa_filled_circle(centers[i], POINT_RADIUS, POINT_COLORS[letter])
            label(centers[i], letter, offsetX=LABEL_FONT_SIZE/2)