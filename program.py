"""
File containing the main function of the program 
"""

import pygame as pg
import numpy as np
import sys, draw, calculate
from settings import *


def setup() -> None:
    """Basic setup for the program
    
Parameters: None"""

    pg.display.set_mode((WIDTH + MENU_WIDTH, WIDTH))
    pg.display.set_caption("Triangle Centers")
    pg.display.set_icon(pg.image.load("triangle_icon.png"))

    pg.mixer.music.load("Background Music.mp3")
    pg.mixer.music.play(-1)


def main() -> None:
    """Main funciton 
Parameters: None"""

    # setup 
    setup()

    # initial example verticies 
    vertecies = [[-9, -2], [4, -7], [8, 8]]

    # booleans
    mouse_down = False
    is_changing_vertex = False
    left_shift = False
    center_is_selected = False
    played_select_sound = False

    # main loop
    while True:

        # checking if "triangle" is just a strait line 
        is_line = calculate.check_if_line(vertecies)

        # event loop 
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_down = True
            if event.type == pg.MOUSEBUTTONUP:
                mouse_down = False
                is_changing_vertex = False
                played_select_sound = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LSHIFT:
                    left_shift = True
                if event.key in (pg.K_q, pg.K_ESCAPE):
                    pg.quit()
                    sys.exit()
            if event.type == pg.KEYUP:
                if event.key == pg.K_LSHIFT:
                    left_shift = False

        # make triangle points correlate to the grid on the screen
        adjusted_triangle_points = calculate.adjust_triangle_verticies(vertecies)

        # draw the graph and grid
        draw.graph()
        draw.triangle(adjusted_triangle_points)

        # check and, therefore, record if/which vertex is being moved
        if (selected_vertex := calculate.selected_point(adjusted_triangle_points, VERTEX_SIZE)) and mouse_down:
            is_changing_vertex = True
            changing_vertex = selected_vertex - 1
        
        # calculate and draw centers if the triangle is a triangle (not a line)
        if not is_line:
            centers = calculate.centers(vertecies)

            # draw all centers or only the one being hovered over 
            if not (selected_center := calculate.selected_point(centers, POINT_RADIUS, center_is_selected)):
                draw.centers(centers, adjusted_triangle_points)
            else:
                draw.centers(centers, adjusted_triangle_points, only_show=selected_center)
        else:
            draw.menu_description('Triangle Centers')
        
        # move the triangle vertex, if selected
        if mouse_down and is_changing_vertex:

            if not played_select_sound:
                pg.mixer.Sound("Point.mp3").play()
                played_select_sound = True
        
            x, y = calculate.downsize(*pg.mouse.get_pos())

            if pg.mouse.get_pos()[0] <= WIDTH:
                if left_shift:
                    if (vertecies[changing_vertex] != (snap_points := (int(x + 0.5 * np.sign(x)), int(y + 0.5 * np.sign(y))))):
                        pg.mixer.Sound("Point.mp3").play()
                    vertecies[changing_vertex] = snap_points
                else:
                    vertecies[changing_vertex] = [x, y]
        else:
            is_changing_vertex = False

        # determine if center is currently selected (for audio)
        center_is_selected = bool(selected_center)

        # update the screen 
        pg.display.update()