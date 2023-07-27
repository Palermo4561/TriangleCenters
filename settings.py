"""
File containing settings/colors for the program 
"""


SYMBOL = {
    "G" : "Centroid", # centroid
    "H" : "Orthocenter", # orthocenter
    "C" : "Circumcenter", # circumcenter
    "I" : "Incenter"  # incenter
}


POINT_COLORS = {
    "G" : "#ff0000", # centroid
    "H" : "#00ff00", # orthocenter
    "C" : "#0000ff", # circumcenter
    "I" : "#8A009C"  # incenter
}


MAIN_COLORS = {
    "triangle" : "#0C6A00",
    "grid" : "#999999",
    "axes" : "#000000",
    "background" : "#DFDFDF",
    "border" : "#000000",
    "math" : "#16161646",
    "menu" : "#000000"
}


WIDTH = 600
MENU_WIDTH = 400
NUM_BOXES = 20
SCALE = WIDTH / NUM_BOXES
POINT_RADIUS = SCALE // 7
VERTEX_SIZE = SCALE // 4

LABEL_FONT_SIZE = int(SCALE + NUM_BOXES // 6)

FONT_STYLES = {
    'graph' : "Cadisone Sans.ttf", 
    'menu' : None
} 