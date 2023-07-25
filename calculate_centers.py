"""
File that contains teh calculations for the triangle centers
"""

from math import sqrt, dist

def centroid(verticies:list) -> tuple:
    """The point where all three medians intersect - notated by G

Parameters:
    verticies: a list of the three points of the triangle"""

    # find the average of the three points
    x_total = 0
    y_total = 0
    for current_point in verticies:
        x_total += current_point[0]
        y_total += current_point[1]
    
    x_average = x_total / 3
    y_average = y_total / 3

    # return the average
    return (x_average, y_average)


def orthocenter(verticies:list) -> tuple:
    """The point where all altitudes intersect - notated by H

Parameters:
    verticies: a list of the three points of the triangle"""

    # set variables to work with
    x1, x2, x3 = verticies[0][0], verticies[1][0], verticies[2][0]
    y1, y2, y3 = verticies[0][1], verticies[1][1], verticies[2][1]

    # set booleans for error prevention
    # these are used to ensure that 0 and inf cases don't break the calculations
    no_slope_one = True
    has_x = False
    has_y = False

    # find the slopes of two of the perpendicular bisector from the points
    # slope one
    if (y_difference := y2 - y1) == 0:
        return_x = x3
        has_x = True
    elif (x_difference := x2 - x1) == 0:
        return_y = y3
        has_y = True
    else:
        slope_one = -1/(y_difference / x_difference)
        no_slope_one = False
    
    # slope two
    if (y_difference := y3 - y2) == 0:
        return_x = x1
        has_x = True
    elif (x_difference := x3 - x2) == 0:
        return_y = y1
        has_y = True
    else:
        slope_two = -1/(y_difference / x_difference)
    
    # calculate the point from the given slopes (or lack of slopes)
    if has_x:
        if not has_y:
            # has X, doesn't have Y
            if no_slope_one:
                return_y = (slope_two*return_x - (slope_two * x1) + y1)
            else:
                return_y = (slope_one*return_x - (slope_one * x3) + y3)
    else:
        if has_y:
            # has Y, doesn't have X
            if no_slope_one:
                return_x = (return_y + (slope_two * x1) - y1) / slope_two
            else:
                return_x = (return_y + (slope_one * x3) - y3) / slope_one
        else:
            # doesn't have X nor Y
            return_x = ((-slope_two * x1) - y3 + (slope_one * x3) + y1) / (slope_one - slope_two)
            
            return_y = (slope_one*return_x - (slope_one * x3) + y3)

    # return X and Y
    return (return_x, return_y)


def circumcenter(verticies:list) -> tuple:
    """The point where all three perpendicular bisectors intersect - notated by C

Parameters:
    verticies: a list of the three points of the triangle"""


    # set variables to work with
    x1, x2, x3 = verticies[0][0], verticies[1][0], verticies[2][0]
    y1, y2, y3 = verticies[0][1], verticies[1][1], verticies[2][1]

    # set booleans for error prevention
    # these are used to ensure that 0 and inf cases don't break the calculations
    no_slope_one = True
    has_x = False
    has_y = False

    # find the slopes of two of the perpendicular bisectors from the points
    # slope one
    if (y_difference := y2 - y1) == 0:
        return_x = (x2 + x1) / 2
        has_x = True
    elif (x_difference := x2 - x1) == 0:
        return_y = (y2 + y1) / 2
        has_y = True
    else:
        slope_one = -1/(y_difference / x_difference)
        no_slope_one = False
        
    # slope two
    if (y_difference := y3 - y2) == 0:
        return_x = (x3 + x2) / 2
        has_x = True
    elif (x_difference := x3 - x2) == 0:
        return_y = (y3 + y2) / 2
        has_y = True
    else:
        slope_two = -1/(y_difference / x_difference)
    

    # calculate the point from the given slopes (or lack of slopes)
    if has_x:
        if not has_y:
            # has X, doesn't have Y
            if no_slope_one:
                return_y = slope_two * return_x - (slope_two * (x3 + x2) / 2) + (y3 + y2) / 2
            else:
                return_y = slope_one * return_x - (slope_one * (x2 + x1) / 2) + (y2 + y1) / 2
    else:
        if has_y:
            # has Y, doesn't have X
            if no_slope_one:
                return_x = (return_y + (slope_two * (x3 + x2) / 2) - (y3 + y2) / 2) / slope_two
            else:
                return_x = (return_y + (slope_one * (x2 + x1) / 2) - (y2 + y1) / 2) / slope_one
        else:
            # doesn't have X nor Y 
            return_x = (slope_one * (x2 + x1) / 2 - (y2 + y1) / 2 - slope_two * (x3 + x2) / 2 + (y3 + y2) / 2) / (slope_one - slope_two)
            return_y = slope_one * return_x - (slope_one * (x2 + x1) / 2) + (y2 + y1) / 2

    # return X and Y
    return (return_x, return_y)


def incenter(verticies:list, *, return_radius:bool=False) -> float|tuple:
    """The point where all three angle bisectors intersect - notated by I

Parameters:
    verticies: a list of the three points of the triangle"""


    # set variables to work with
    x1, x2, x3 = verticies[0][0], verticies[1][0], verticies[2][0]
    y1, y2, y3 = verticies[0][1], verticies[1][1], verticies[2][1]

    # distances
    a = dist(verticies[1], verticies[2])
    b = dist(verticies[0], verticies[2])
    c = dist(verticies[0], verticies[1])

    # incenter formula
    x = (a * x1 + b * x2 + c * x3) / (a + b + c)
    y = (a * y1 + b * y2 + c * y3) / (a + b + c)
    

    if return_radius:

        # find semi-perimeter
        s = (a + b + c) / 2

        # Heron's Formula
        area = sqrt(s * (s - a) * (s - b) * (s - c))

        # by dividing area but semi-perimeter, we get the radious of the incenter
        return area / s
    
    return (x, y)