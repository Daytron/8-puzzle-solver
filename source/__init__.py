__author__ = 'DaytronSledge'

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import classes

# Globals
WIDTH = 900
HEIGHT = 620

x_pos_puzzle = 50
y_pos_puzzle = 80
x_pos_input = 500
y_pos_input = 200
x_pos_goal = 50
y_pos_goal = 370
tile_wide = 70

tile_counter_input = 1
tile_list_input = []

color_input_bg = 'White'
color_puzzle_bg = 'White'
color_blank_tile = 'Teal'

isInputOn = True
isTile1LockOn = True
isTile2LockOn = True
isTile3LockOn = True
isTile4LockOn = True
isTile5LockOn = True
isTile6LockOn = True
isTile7LockOn = True
isTile8LockOn = True
isTile9LockOn = True


def draw(canvas):
    # Positions for puzzle tiles
    x = x_pos_puzzle
    y = y_pos_puzzle

    # Square size
    s = tile_wide

    # Draw puzzle text
    canvas.draw_text('Initial State', (50, 70), 22, 'Black', 'serif')

    # Draw puzzle tiles
    canvas.draw_polygon([[x, y], [x, y + s], [x + s, y + s], [x + s, y]], 2, 'Black', color_puzzle_bg)
    canvas.draw_polygon([[x + s, y], [x + s, y + s], [x + (2 * s), y + s], [x + (2 * s), y]], 2, 'Black',
                        color_puzzle_bg)
    canvas.draw_polygon([[x + (2 * s), y], [x + (2 * s), y + s], [x + (3 * s), y + s], [x + (3 * s), y]], 2, 'Black',
                        color_puzzle_bg)

    canvas.draw_polygon([[x, y + s], [x, y + (2 * s)], [x + s, y + (2 * s)], [x + s, y + s]], 2, 'Black',
                        color_puzzle_bg)
    canvas.draw_polygon([[x + s, y + s], [x + s, y + (2 * s)], [x + (2 * s), y + (2 * s)], [x + (2 * s), y + s]], 2,
                        'Black', color_puzzle_bg)
    canvas.draw_polygon(
        [[x + (2 * s), y + s], [x + (2 * s), y + (2 * s)], [x + (3 * s), y + (2 * s)], [x + (3 * s), y + s]], 2,
        'Black',
        color_puzzle_bg)

    canvas.draw_polygon([[x, y + (2 * s)], [x, y + (3 * s)], [x + s, y + (3 * s)], [x + s, y + (2 * s)]], 2, 'Black',
                        color_puzzle_bg)
    canvas.draw_polygon(
        [[x + s, y + (2 * s)], [x + s, y + (3 * s)], [x + (2 * s), y + (3 * s)], [x + (2 * s), y + (2 * s)]], 2,
        'Black',
        color_puzzle_bg)
    canvas.draw_polygon([[x + (2 * s), y + (2 * s)], [x + (2 * s), y + (3 * s)], [x + (3 * s), y + (3 * s)],
                         [x + (3 * s), y + (2 * s)]], 2, 'Black',
                        color_puzzle_bg)

    # Positions for puzzle tiles
    n = x_pos_goal
    m = y_pos_goal

    # Square size
    s = tile_wide

    # Draw puzzle text
    canvas.draw_text('Goal State', (50, 360), 22, 'Black', 'serif')

    # Draw puzzle tiles
    canvas.draw_polygon([[n, m], [n, m + s], [n + s, m + s], [n + s, m]], 2, 'Black', color_puzzle_bg)
    canvas.draw_polygon([[n + s, m], [n + s, m + s], [n + (2 * s), m + s], [n + (2 * s), m]], 2, 'Black',
                        color_puzzle_bg)
    canvas.draw_polygon([[n + (2 * s), m], [n + (2 * s), m + s], [n + (3 * s), m + s], [n + (3 * s), m]], 2, 'Black',
                        color_puzzle_bg)

    canvas.draw_polygon([[n, m + s], [n, m + (2 * s)], [n + s, m + (2 * s)], [n + s, m + s]], 2, 'Black',
                        color_puzzle_bg)
    canvas.draw_polygon([[n + s, m + s], [n + s, m + (2 * s)], [n + (2 * s), m + (2 * s)], [n + (2 * s), m + s]], 2,
                        'Black', color_puzzle_bg)
    canvas.draw_polygon(
        [[n + (2 * s), m + s], [n + (2 * s), m + (2 * s)], [n + (3 * s), m + (2 * s)], [n + (3 * s), m + s]], 2,
        'Black',
        color_puzzle_bg)

    canvas.draw_polygon([[n, m + (2 * s)], [n, m + (3 * s)], [n + s, m + (3 * s)], [n + s, m + (2 * s)]], 2, 'Black',
                        color_puzzle_bg)
    canvas.draw_polygon(
        [[n + s, m + (2 * s)], [n + s, m + (3 * s)], [n + (2 * s), m + (3 * s)], [n + (2 * s), m + (2 * s)]], 2,
        'Black',
        color_puzzle_bg)
    canvas.draw_polygon([[n + (2 * s), m + (2 * s)], [n + (2 * s), m + (3 * s)], [n + (3 * s), m + (3 * s)],
                         [n + (3 * s), m + (2 * s)]], 2, 'Black',
                        color_puzzle_bg)


    # Positions for input tiles
    v = x_pos_input
    w = y_pos_input

    # Positions for drawing the number
    v_centre = ((v + v + s) / 2) - 10
    w_centre = ((w + w + s) / 2) + 15

    # Draw puzzle text
    #canvas.draw_text('Goal State', (50, 400), 22, 'Black', 'serif')

    if isTile1LockOn is True:
        canvas.draw_polygon([[v, w], [v, w + s], [v + s, w + s], [v + s, w]], 2, 'Black', color_input_bg)
        canvas.draw_text('1', (v_centre, w_centre), 40, 'Black', 'monospace')

    if isTile2LockOn is True:
        canvas.draw_polygon([[v + s, w], [v + s, w + s], [v + (2 * s), w + s], [v + (2 * s), w]], 2, 'Black',
                            color_input_bg)
        canvas.draw_text('2', (v_centre + s, w_centre), 40, 'Black', 'monospace')

    if isTile3LockOn is True:
        canvas.draw_polygon([[v + (2 * s), w], [v + (2 * s), w + s], [v + (3 * s), w + s], [v + (3 * s), w]], 2,
                            'Black', color_input_bg)
        canvas.draw_text('3', (v_centre + (2 * s), w_centre), 40, 'Black', 'monospace')

    if isTile4LockOn is True:
        canvas.draw_polygon([[v, w + s], [v, w + (2 * s)], [v + s, w + (2 * s)], [v + s, w + s]], 2, 'Black',
                            color_input_bg)
        canvas.draw_text('4', (v_centre, w_centre + s), 40, 'Black', 'monospace')

    if isTile5LockOn is True:
        canvas.draw_polygon([[v + s, w + s], [v + s, w + (2 * s)], [v + (2 * s), w + (2 * s)], [v + (2 * s), w + s]], 2,
                            'Black',
                            color_input_bg)
        canvas.draw_text('5', (v_centre + s, w_centre + s), 40, 'Black', 'monospace')

    if isTile6LockOn is True:
        canvas.draw_polygon(
            [[v + (2 * s), w + s], [v + (2 * s), w + (2 * s)], [v + (3 * s), w + (2 * s)], [v + (3 * s), w + s]], 2,
            'Black',
            color_input_bg)
        canvas.draw_text('6', (v_centre + (2 * s), w_centre + s), 40, 'Black', 'monospace')

    if isTile7LockOn is True:
        canvas.draw_polygon([[v, w + (2 * s)], [v, w + (3 * s)], [v + s, w + (3 * s)], [v + s, w + (2 * s)]], 2,
                            'Black', color_input_bg)
        canvas.draw_text('7', (v_centre, w_centre + (2 * s)), 40, 'Black', 'monospace')

    if isTile8LockOn is True:
        canvas.draw_polygon(
            [[v + s, w + (2 * s)], [v + s, w + (3 * s)], [v + (2 * s), w + (3 * s)], [v + (2 * s), w + (2 * s)]], 2,
            'Black',
            color_input_bg)
        canvas.draw_text('8', (v_centre + s, w_centre + (2 * s)), 40, 'Black', 'monospace')

    if isTile9LockOn is True:
        canvas.draw_polygon([[v + (2 * s), w + (2 * s)], [v + (2 * s), w + (3 * s)], [v + (3 * s), w + (3 * s)],
                             [v + (3 * s), w + (2 * s)]], 2,
                            'Black', color_blank_tile)

    # Draw from selected input tiles
    if isInputOn is True:
        x_centre = ((x + x + s) / 2) - 10
        y_centre = ((y + y + s) / 2) + 15
        draw_tile_counter = 1

        for tile_num in tile_list_input:
            x_draw = x_centre
            y_draw = y_centre

            if draw_tile_counter is 2:
                x_draw = x_centre + s
            elif draw_tile_counter is 3:
                x_draw = x_centre + (2 * s)
            elif draw_tile_counter is 4:
                y_draw = y_centre + s
            elif draw_tile_counter is 5:
                x_draw = x_centre + s
                y_draw = y_centre + s
            elif draw_tile_counter is 6:
                x_draw = x_centre + (2 * s)
                y_draw = y_centre + s
            elif draw_tile_counter is 7:
                y_draw = y_centre + (2 * s)
            elif draw_tile_counter is 8:
                x_draw = x_centre + s
                y_draw = y_centre + (2 * s)
            elif draw_tile_counter is 9:
                x_draw = x_centre + (2 * s)
                y_draw = y_centre + (2 * s)
            if tile_num is not '0':
                canvas.draw_text(tile_num, (x_draw, y_draw), 40, 'Black', 'monospace')

            draw_tile_counter += 1

    return None


def mouse_handler_input(pos):
    global tile_counter_input, isInputOn, tile_list_input
    global isTile1LockOn, isTile2LockOn, isTile3LockOn, isTile4LockOn, isTile5LockOn, isTile6LockOn
    global isTile7LockOn, isTile8LockOn, isTile9LockOn

    #print "tile_list_input:", tile_list_input
    if (isInputOn is True) and (tile_counter_input < 10):

        if isTile1LockOn is True:
            if (pos[0] < (x_pos_input + tile_wide) and pos[0] > x_pos_input) and \
                    (pos[1] < (y_pos_input + tile_wide) and pos[1] > y_pos_input):
                tile_list_input.append('1')
                tile_counter_input += 1
                isTile1LockOn = False
                return None

        if isTile2LockOn is True:
            if (pos[0] < (x_pos_input + (2 * tile_wide)) and pos[0] > (x_pos_input + tile_wide)) and \
                    (pos[1] < (y_pos_input + tile_wide) and pos[1] > y_pos_input):
                tile_list_input.append('2')
                tile_counter_input += 1
                isTile2LockOn = False
                return None

        if isTile3LockOn is True:
            if (pos[0] < (x_pos_input + (3 * tile_wide)) and pos[0] > (x_pos_input + (2 * tile_wide))) and \
                    (pos[1] < (y_pos_input + tile_wide) and pos[1] > y_pos_input):
                tile_list_input.append('3')
                tile_counter_input += 1
                isTile3LockOn = False
                return None

        if isTile4LockOn is True:
            if (pos[0] < (x_pos_input + tile_wide) and pos[0] > x_pos_input) and \
                    (pos[1] < (y_pos_input + (2 * tile_wide)) and pos[1] > (y_pos_input + tile_wide)):
                tile_list_input.append('4')
                tile_counter_input += 1
                isTile4LockOn = False
                return None

        if isTile5LockOn is True:
            if (pos[0] < (x_pos_input + (2 * tile_wide)) and pos[0] > (x_pos_input + tile_wide)) and \
                    (pos[1] < (y_pos_input + (2 * tile_wide)) and pos[1] > (y_pos_input + tile_wide)):
                tile_list_input.append('5')
                tile_counter_input += 1
                isTile5LockOn = False
                return None

        if isTile6LockOn is True:
            if (pos[0] < (x_pos_input + (3 * tile_wide)) and pos[0] > (x_pos_input + (2 * tile_wide))) and \
                    (pos[1] < (y_pos_input + (2 * tile_wide)) and pos[1] > (y_pos_input + tile_wide)):
                tile_list_input.append('6')
                tile_counter_input += 1
                isTile6LockOn = False
                return None

        if isTile7LockOn is True:
            if (pos[0] < (x_pos_input + tile_wide) and pos[0] > x_pos_input) and \
                    (pos[1] < (y_pos_input + (3 * tile_wide)) and pos[1] > (y_pos_input + (2 * tile_wide))):
                tile_list_input.append('7')
                tile_counter_input += 1
                isTile7LockOn = False
                return None

        if isTile8LockOn is True:
            if (pos[0] < (x_pos_input + (2 * tile_wide)) and pos[0] > (x_pos_input + tile_wide)) and \
                    (pos[1] < (y_pos_input + (3 * tile_wide)) and pos[1] > (y_pos_input + (2 * tile_wide))):
                tile_list_input.append('8')
                tile_counter_input += 1
                isTile8LockOn = False
                return None

        if isTile9LockOn is True:
            if (pos[0] < (x_pos_input + (3 * tile_wide)) and pos[0] > (x_pos_input + (2 * tile_wide))) and \
                    (pos[1] < (y_pos_input + (3 * tile_wide)) and pos[1] > (y_pos_input + (2 * tile_wide))):
                tile_list_input.append('0')
                tile_counter_input += 1
                isTile9LockOn = False
                return None


frame = simplegui.create_frame("8 Puzzle Solver", WIDTH, HEIGHT)
frame.set_canvas_background('Silver')
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(mouse_handler_input)

frame.start()