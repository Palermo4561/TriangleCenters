"""
File containing the main function of the program 
"""

import pygame as pg
import numpy as np
import sys, draw, calculate
from settings import *
import functions
import asyncio


async def main() -> None:
    """Main funciton 
Parameters: None"""

    # setup 
    functions.setup()

    # initial example verticies 
    vertecies = [[-9, -2], [4, -7], [8, 8]]

    # booleans
    mouse_down = False
    is_changing_vertex = False
    left_shift = False
    center_is_selected = False
    played_select_sound = False
    muted = False
    running = True

    # main loop
    while running:

        # checking if "triangle" is just a strait line 
        is_line = calculate.check_if_line(vertecies)

        # event loop 
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_down = True
            if event.type == pg.MOUSEBUTTONUP:
                mouse_down = False
                is_changing_vertex = False
                played_select_sound = False
                if pg.Rect(0.93 * (WIDTH + MENU_WIDTH), 0.9 * WIDTH, 0.07 * (WIDTH + MENU_WIDTH), 0.1 * WIDTH).collidepoint(pg.mouse.get_pos()):
                    muted = functions.change_pause(muted)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LSHIFT:
                    left_shift = True
                if event.key in (pg.K_q, pg.K_ESCAPE):
                    running = False
                    pg.quit()
                    sys.exit()
                if event.key == pg.K_m:
                    muted = functions.change_pause(muted)
            if event.type == pg.KEYUP:
                if event.key == pg.K_LSHIFT:
                    left_shift = False

        # make triangle points correlate to the grid on the screen
        adjusted_triangle_points = calculate.adjust_triangle_verticies(vertecies)

        # draw the graph and grid
        draw.graph()
        draw.triangle(adjusted_triangle_points)

        # check and, therefore, record if/which vertex is being moved
        if (selected_vertex := calculate.selected_point(adjusted_triangle_points, VERTEX_SIZE, muted)) and mouse_down:
            is_changing_vertex = True
            changing_vertex = selected_vertex - 1
        
        # calculate and draw centers if the triangle is a triangle (not a line)
        if not is_line:
            centers = calculate.centers(vertecies)

            # draw all centers or only the one being hovered over 
            if not (selected_center := calculate.selected_point(centers, POINT_RADIUS, muted, center_is_selected)):
                draw.centers(centers, adjusted_triangle_points)
            else:
                draw.centers(centers, adjusted_triangle_points, only_show=selected_center)
        else:
            draw.menu_description('Triangle Centers')
        
        # move the triangle vertex, if selected
        if mouse_down and is_changing_vertex:

            if not (played_select_sound or muted):
                pg.mixer.Sound("Point.mp3").play()
                played_select_sound = True
        
            x, y = calculate.downsize(*pg.mouse.get_pos())

            if pg.mouse.get_pos()[0] <= WIDTH:
                if left_shift:
                    if (vertecies[changing_vertex] != (snap_points := (int(x + 0.5 * np.sign(x)), int(y + 0.5 * np.sign(y))))) and not muted:
                        pg.mixer.Sound("Point.mp3").play()
                    vertecies[changing_vertex] = snap_points
                else:
                    vertecies[changing_vertex] = [x, y]
        else:
            is_changing_vertex = False

        # determine if center is currently selected (for audio)
        center_is_selected = bool(selected_center)

        draw.mute_button(muted)

        # update the screen 
        pg.display.update()

        # await for async 
        await asyncio.sleep(0)
    
    # fill the screen black when the program closes 
    pg.display.get_surface().fill('black')
