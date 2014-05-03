__author__ = 'DaytronSledge'

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import classes

# Globals
WIDTH = 700
HEIGHT = 600


def draw(canvas):

    x = 50
    y = 100
    s = 70
    color = 'White'
    canvas.draw_polygon([[x, y], [x, y+s], [x+s, y+s], [x+s, y]], 2, 'Black', 'White')
    canvas.draw_polygon([[x+s, y], [x+s,y+s], [x+(2*s),y+s], [x+(2*s),y]], 2, 'Black', 'White')
    canvas.draw_polygon([[x+(2*s),y], [x+(2*s),y+s], [x+(3*s),y+s], [x+(3*s),y]], 2, 'Black', 'White')

    canvas.draw_polygon([[x, y+s], [x, y+(2*s)], [x+s, y+(2*s)], [x+s, y+s]], 2, 'Black', 'White')
    canvas.draw_polygon([[x+s, y+s], [x+s, y+(2*s)], [x+(2*s), y+(2*s)], [x+(2*s), y+s]], 2, 'Black', 'Teal')
    canvas.draw_polygon([[x+(2*s), y+s], [x+(2*s), y+(2*s)], [x+(3*s), y+(2*s)], [x+(3*s), y+s]], 2, 'Black', 'White')

    canvas.draw_polygon([[x, y+(2*s)], [x, y+(3*s)], [x+s, y+(3*s)], [x+s, y+(2*s)]], 2, 'Black', 'White')
    canvas.draw_polygon([[x+s, y+(2*s)], [x+s, y+(3*s)], [x+(2*s), y+(3*s)], [x+(2*s), y+(2*s)]], 2, 'Black', 'White')
    canvas.draw_polygon([[x+(2*s), y+(2*s)], [x+(2*s), y+(3*s)], [x+(3*s), y+(3*s)], [x+(3*s), y+(2*s)]], 2, 'Black', 'White')

    v = 440
    w = 100
    canvas.draw_polygon([[v, w], [v, w+s], [v+s, w+s], [v+s, w]], 2, 'Black', color)
    canvas.draw_polygon([[v+s, w], [v+s,w+s], [v+(2*s),w+s], [v+(2*s),w]], 2, 'Black', color)
    canvas.draw_polygon([[v+(2*s),w], [v+(2*s),w+s], [v+(3*s),w+s], [v+(3*s),w]], 2, 'Black', color)

    canvas.draw_polygon([[v, w+s], [v, w+(2*s)], [v+s, w+(2*s)], [v+s, w+s]], 2, 'Black', color)
    canvas.draw_polygon([[v+s, w+s], [v+s, w+(2*s)], [v+(2*s), w+(2*s)], [v+(2*s), w+s]], 2, 'Black', color)
    canvas.draw_polygon([[v+(2*s), w+s], [v+(2*s), w+(2*s)], [v+(3*s), w+(2*s)], [v+(3*s), w+s]], 2, 'Black', color)

    canvas.draw_polygon([[v, w+(2*s)], [v, w+(3*s)], [v+s, w+(3*s)], [v+s, w+(2*s)]], 2, 'Black', color)
    canvas.draw_polygon([[v+s, w+(2*s)], [v+s, w+(3*s)], [v+(2*s), w+(3*s)], [v+(2*s), w+(2*s)]], 2, 'Black', color)
    canvas.draw_polygon([[v+(2*s), w+(2*s)], [v+(2*s), w+(3*s)], [v+(3*s), w+(3*s)], [v+(3*s), w+(2*s)]], 2, 'Black', color)

frame = simplegui.create_frame("8 Puzzle Solver", WIDTH, HEIGHT)
frame.set_canvas_background('Silver')
frame.set_draw_handler(draw)

frame.start()