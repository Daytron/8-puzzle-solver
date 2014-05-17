## 8 Puzzle Solver ##

### Description ###
An 8 puzzle solver Python application utilising A-star algorithm. Goal state can be reached by expanding a given state to its successor or children states, as the application find a match for each generated child. Once the goal is found, the application trace and display the path leading to the initial state. Solution path is shown by animating the tiles as it moves one tile at a time towards the goal state.


### Screenshots ###
Ready to accept input for an initial state
![ScreenShot](https://raw.githubusercontent.com/Daytron/8-puzzle-solver/master/screenshots/enter_init_state.png)
<BR><BR>
Ready to accept input for a goal state
![ScreenShot](https://raw.githubusercontent.com/Daytron/8-puzzle-solver/master/screenshots/enter_goal_state.png)
<BR><BR>
All inputs are all set and ready to commence searching via 'Find Solution' button
![ScreenShot](https://raw.githubusercontent.com/Daytron/8-puzzle-solver/master/screenshots/ready_to_search.png)
<BR><BR>
Output result
![ScreenShot](https://raw.githubusercontent.com/Daytron/8-puzzle-solver/master/screenshots/solution_found.png)

### Requirements ###
- Python 2.7
- [Pygame](http://www.pygame.org)
- [SimpleGUICS2Pygame](https://pypi.python.org/pypi/SimpleGUICS2Pygame)


### Configuration ###
Change image (logo) file path to your own path

	image_logo = simplegui.load_image('file:///C:/8-puzzle-solver/logo.png')

### Usage ###

	python eightPuzzle.py

### Instructions ###
1. Enter the initial and goal states by clicking one tile a time in the keypad found on the right side of the canvas. The direction of each tile input goes from left to right for each row (top to bottom).
2. Once all inputs are in placed, click 'Find Solution' button.
3. Click 'Show Solution' button for the tiles animation of the solution path.

### Contribution Notice ###
No pull request at the moment. Thanks.


### License and Copyright ###
This package is Copyright (c) Ryan Gilera 2014 and is licensed under the MIT license. See [license](https://raw.githubusercontent.com/Daytron/8-puzzle-solver/master/LICENSE) for more information.