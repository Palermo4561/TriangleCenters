"""
File containing mathematical calculations with a return value
"""

import pygame as pg
from settings import *
import calculate_centers as cc


def adjust_size_x(x:float) -> float:
    """Changes the mathematical x value into the value that will be represented correctly on the graph

Parameters:
    x: the x value to be changed"""

    return WIDTH / 2 + (x * SCALE)


def adjust_size_y(y:float) -> float:
    """Changes the mathematical y value into the value that will be represented correctly on the graph

Parameters:
    y: the y value to be changed"""
    return WIDTH / 2 - (y * SCALE)


def adjust_both(x:float, y:float) -> tuple:
    """Changes both the mathematical x and y values into the values that will be represented correctly on the graph

Parameters:
    x: the x value to be changed
    y: the y value to be changed"""

    return (adjust_size_x(x), adjust_size_y(y))


def adjust_triangle_verticies(verticies:list) -> list:
    """Changes both the mathematical x and y values into the values that will be represented correctly on the graph for the whole triangle

Parameters:
    verticies: a list of the three verticies of the triangle"""

    return list(map(lambda point : adjust_both(*point), verticies))


def downsize(x:float, y:float) -> tuple:
    """Changes both the graphical x and y values into the correct mathematical values
    
Parameters:
    x: the x value to be changed
    y: the y value to be changed"""

    return ((-WIDTH/2 + x)/SCALE, (WIDTH/2 - y)/SCALE)


def centers(verticies:list) -> tuple:
    """Calculates and returns the graphical values of each center based on the given triangle verticies

Parameters:
    verticies: a list of the three verticies of the triangle"""
    gx, gy = adjust_both(*cc.centroid(verticies))
    hx, hy = adjust_both(*cc.orthocenter(verticies))
    cx, cy = adjust_both(*cc.circumcenter(verticies))
    ix, iy = adjust_both(*cc.incenter(verticies))

    return (gx, gy), (hx, hy), (cx, cy), (ix, iy) 


def selected_point(points:tuple|list, size_of_point:float, was_on_point:bool=True) -> int:
    """Returns the point hovered over by the mouse, or 0 if no point is being hovered over

Parameters:
    points: a sequence of the points being chekced
    size_of_point: the radius of the point, used for the collision box"""

    for i, point in enumerate(points):

        x = point[0]
        y = point[1]

        collision_rect = pg.rect.Rect(x - size_of_point, y - size_of_point, size_of_point * 2, size_of_point * 2)
        
        if pg.Rect.collidepoint(collision_rect, *pg.mouse.get_pos()):
            if not was_on_point:
                pg.mixer.Sound("Point.mp3").play()
            return i + 1
        
    return 0


def check_if_line(vertecies:list) -> bool:
    """Checks to see if the triangle is actually a line 

Parameters:
    vertecies: a list of the three points of the triangle"""

    x1, x2, x3 = vertecies[0][0], vertecies[1][0], vertecies[2][0]
    y1, y2, y3 = vertecies[0][1], vertecies[1][1], vertecies[2][1]

    is_line = (x1 == x2 == x3) or (y1 == y2 == y3)

    if x2 - x1 == 0:
        return is_line or ((y1 - y3) / (x1 - x3) == (y3 - y2) / (x3 - x2))
    
    if x3 - x2 == 0:
        return is_line or ((y2 - y1) / (x2 - x1) == (y1 - y3) / (x1 - x3))
    
    return is_line or ((y2 - y1) / (x2 - x1) == (y3 - y2) / (x3 - x2))