
DESCRIPTIONS = {

    'Triangle Centers' : """
This is an interactive triangle center
calculator that dynamically shows and 
calculates the 4 centers of a triangle


Hover over a center to veiw the math
and a description for the center

Drag the vertecies to change the
centers' locations 

Hold Left Shift to snap the verticies by
the grid 


Pres Esc or Q to quit""", 

    'Centroid' : """
This is the centroid, marked as 'G'

The centroid is considered the
\"center of mass\" for the triangle, 
where the three lines drawn from each 
vertex to the opposide side's 
midpoint (called medians) intersect

More simply, it is the average of the
three points

Formula:
x = (x1 + x2 + x3) / 3 
y = (y1 + y2 + y3) / 3""", 

    'Orthocenter' : """
This is the Orthocenter, marked as 'H'

The orthocenter is the intersection of the 
three lines that start at each  vertex and end 
at the opposite side at a 90° angle (the 
altitudes of each side)

Steps (formula is too complex):
1. Find the slopes of two lines 
    a. if slope = 0, the opposite vertex's x is 
        the orthocenter's x
    b. if slope = Inf, the opposite vertex's y 
        is the orthocenter's y
2. Find the reciprocal of the non-zero, real 
    slopes and use point-slope to solve for y of 
    each real non-0 slope
3. Set the two lines equal to each other to 
    find x (if no slope is 0)
4. Plug in x in either point-slope to find y 
    (if no slope is Inf)""", 

    'Circumcenter' : """
This is the Circumcenter, marked as 'C'

The circumcenter is the origin of the circle 
that touches each vertex and the intersection 
of the lines comming from each side's midpoint 
at a 90° angle (perpendicular bisectors)

Steps (formula is too complex):
1. Find the slopes of two lines 
    a. if slope = 0, this line's midpoint's
        x is the circumcenter's x
    b. if slope = Inf, this line's midpoint's  
        y is the circumcenter's y
2. Find the reciprocal of the non-zero, real 
    slopes and use point-slope to solve for y of 
    each real non-0 slope
3. Set the two lines equal to each other to 
    find x (if no slope is 0)
4. Plug in x in either point-slope to find y 
    (if no slope is Inf)""", 

    'Incenter' : """
This is the Incenter, marked as 'I'

The incenter is the origin of the
incircle of the triangle, or the 
intersection of the three lines from 
the each vertex that split the vertex's 
angle in half (called angle bisectors)

Formula:
a = sqrt((x3 - x2)² + (y3 - y2)²)
b = sqrt((x1 - x3)² + (y1 - y3)²)
c = sqrt((x1 - x2)² + (y1 - y2)²)

x = (a*x1 + b*x2 + c*x3) / (a+b+c)
y = (a*y1 + b*y2 + c*y3) / (a+b+c)"""
}