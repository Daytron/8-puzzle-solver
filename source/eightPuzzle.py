try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from classes import *

#### Constants ####
# Canvas size
WIDTH = 700
HEIGHT = 620

# Starting coordinates for initial state, goal state and input key
X_POS_PUZZLE = 50
Y_POS_PUZZLE = 80
X_POS_INPUT = 400
Y_POS_INPUT = 200
X_POS_GOAL = 50
Y_POS_GOAL = 370

# Tile size (side)
TILE_WIDE = 70

# Default colors
CANVAS_BG = 'LightSkyBlue'
COLOR_INPUT_BG = 'White'
COLOR_PUZZLE_BG = 'White'
COLOR_TILE_BORDER = 'Black'


#### Global variables ####
# Tile counter
tile_counter_input = 1

# Pattern lists for initial and goal states
initState = []
goalState = []

# Master list of all class State objects created
master_states = []

# Var for A star algorithm
openStates = []

# Explored path list (objects)
explored_states = []

# Solution/Moves to reach goal (objects)
solution_path = []

# List of tiles (integers), use for displaying tiles in the canvas
puzzle_state = []

# Flag counter for timer handler
timer_counter = 0

# Number of moves for the solution path for the puzzle
num_moves = 0

# Boolean status variables
isDrawGoalText = False
isInputPuzzleInstructionOn = True
isInputGoalInstructionOn = False
isTile1LockOn = True
isTile2LockOn = True
isTile3LockOn = True
isTile4LockOn = True
isTile5LockOn = True
isTile6LockOn = True
isTile7LockOn = True
isTile8LockOn = True
isTile9LockOn = True
isButtonFindSolutionOn = False
isButtonShowSolutionOn = False

def draw(canvas):
    """
    :description: Draw handler for the frame canvas
    :param canvas: Frame's canvas
    :return: None
    """
    global isInputGoalInstructionOn
    # Positions for puzzle tiles
    x = X_POS_PUZZLE
    y = Y_POS_PUZZLE

    # Square size
    s = TILE_WIDE

    # Draw Title logo
    # canvas.draw_image(image, center_source, width_height_source, center_dest, width_height_dest, rotation)
    # Draw an image that was previously loaded. center_source is a pair of coordinates
    # giving the position of the center of the image,
    # while center_dest is a pair of screen coordinates specifying where the center of the image should be drawn
    # on the canvas.
    # width_height_source is a pair of integers giving the size of the original image,
    # while width_height_dest is a pair of integers giving the size of how the images should be drawn.
    # The image can be rotated clockwise by rotation radians.
    #
    # You can draw the whole image file or just part of it.
    # The source information (center_source and width_height_source) specifies which pixels to display.
    # If it attempts to use any pixels outside of the actual file size, then no image will be drawn.
    # Specifying a different width or height in the destination than in the source will rescale the image.
    canvas.draw_image(image_logo, (298 / 2, 60 / 2), (298, 60), (520, 50), (298, 60))

    # Draw puzzle text
    canvas.draw_text('Initial State', (50, 70), 25, 'Black', 'sans-serif')

    # Draw puzzle tiles
    canvas.draw_polygon([[x, y], [x, y + s], [x + s, y + s], [x + s, y]], 2, COLOR_TILE_BORDER, COLOR_PUZZLE_BG)
    canvas.draw_polygon([[x + s, y], [x + s, y + s], [x + (2 * s), y + s], [x + (2 * s), y]], 2, COLOR_TILE_BORDER,
                        COLOR_PUZZLE_BG)
    canvas.draw_polygon([[x + (2 * s), y], [x + (2 * s), y + s], [x + (3 * s), y + s], [x + (3 * s), y]], 2,
                        COLOR_TILE_BORDER,
                        COLOR_PUZZLE_BG)

    canvas.draw_polygon([[x, y + s], [x, y + (2 * s)], [x + s, y + (2 * s)], [x + s, y + s]], 2, COLOR_TILE_BORDER,
                        COLOR_PUZZLE_BG)
    canvas.draw_polygon([[x + s, y + s], [x + s, y + (2 * s)], [x + (2 * s), y + (2 * s)], [x + (2 * s), y + s]], 2,
                        COLOR_TILE_BORDER, COLOR_PUZZLE_BG)
    canvas.draw_polygon(
        [[x + (2 * s), y + s], [x + (2 * s), y + (2 * s)], [x + (3 * s), y + (2 * s)], [x + (3 * s), y + s]], 2,
        COLOR_TILE_BORDER,
        COLOR_PUZZLE_BG)

    canvas.draw_polygon([[x, y + (2 * s)], [x, y + (3 * s)], [x + s, y + (3 * s)], [x + s, y + (2 * s)]], 2,
                        COLOR_TILE_BORDER,
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
    canvas.draw_text('Goal State', (50, 360), 25, 'Black', 'sans-serif')

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
        canvas.draw_polygon([[v + (2 * s), w + s], [v + (2 * s), w + (2 * s)], [v + (3 * s), w + (2 * s)],
            [v + (3 * s), w + s]], 2, COLOR_TILE_BORDER, COLOR_INPUT_BG)
        canvas.draw_text('6', (v_centre + (2 * s), w_centre + s), 40, 'Black', 'monospace')

    if isTile7LockOn is True:
        canvas.draw_polygon([[v, w + (2 * s)], [v, w + (3 * s)], [v + s, w + (3 * s)], [v + s, w + (2 * s)]], 2,
                            COLOR_TILE_BORDER, COLOR_INPUT_BG)
        canvas.draw_text('7', (v_centre, w_centre + (2 * s)), 40, 'Black', 'monospace')

    if isTile8LockOn is True:
        canvas.draw_polygon([[v + s, w + (2 * s)], [v + s, w + (3 * s)], [v + (2 * s), w + (3 * s)], [v + (2 * s),
            w + (2 * s)]], 2, COLOR_TILE_BORDER, COLOR_INPUT_BG)
        canvas.draw_text('8', (v_centre + s, w_centre + (2 * s)), 40, 'Black', 'monospace')

    if isTile9LockOn is True:
        canvas.draw_polygon([[v + (2 * s), w + (2 * s)], [v + (2 * s), w + (3 * s)], [v + (3 * s), w + (3 * s)],
                             [v + (3 * s), w + (2 * s)]], 2, COLOR_TILE_BORDER, COLOR_INPUT_BG)

    # Draw instructions for input for both initial and goal state
    if isInputPuzzleInstructionOn is True:
        canvas.draw_text("Key-in the initial state:", (X_POS_INPUT - 7, 185), 25, 'Black', 'serif')

    if isInputGoalInstructionOn is True:
        canvas.draw_text("Key-in the goal state:", (X_POS_INPUT - 7, 185), 25, 'Black', 'serif')
        if len(goalState) is 9:
            isInputGoalInstructionOn = False

    # Drawing puzzle tiles
    x_centre = ((x + x + s) / 2) - 10
    y_centre = ((y + y + s) / 2) + 15

    draw_tile_counter = 1

    for tile_init in initState:
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
        if tile_init is not 0:
            canvas.draw_text(str(tile_init), (x_puzzle, y_puzzle), 40, 'Black', 'monospace')

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
            if tile_goal is not 0:
                canvas.draw_text(str(tile_goal), (x_goal, y_goal), 40, 'Black', 'monospace')
            draw_tile_cntr += 1


    if isButtonShowSolutionOn is True and isButtonFindSolutionOn is False:
        tile_counter = 1

        canvas.draw_text('Solution:', (X_POS_INPUT, 185), 25, 'Black','sans-serif')

        canvas.draw_polygon([[v, w], [v, w + s], [v + s, w + s], [v + s, w]], 2, COLOR_TILE_BORDER, COLOR_INPUT_BG)
        canvas.draw_polygon([[v + s, w], [v + s, w + s], [v + (2 * s), w + s], [v + (2 * s), w]], 2, COLOR_TILE_BORDER,
                            COLOR_INPUT_BG)
        canvas.draw_polygon([[v + (2 * s), w], [v + (2 * s), w + s], [v + (3 * s), w + s], [v + (3 * s), w]], 2,
                            COLOR_TILE_BORDER, COLOR_INPUT_BG)
        canvas.draw_polygon([[v, w + s], [v, w + (2 * s)], [v + s, w + (2 * s)], [v + s, w + s]], 2, COLOR_TILE_BORDER,
                            COLOR_INPUT_BG)
        canvas.draw_polygon([[v + s, w + s], [v + s, w + (2 * s)], [v + (2 * s), w + (2 * s)], [v + (2 * s), w + s]], 2,
                            COLOR_TILE_BORDER, COLOR_INPUT_BG)
        canvas.draw_polygon([[v + (2 * s), w + s], [v + (2 * s), w + (2 * s)], [v + (3 * s), w + (2 * s)],
            [v + (3 * s), w + s]], 2, COLOR_TILE_BORDER, COLOR_INPUT_BG)

        canvas.draw_polygon([[v, w + (2 * s)], [v, w + (3 * s)], [v + s, w + (3 * s)], [v + s, w + (2 * s)]], 2,
                            COLOR_TILE_BORDER, COLOR_INPUT_BG)
        canvas.draw_polygon([[v + s, w + (2 * s)], [v + s, w + (3 * s)], [v + (2 * s), w + (3 * s)], [v + (2 * s),
            w + (2 * s)]], 2, COLOR_TILE_BORDER, COLOR_INPUT_BG)
        canvas.draw_polygon([[v + (2 * s), w + (2 * s)], [v + (2 * s), w + (3 * s)], [v + (3 * s), w + (3 * s)],
                             [v + (3 * s), w + (2 * s)]], 2, COLOR_TILE_BORDER, COLOR_INPUT_BG)


        canvas.draw_text("Solution found.",(X_POS_INPUT-90,460),23,'DarkRed','sans-serif')
        canvas.draw_text("* The goal state can be reached in "+str(num_moves)+" moves.",
            (X_POS_INPUT-90,490),20,'Black','sans-serif')
        canvas.draw_text("* There are "+str(len(explored_states))+" states explored.",
            (X_POS_INPUT-90,515),20,'Black','sans-serif')
        canvas.draw_text("* Click 'Show solution' button",
            (X_POS_INPUT-90, 540),20,'Black','sans-serif')
        for tile_soln in puzzle_state:
            v_soln = v_centre
            w_soln = w_centre

            if tile_counter is 2:
                v_soln = v_centre + s
            elif tile_counter is 3:
                v_soln = v_centre + (2 * s)
            elif tile_counter is 4:
                w_soln = w_centre + s
            elif tile_counter is 5:
                v_soln = v_centre + s
                w_soln = w_centre + s
            elif tile_counter is 6:
                v_soln = v_centre + (2 * s)
                w_soln = w_centre + s
            elif tile_counter is 7:
                w_soln = w_centre + (2 * s)
            elif tile_counter is 8:
                v_soln = v_centre + s
                w_soln = w_centre + (2 * s)
            elif tile_counter is 9:
                v_soln = v_centre + (2 * s)
                w_soln = w_centre + (2 * s)
            if tile_soln is not 0:
                canvas.draw_text(str(tile_soln), (v_soln, w_soln), 40, 'Black', 'monospace')
            tile_counter += 1

    return None


def initiate_draw_goal_state():
    """
    :description: Resets variables, ready for goal state input
    :return: None
    """
    global tile_counter_input, isTile1LockOn, isDrawGoalText, isTile2LockOn, isTile3LockOn, isInputPuzzleInstructionOn, \
        isTile4LockOn, isTile5LockOn, isTile6LockOn, isTile7LockOn, isTile8LockOn, isTile9LockOn, \
        isInputGoalInstructionOn, isButtonFindSolutionOn

    tile_counter_input = 0
    isInputPuzzleInstructionOn = False
    isInputGoalInstructionOn = True
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

    isButtonFindSolutionOn = True

def mouse_handler_input(pos):
    """
    :description: Mouse click handler for initial and goal state inputs
    :param pos: Mouse click position [x,y]
    :return: None
    """
    global tile_counter_input, initState, isTile1LockOn, isTile2LockOn, \
        isTile3LockOn, isTile4LockOn, isTile5LockOn, isTile6LockOn, \
        isTile7LockOn, isTile8LockOn, isTile9LockOn, goalState, puzzle_state

    #print "initState:", initState
    if tile_counter_input < 10:

        if isTile1LockOn is True:
            if (pos[0] < (X_POS_INPUT + TILE_WIDE) and pos[0] > X_POS_INPUT) and \
                    (pos[1] < (Y_POS_INPUT + TILE_WIDE) and pos[1] > Y_POS_INPUT):
                if isDrawGoalText is False:
                    initState.append(1)
                else:
                    goalState.append(1)
                tile_counter_input += 1
                isTile1LockOn = False

        if isTile2LockOn is True:
            if (pos[0] < (X_POS_INPUT + (2 * TILE_WIDE)) and pos[0] > (X_POS_INPUT + TILE_WIDE)) and \
                    (pos[1] < (Y_POS_INPUT + TILE_WIDE) and pos[1] > Y_POS_INPUT):
                if isDrawGoalText is False:
                    initState.append(2)
                else:
                    goalState.append(2)
                tile_counter_input += 1
                isTile2LockOn = False

        if isTile3LockOn is True:
            if (pos[0] < (X_POS_INPUT + (3 * TILE_WIDE)) and pos[0] > (X_POS_INPUT + (2 * TILE_WIDE))) and \
                    (pos[1] < (Y_POS_INPUT + TILE_WIDE) and pos[1] > Y_POS_INPUT):
                if isDrawGoalText is False:
                    initState.append(3)
                else:
                    goalState.append(3)
                tile_counter_input += 1
                isTile3LockOn = False

        if isTile4LockOn is True:
            if (pos[0] < (X_POS_INPUT + TILE_WIDE) and pos[0] > X_POS_INPUT) and \
                    (pos[1] < (Y_POS_INPUT + (2 * TILE_WIDE)) and pos[1] > (Y_POS_INPUT + TILE_WIDE)):
                if isDrawGoalText is False:
                    initState.append(4)
                else:
                    goalState.append(4)
                tile_counter_input += 1
                isTile4LockOn = False

        if isTile5LockOn is True:
            if (pos[0] < (X_POS_INPUT + (2 * TILE_WIDE)) and pos[0] > (X_POS_INPUT + TILE_WIDE)) and \
                    (pos[1] < (Y_POS_INPUT + (2 * TILE_WIDE)) and pos[1] > (Y_POS_INPUT + TILE_WIDE)):
                if isDrawGoalText is False:
                    initState.append(5)
                else:
                    goalState.append(5)
                tile_counter_input += 1
                isTile5LockOn = False

        if isTile6LockOn is True:
            if (pos[0] < (X_POS_INPUT + (3 * TILE_WIDE)) and pos[0] > (X_POS_INPUT + (2 * TILE_WIDE))) and \
                    (pos[1] < (Y_POS_INPUT + (2 * TILE_WIDE)) and pos[1] > (Y_POS_INPUT + TILE_WIDE)):
                if isDrawGoalText is False:
                    initState.append(6)
                else:
                    goalState.append(6)
                tile_counter_input += 1
                isTile6LockOn = False
                return None

        if isTile7LockOn is True:
            if (pos[0] < (X_POS_INPUT + TILE_WIDE) and pos[0] > X_POS_INPUT) and \
                    (pos[1] < (Y_POS_INPUT + (3 * TILE_WIDE)) and pos[1] > (Y_POS_INPUT + (2 * TILE_WIDE))):
                if isDrawGoalText is False:
                    initState.append(7)
                else:
                    goalState.append(7)
                tile_counter_input += 1
                isTile7LockOn = False

        if isTile8LockOn is True:
            if (pos[0] < (X_POS_INPUT + (2 * TILE_WIDE)) and pos[0] > (X_POS_INPUT + TILE_WIDE)) and \
                    (pos[1] < (Y_POS_INPUT + (3 * TILE_WIDE)) and pos[1] > (Y_POS_INPUT + (2 * TILE_WIDE))):
                if isDrawGoalText is False:
                    initState.append(8)
                else:
                    goalState.append(8)
                tile_counter_input += 1
                isTile8LockOn = False

        if isTile9LockOn is True:
            if (pos[0] < (X_POS_INPUT + (3 * TILE_WIDE)) and pos[0] > (X_POS_INPUT + (2 * TILE_WIDE))) and \
                    (pos[1] < (Y_POS_INPUT + (3 * TILE_WIDE)) and pos[1] > (Y_POS_INPUT + (2 * TILE_WIDE))):
                if isDrawGoalText is False:
                    initState.append(0)
                else:
                    goalState.append(0)
                tile_counter_input += 1
                isTile9LockOn = False



    if tile_counter_input is 10:
        if isDrawGoalText is False:
            initiate_draw_goal_state()


def button_find_solution():
    """
    :description: Starts searching for solution using A star algorithm
        note: all openStates and closedStates lists hold OBJECTS not lists of tiles
    :return: None
    """
    global master_states, isItInitialGN, openStates, explored_states, isButtonFindSolutionOn, isButtonShowSolutionOn, \
        puzzle_state

    if isButtonFindSolutionOn is True:
        # print goalState
        # create object for initial state and save to master states list
        master_states.append(State(initState, initState, goalState, 0))
        openStates.append(master_states[0])
        closedStates = []

        while openStates:
            x = openStates[0]
            openStates.pop(0)

            # Checks if the goal state is found
            if x.node == goalState:
                for state in closedStates:
                    explored_states.append(state)
                explored_states.append(x)

                find_path()
                display_solution()

                isButtonFindSolutionOn = False
                isButtonShowSolutionOn = True
                puzzle_state = list(initState)
                return None

            # Otherwise keep looking by expanding more states
            else:
                x.generate_children(master_states)

                for child in x.children:
                    master_states.append(State(child, initState, goalState, (x.gn + 1)))
                    if not (master_states[-1] in openStates or master_states[-1] in closedStates):
                        openStates.append(master_states[-1])
                closedStates.append(x)
                # print openStates
                reorder_heuristics()
        else:
            print "Failed to find a solution"


def reorder_heuristics():
    """
    :description: Re-arrange the objects generated stored in openStates variable
        according to their f(n) values from lowest to highest
    :return: None
    """
    global openStates

    temp_list = list(openStates)
    del openStates[:]
    lowest = temp_list[0].fn
    low_obj = temp_list[0]
    counter = 0

    while len(temp_list) > 0:
        if temp_list[counter].fn < lowest:
            lowest = temp_list[counter].fn
            low_obj = temp_list[counter]
        counter += 1
        if counter == len(temp_list):
            openStates.append(low_obj)
            #print low_obj
            #print temp_list
            temp_list.remove(low_obj)
            if temp_list:
                lowest = temp_list[0].fn
                low_obj = temp_list[0]
            counter = 0


def find_path():
    """
    :description: Filters explored path found to find the optimise path.
    :return: None
    """
    global solution_path
    rev_solution = []
    skip_state = []
    next_index_elem = 0
    rev_states = explored_states[::-1]
    #for o in rev_states:
        #print o.node
    for i, node in enumerate(rev_states):
        if not (i in skip_state):
            #print "i:", i
            if i < (len(rev_states)-1):
                if node.node in rev_states[i+1].children:
                    rev_solution.append(node.node)
                else:
                    skip_state.append(i+1)
                    next_index_elem = i + 2
                    while True:
                        if next_index_elem < len(rev_states):
                            if node.node in rev_states[next_index_elem].children:
                                rev_solution.append(node.node)
                                break
                            else:
                                skip_state.append(next_index_elem)
                                next_index_elem += 1
                        else:
                            break
            else:
                rev_solution.append(node.node)
    solution_path = rev_solution[::-1]
    #print solution_path
    #print skip_state


def display_solution():
    """
    :description: Formats and displays solution output into the console
    :return: None
    """
    global num_moves
    i = 0
    num_moves = len(solution_path) - 1
    print "The goal can be reached in " + str(num_moves) + " moves."
    for node in solution_path:
        if i == 0:
            print "Initial state:"
        else:
            print "Move", i
        print node[0], node[1], node[2]
        print node[3], node[4], node[5]
        print node[6], node[7], node[8]
        print ""
        i += 1


def timer_handler():
    """
    :description: Sets the the solution animation using timer
    :return: None
    """
    global timer_counter, puzzle_state

    timer_counter += 1
    if timer_counter < len(solution_path):
        puzzle_state = solution_path[timer_counter]
    else:

        timer_counter = 0
        timer.stop()


def button_show_solution():
    """
    :description: Button function for initialising solution path display view in the canvas
    :return: None
    """
    global puzzle_state

    if isButtonShowSolutionOn is True:
        puzzle_state = list(initState)
        timer.start()

def button_quit_application():
    """
    :description: Button function to quit program
    :return: None
    """
    if timer.is_running() is True:
        timer.stop()
    frame.stop()

image_logo = simplegui.load_image('file:///X:/GIT_ROOT/8-puzzle-solver/logo.png')

# Frame initialisation
frame = simplegui.create_frame("8 Puzzle Solver", WIDTH, HEIGHT)

# Frame settings and control handlers initialisation
frame.set_canvas_background(CANVAS_BG)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(mouse_handler_input)
label1 = frame.add_label('8 Puzzle Solver')
blankSpace1 = frame.add_label('')
label2 = frame.add_label('Instruction:')
label3 =  frame.add_label('1. Enter initial and goal states')
label4 = frame.add_label('  by clicking one tile at a time')
label5 = frame.add_label(' on keypad on the right')
label6 = frame.add_label('2. Click Find Solution button')
label7 = frame.add_label('3. Click Show solution button')

blankSpace2 = frame.add_label('')
button1 = frame.add_button('Find Solution', button_find_solution, 120)
blankSpace3 = frame.add_label('')
button2 = frame.add_button('Show Solution', button_show_solution, 120)

blankSpace4 = frame.add_label('')
blankSpace5 = frame.add_label('')
blankSpace6 = frame.add_label('')
blankSpace7 = frame.add_label('')
button3 =  frame.add_button('Quit', button_quit_application, 120)


# Timer initialisation
timer = simplegui.create_timer(500, timer_handler)

# Frame call/Program starts here
frame.start()