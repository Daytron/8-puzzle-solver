__author__ = 'DaytronSledge'

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import classes

# Constants
# Canvas size
WIDTH = 900
HEIGHT = 620

# Starting coordinates for initial state, goal state and input key
X_POS_PUZZLE = 50
Y_POS_PUZZLE = 80
X_POS_INPUT = 500
Y_POS_INPUT = 200
X_POS_GOAL = 50
Y_POS_GOAL = 370

# Tile size (side)
TILE_WIDE = 70

# Default colors
COLOR_INPUT_BG = 'White'
COLOR_PUZZLE_BG = 'White'
COLOR_TILE_BORDER = 'Black'
COLOR_BLANK_TILE = 'Teal'

# Global variables
# Tile counter
tile_counter_input = 1

# Pattern lists for initial and goal states
initState = []
goalState = []

# Boolean status variables
isDrawGoalText = False
isDrawInstPuzzle = True
isDrawInstGoal = False
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
    global isDrawInstGoal
    # Positions for puzzle tiles
    x = X_POS_PUZZLE
    y = Y_POS_PUZZLE

    # Square size
    s = TILE_WIDE

    # Draw puzzle text
    canvas.draw_text('Initial State', (50, 70), 22, 'Black', 'serif')

    # Draw puzzle tiles
    canvas.draw_polygon([[x, y], [x, y + s], [x + s, y + s], [x + s, y]], 2, COLOR_TILE_BORDER, COLOR_PUZZLE_BG)
    canvas.draw_polygon([[x + s, y], [x + s, y + s], [x + (2 * s), y + s], [x + (2 * s), y]], 2, COLOR_TILE_BORDER,
                        COLOR_PUZZLE_BG)
    canvas.draw_polygon([[x + (2 * s), y], [x + (2 * s), y + s], [x + (3 * s), y + s], [x + (3 * s), y]], 2, COLOR_TILE_BORDER,
                        COLOR_PUZZLE_BG)

    canvas.draw_polygon([[x, y + s], [x, y + (2 * s)], [x + s, y + (2 * s)], [x + s, y + s]], 2, COLOR_TILE_BORDER,
                        COLOR_PUZZLE_BG)
    canvas.draw_polygon([[x + s, y + s], [x + s, y + (2 * s)], [x + (2 * s), y + (2 * s)], [x + (2 * s), y + s]], 2,
                        COLOR_TILE_BORDER, COLOR_PUZZLE_BG)
    canvas.draw_polygon(
        [[x + (2 * s), y + s], [x + (2 * s), y + (2 * s)], [x + (3 * s), y + (2 * s)], [x + (3 * s), y + s]], 2,
        COLOR_TILE_BORDER,
        COLOR_PUZZLE_BG)

    canvas.draw_polygon([[x, y + (2 * s)], [x, y + (3 * s)], [x + s, y + (3 * s)], [x + s, y + (2 * s)]], 2, COLOR_TILE_BORDER,
                        COLOR_PUZZLE_BG)
    canvas.draw_polygon(
        [[x + s, y + (2 * s)], [x + s, y + (3 * s)], [x + (2 * s), y + (3 * s)], [x + (2 * s), y + (2 * s)]], 2,
        COLOR_TILE_BORDER,
        COLOR_PUZZLE_BG)
    canvas.draw_polygon([[x + (2 * s), y + (2 * s)], [x + (2 * s), y + (3 * s)], [x + (3 * s), y + (3 * s)],
                         [x + (3 * s), y + (2 * s)]], 2, COLOR_TILE_BORDER,
                        COLOR_PUZZLE_BG)

    # Positions for puzzle tiles
    n = X_POS_GOAL
    m = Y_POS_GOAL

    # Square size
    s = TILE_WIDE

    # Draw puzzle text
    canvas.draw_text('Goal State', (50, 360), 22, 'Black', 'serif')

    # Draw puzzle tiles
    canvas.draw_polygon([[n, m], [n, m + s], [n + s, m + s], [n + s, m]], 2, COLOR_TILE_BORDER, COLOR_PUZZLE_BG)
    canvas.draw_polygon([[n + s, m], [n + s, m + s], [n + (2 * s), m + s], [n + (2 * s), m]], 2, COLOR_TILE_BORDER,
                        COLOR_PUZZLE_BG)
    canvas.draw_polygon([[n + (2 * s), m], [n + (2 * s), m + s], [n + (3 * s), m + s], [n + (3 * s), m]], 2,
                        COLOR_TILE_BORDER, COLOR_PUZZLE_BG)

    canvas.draw_polygon([[n, m + s], [n, m + (2 * s)], [n + s, m + (2 * s)], [n + s, m + s]], 2, COLOR_TILE_BORDER,
                        COLOR_PUZZLE_BG)
    canvas.draw_polygon([[n + s, m + s], [n + s, m + (2 * s)], [n + (2 * s), m + (2 * s)], [n + (2 * s), m + s]], 2,
                        COLOR_TILE_BORDER, COLOR_PUZZLE_BG)
    canvas.draw_polygon(
        [[n + (2 * s), m + s], [n + (2 * s), m + (2 * s)], [n + (3 * s), m + (2 * s)], [n + (3 * s), m + s]], 2,
        COLOR_TILE_BORDER, COLOR_PUZZLE_BG)
    canvas.draw_polygon([[n, m + (2 * s)], [n, m + (3 * s)], [n + s, m + (3 * s)], [n + s, m + (2 * s)]], 2,
                        COLOR_TILE_BORDER, COLOR_PUZZLE_BG)
    canvas.draw_polygon(
        [[n + s, m + (2 * s)], [n + s, m + (3 * s)], [n + (2 * s), m + (3 * s)], [n + (2 * s), m + (2 * s)]], 2,
        COLOR_TILE_BORDER, COLOR_PUZZLE_BG)
    canvas.draw_polygon([[n + (2 * s), m + (2 * s)], [n + (2 * s), m + (3 * s)], [n + (3 * s), m + (3 * s)],
                         [n + (3 * s), m + (2 * s)]], 2, COLOR_TILE_BORDER, COLOR_PUZZLE_BG)

    # Positions for input tiles
    v = X_POS_INPUT
    w = Y_POS_INPUT

    # Positions for drawing the number
    v_centre = ((v + v + s) / 2) - 10
    w_centre = ((w + w + s) / 2) + 15

    # Draw puzzle text
    #canvas.draw_text('Goal State', (50, 400), 22, 'Black', 'serif')

    if isTile1LockOn is True:
        canvas.draw_polygon([[v, w], [v, w + s], [v + s, w + s], [v + s, w]], 2, COLOR_TILE_BORDER, COLOR_INPUT_BG)
        canvas.draw_text('1', (v_centre, w_centre), 40, 'Black', 'monospace')

    if isTile2LockOn is True:
        canvas.draw_polygon([[v + s, w], [v + s, w + s], [v + (2 * s), w + s], [v + (2 * s), w]], 2, COLOR_TILE_BORDER,
                            COLOR_INPUT_BG)
        canvas.draw_text('2', (v_centre + s, w_centre), 40, 'Black', 'monospace')

    if isTile3LockOn is True:
        canvas.draw_polygon([[v + (2 * s), w], [v + (2 * s), w + s], [v + (3 * s), w + s], [v + (3 * s), w]], 2,
                            COLOR_TILE_BORDER, COLOR_INPUT_BG)
        canvas.draw_text('3', (v_centre + (2 * s), w_centre), 40, 'Black', 'monospace')

    if isTile4LockOn is True:
        canvas.draw_polygon([[v, w + s], [v, w + (2 * s)], [v + s, w + (2 * s)], [v + s, w + s]], 2, COLOR_TILE_BORDER,
                            COLOR_INPUT_BG)
        canvas.draw_text('4', (v_centre, w_centre + s), 40, 'Black', 'monospace')

    if isTile5LockOn is True:
        canvas.draw_polygon([[v + s, w + s], [v + s, w + (2 * s)], [v + (2 * s), w + (2 * s)], [v + (2 * s), w + s]], 2,
                            COLOR_TILE_BORDER, COLOR_INPUT_BG)
        canvas.draw_text('5', (v_centre + s, w_centre + s), 40, 'Black', 'monospace')

    if isTile6LockOn is True:
        canvas.draw_polygon(
            [[v + (2 * s), w + s], [v + (2 * s), w + (2 * s)], [v + (3 * s), w + (2 * s)], [v + (3 * s), w + s]], 2,
            COLOR_TILE_BORDER,
            COLOR_INPUT_BG)
        canvas.draw_text('6', (v_centre + (2 * s), w_centre + s), 40, 'Black', 'monospace')

    if isTile7LockOn is True:
        canvas.draw_polygon([[v, w + (2 * s)], [v, w + (3 * s)], [v + s, w + (3 * s)], [v + s, w + (2 * s)]], 2,
                            COLOR_TILE_BORDER, COLOR_INPUT_BG)
        canvas.draw_text('7', (v_centre, w_centre + (2 * s)), 40, 'Black', 'monospace')

    if isTile8LockOn is True:
        canvas.draw_polygon(
            [[v + s, w + (2 * s)], [v + s, w + (3 * s)], [v + (2 * s), w + (3 * s)], [v + (2 * s), w + (2 * s)]], 2,
            COLOR_TILE_BORDER,
            COLOR_INPUT_BG)
        canvas.draw_text('8', (v_centre + s, w_centre + (2 * s)), 40, 'Black', 'monospace')

    if isTile9LockOn is True:
        canvas.draw_polygon([[v + (2 * s), w + (2 * s)], [v + (2 * s), w + (3 * s)], [v + (3 * s), w + (3 * s)],
                             [v + (3 * s), w + (2 * s)]], 2,
                            COLOR_TILE_BORDER, COLOR_BLANK_TILE)

    # Draw instructions for input for both initial and goal state
    if isDrawInstPuzzle is True:
        canvas.draw_text("Key-in the initial state:", (470, 170), 30, 'Black', 'serif')

    if isDrawInstGoal is True:
        canvas.draw_text("Key-in the goal state:", (470, 170), 30, 'Black', 'serif')
        if len(goalState) is 9:
            isDrawInstGoal = False

    # Drawing puzzle tiles
    x_centre = ((x + x + s) / 2) - 10
    y_centre = ((y + y + s) / 2) + 15

    draw_tile_counter = 1

    for tile_puzzle in initState:
        x_puzzle = x_centre
        y_puzzle = y_centre

        if draw_tile_counter is 2:
            x_puzzle = x_centre + s
        elif draw_tile_counter is 3:
            x_puzzle = x_centre + (2 * s)
        elif draw_tile_counter is 4:
            y_puzzle = y_centre + s
        elif draw_tile_counter is 5:
            x_puzzle = x_centre + s
            y_puzzle = y_centre + s
        elif draw_tile_counter is 6:
            x_puzzle = x_centre + (2 * s)
            y_puzzle = y_centre + s
        elif draw_tile_counter is 7:
            y_puzzle = y_centre + (2 * s)
        elif draw_tile_counter is 8:
            x_puzzle = x_centre + s
            y_puzzle = y_centre + (2 * s)
        elif draw_tile_counter is 9:
            x_puzzle = x_centre + (2 * s)
            y_puzzle = y_centre + (2 * s)
        if tile_puzzle is not '0':
            canvas.draw_text(tile_puzzle, (x_puzzle, y_puzzle), 40, 'Black', 'monospace')

        draw_tile_counter += 1

    # Drawing goal tiles
    if isDrawGoalText is True:
        draw_tile_cntr = 1
        n_centre = ((n + n + s) / 2) - 10
        m_centre = ((m + m + s) / 2) + 15

        for tile_goal in goalState:
            x_goal = n_centre
            y_goal = m_centre

            if draw_tile_cntr is 2:
                x_goal = n_centre + s
            elif draw_tile_cntr is 3:
                x_goal = n_centre + (2 * s)
            elif draw_tile_cntr is 4:
                y_goal = m_centre + s
            elif draw_tile_cntr is 5:
                x_goal = n_centre + s
                y_goal = m_centre + s
            elif draw_tile_cntr is 6:
                x_goal = n_centre + (2 * s)
                y_goal = m_centre + s
            elif draw_tile_cntr is 7:
                y_goal = m_centre + (2 * s)
            elif draw_tile_cntr is 8:
                x_goal = n_centre + s
                y_goal = m_centre + (2 * s)
            elif draw_tile_cntr is 9:
                x_goal = n_centre + (2 * s)
                y_goal = m_centre + (2 * s)
            if tile_goal is not '0':
                canvas.draw_text(tile_goal, (x_goal, y_goal), 40, 'Black', 'monospace')

            draw_tile_cntr += 1

    return None

# resets some variables, ready for goal state inputs
def activateDrawGoalText():
    global tile_counter_input, isTile1LockOn, isDrawGoalText, isTile2LockOn, isTile3LockOn, isDrawInstPuzzle, \
            isTile4LockOn, isTile5LockOn, isTile6LockOn, isTile7LockOn, isTile8LockOn, isTile9LockOn, isDrawInstGoal

    tile_counter_input = 0
    isDrawInstPuzzle = False
    isDrawInstGoal = True
    isDrawGoalText = True
    isTile1LockOn = True
    isTile2LockOn = True
    isTile3LockOn = True
    isTile4LockOn = True
    isTile5LockOn = True
    isTile6LockOn = True
    isTile7LockOn = True
    isTile8LockOn = True
    isTile9LockOn = True

# Mouseclick handler for initial and goal state inputs
def mouse_handler_input(pos):
    global tile_counter_input, initState, isTile1LockOn, isTile2LockOn, \
            isTile3LockOn, isTile4LockOn, isTile5LockOn, isTile6LockOn, \
            isTile7LockOn, isTile8LockOn, isTile9LockOn, goalState

    #print "initState:", initState
    if tile_counter_input < 10:

        if isTile1LockOn is True:
            if (pos[0] < (X_POS_INPUT + TILE_WIDE) and pos[0] > X_POS_INPUT) and \
                    (pos[1] < (Y_POS_INPUT + TILE_WIDE) and pos[1] > Y_POS_INPUT):
                if isDrawGoalText is False:
                    initState.append('1')
                else:
                    goalState.append('1')
                tile_counter_input += 1
                isTile1LockOn = False

        if isTile2LockOn is True:
            if (pos[0] < (X_POS_INPUT + (2 * TILE_WIDE)) and pos[0] > (X_POS_INPUT + TILE_WIDE)) and \
                    (pos[1] < (Y_POS_INPUT + TILE_WIDE) and pos[1] > Y_POS_INPUT):
                if isDrawGoalText is False:
                    initState.append('2')
                else:
                    goalState.append('2')
                tile_counter_input += 1
                isTile2LockOn = False

        if isTile3LockOn is True:
            if (pos[0] < (X_POS_INPUT + (3 * TILE_WIDE)) and pos[0] > (X_POS_INPUT + (2 * TILE_WIDE))) and \
                    (pos[1] < (Y_POS_INPUT + TILE_WIDE) and pos[1] > Y_POS_INPUT):
                if isDrawGoalText is False:
                    initState.append('3')
                else:
                    goalState.append('3')
                tile_counter_input += 1
                isTile3LockOn = False

        if isTile4LockOn is True:
            if (pos[0] < (X_POS_INPUT + TILE_WIDE) and pos[0] > X_POS_INPUT) and \
                    (pos[1] < (Y_POS_INPUT + (2 * TILE_WIDE)) and pos[1] > (Y_POS_INPUT + TILE_WIDE)):
                if isDrawGoalText is False:
                    initState.append('4')
                else:
                    goalState.append('4')
                tile_counter_input += 1
                isTile4LockOn = False

        if isTile5LockOn is True:
            if (pos[0] < (X_POS_INPUT + (2 * TILE_WIDE)) and pos[0] > (X_POS_INPUT + TILE_WIDE)) and \
                    (pos[1] < (Y_POS_INPUT + (2 * TILE_WIDE)) and pos[1] > (Y_POS_INPUT + TILE_WIDE)):
                if isDrawGoalText is False:
                    initState.append('5')
                else:
                    goalState.append('5')
                tile_counter_input += 1
                isTile5LockOn = False

        if isTile6LockOn is True:
            if (pos[0] < (X_POS_INPUT + (3 * TILE_WIDE)) and pos[0] > (X_POS_INPUT + (2 * TILE_WIDE))) and \
                    (pos[1] < (Y_POS_INPUT + (2 * TILE_WIDE)) and pos[1] > (Y_POS_INPUT + TILE_WIDE)):
                if isDrawGoalText is False:
                    initState.append('6')
                else:
                    goalState.append('6')
                tile_counter_input += 1
                isTile6LockOn = False
                return None

        if isTile7LockOn is True:
            if (pos[0] < (X_POS_INPUT + TILE_WIDE) and pos[0] > X_POS_INPUT) and \
                    (pos[1] < (Y_POS_INPUT + (3 * TILE_WIDE)) and pos[1] > (Y_POS_INPUT + (2 * TILE_WIDE))):
                if isDrawGoalText is False:
                    initState.append('7')
                else:
                    goalState.append('7')
                tile_counter_input += 1
                isTile7LockOn = False

        if isTile8LockOn is True:
            if (pos[0] < (X_POS_INPUT + (2 * TILE_WIDE)) and pos[0] > (X_POS_INPUT + TILE_WIDE)) and \
                    (pos[1] < (Y_POS_INPUT + (3 * TILE_WIDE)) and pos[1] > (Y_POS_INPUT + (2 * TILE_WIDE))):
                if isDrawGoalText is False:
                    initState.append('8')
                else:
                    goalState.append('8')
                tile_counter_input += 1
                isTile8LockOn = False

        if isTile9LockOn is True:
            if (pos[0] < (X_POS_INPUT + (3 * TILE_WIDE)) and pos[0] > (X_POS_INPUT + (2 * TILE_WIDE))) and \
                    (pos[1] < (Y_POS_INPUT + (3 * TILE_WIDE)) and pos[1] > (Y_POS_INPUT + (2 * TILE_WIDE))):
                if isDrawGoalText is False:
                    initState.append('0')
                else:
                    goalState.append('0')
                tile_counter_input += 1
                isTile9LockOn = False

    if tile_counter_input is 10:
        if isDrawGoalText is False:
            activateDrawGoalText()


def button_find_solution():
    open = [initState]
    closed = []

    while


frame = simplegui.create_frame("8 Puzzle Solver", WIDTH, HEIGHT)
frame.set_canvas_background('Silver')
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(mouse_handler_input)

button1 = frame.add_button('Find Solution', button_find_solution)

frame.start()