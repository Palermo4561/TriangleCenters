"""
File containing functions to draw the graphical representation of the centers' math
"""

from settings import *
import calculate_centers, calculate, draw
from math import dist


def centroid(_, vertecies:list) -> None:
    """Draws the mathematical representation for the centroid

Parameters:
    _: dummy variable (makes the other triangle center calculations work with indexing)
    verticies: a list of the three points of the triangle"""

    for n in range(3):
        x = (vertecies[n-1][0] + vertecies[n][0]) / 2
        y = (vertecies[n-1][1] + vertecies[n][1]) / 2
        draw.thick_aa_line((vertecies[n-2][0], vertecies[n-2][1]), (x, y), MAIN_COLORS['math'], 3)


def orthocenter(adjusted_orthocenter:tuple, vertecies:list) -> None:
    """Draws the mathematical representation for the orthocenter

Parameters:
    adjusted_orthocenter: cordinates of the orthocenter
    verticies: a list of the three points of the triangle"""

    orthocenter = calculate.downsize(*adjusted_orthocenter)
    adjusted_vertecies = list(map(lambda v : calculate.downsize(*v), vertecies))

    x1, x2, x3 = adjusted_vertecies[0][0], adjusted_vertecies[1][0], adjusted_vertecies[2][0]
    y1, y2, y3 = adjusted_vertecies[0][1], adjusted_vertecies[1][1], adjusted_vertecies[2][1]

    if x2 != x1 and y2 != y1:
        s1 = (y2-y1)/(x2-x1)
        s2 = -1/s1
        x_end = (-s2*orthocenter[0] + orthocenter[1] + s1*x1 - y1)/(s1-s2)
        y_end = s1*(x_end - x1) + y1
        draw.thick_aa_line(adjusted_orthocenter, calculate.adjust_both(x_end, y_end), MAIN_COLORS['math'], 3)        
    elif x2 == x1:
        draw.thick_aa_line(adjusted_orthocenter, calculate.adjust_both(x1, orthocenter[1]),\
                           MAIN_COLORS['math'], 3)
    else:
        draw.thick_aa_line(adjusted_orthocenter, calculate.adjust_both(orthocenter[0], y1),\
                           MAIN_COLORS['math'], 3)
        
    if x3 != x2 and y3 != y2:
        s1 = (y3-y2)/(x3-x2)
        s2 = -(x3-x2)/(y3-y2)
        x_end = (-s2*orthocenter[0] + orthocenter[1] + s1*x2 - y2)/(s1-s2)
        y_end = s1*(x_end - x2) + y2
        draw.thick_aa_line(adjusted_orthocenter, calculate.adjust_both(x_end, y_end), MAIN_COLORS['math'], 3)
    elif x3 == x2:
        draw.thick_aa_line(adjusted_orthocenter, calculate.adjust_both(x2, orthocenter[1]),\
                           MAIN_COLORS['math'], 3)
    else:
        draw.thick_aa_line(adjusted_orthocenter, calculate.adjust_both(orthocenter[0], y2),\
                           MAIN_COLORS['math'], 3)
        
    if x1 != x3 and y1 != y3:
        s1 = (y1-y3)/(x1-x3)
        s2 = -(x1-x3)/(y1-y3)
        x_end = (-s2*orthocenter[0] + orthocenter[1] + s1*x3 - y3)/(s1-s2)
        y_end = s1*(x_end - x3) + y3
        draw.thick_aa_line(adjusted_orthocenter, calculate.adjust_both(x_end, y_end), MAIN_COLORS['math'], 3)
    elif x1 == x3:
        draw.thick_aa_line(adjusted_orthocenter, calculate.adjust_both(x3, orthocenter[1]),\
                           MAIN_COLORS['math'], 3)
    else:
        draw.thick_aa_line(adjusted_orthocenter, calculate.adjust_both(orthocenter[0], y3),\
                           MAIN_COLORS['math'], 3)

def circumcenter(circumcenter:tuple, vertecies:list) -> None:
    """Draws the mathematical representation for the circumcenter

Parameters:
    circumcenter: cordinates of the circumcenter
    verticies: a list of the three points of the triangle"""

    r = dist(circumcenter, vertecies[0]) + VERTEX_SIZE / 3
    draw.thick_aa_circle(circumcenter, r, MAIN_COLORS['math'], 3)


def incenter(incenter:tuple, vertecies:list) -> None:
    """Draws the mathematical representation for the incenter

Parameters:
    incenter: cordinates of the incenter
    verticies: a list of the three points of the triangle"""

    r = calculate_centers.incenter(vertecies, return_radius=True)
    draw.thick_aa_circle(incenter, r, MAIN_COLORS['math'], 3)