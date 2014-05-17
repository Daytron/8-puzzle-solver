import math


class State:
    def __init__(self, node, start, goal, gn):
        """
        :description: The class constructor
        :param node: The pattern or state using list of values (integers)
        :param start: The initial state
        :param goal: The goal state
        :param gn: The g(n) value, cost it takes to reach this state/node from initial state
        """
        self.start = start
        self.goal = goal
        self.node = node
        self.gn = gn
        self.hn = self.evaluate_heuristic()
        self.children = []
        self.temp = []
        self.fn = self.gn + self.hn

    def generate_children(self, master_list):
        """
        :description: Generates children of current object by identifying possible tile moves.
        :param master_list: List of objects generated from main program
        :note:
            n - the element position
            t - the element value
        """
        for n, t in enumerate(self.node):
            if t == 0:
                if n == 0:
                    a = self.node[1]
                    b = self.node[3]
                    self.generate_child(1, 0, a, master_list)
                    self.generate_child(3, 0, b, master_list)
                    break
                elif n == 1:
                    a = self.node[0]
                    b = self.node[2]
                    c = self.node[4]
                    self.generate_child(0, 1, a, master_list)
                    self.generate_child(2, 1, b, master_list)
                    self.generate_child(4, 1, c, master_list)
                    break
                elif n == 2:
                    a = self.node[1]
                    b = self.node[5]
                    self.generate_child(1, 2, a, master_list)
                    self.generate_child(5, 2, b, master_list)
                    break
                elif n == 3:
                    a = self.node[0]
                    b = self.node[4]
                    c = self.node[6]
                    self.generate_child(0, 3, a, master_list)
                    self.generate_child(4, 3, b, master_list)
                    self.generate_child(6, 3, c, master_list)
                    break
                elif n == 4:
                    a = self.node[1]
                    b = self.node[3]
                    c = self.node[5]
                    d = self.node[7]
                    self.generate_child(1, 4, a, master_list)
                    self.generate_child(3, 4, b, master_list)
                    self.generate_child(5, 4, c, master_list)
                    self.generate_child(7, 4, d, master_list)
                    break
                elif n == 5:
                    a = self.node[2]
                    b = self.node[4]
                    c = self.node[8]
                    self.generate_child(2, 5, a, master_list)
                    self.generate_child(4, 5, b, master_list)
                    self.generate_child(8, 5, c, master_list)
                    break
                elif n == 6:
                    a = self.node[3]
                    b = self.node[7]
                    self.generate_child(3, 6, a, master_list)
                    self.generate_child(7, 6, b, master_list)
                    break
                elif n == 7:
                    a = self.node[6]
                    b = self.node[4]
                    c = self.node[8]
                    self.generate_child(6, 7, a, master_list)
                    self.generate_child(4, 7, b, master_list)
                    self.generate_child(8, 7, c, master_list)
                    break
                elif n == 8:
                    a = self.node[5]
                    b = self.node[7]
                    self.generate_child(5, 8, a, master_list)
                    self.generate_child(7, 8, b, master_list)
                    break

    def get_tiles(self):
        """
        :description: Returns object list, later to be used to append to master_list
        :return: self.node
        :rtype: List of integers
        """
        return self.node

    def generate_child(self, a, b, val, states_list):
        """
        :description: Generates a state, a successor of current object, by moving one tile to the blank space
            done by switching 0 (blank) with one tile being moved
        :param a: A tile position where the blank space should be created
        :param b: A tile position where the tile (val) moved into
        :param val: The tile value that is being moved to the tile position (b)
        :param states_list: List of objects generated in the main program. It is used to compare if the child generated
            is already an object in this list. If not, acquire the generated successor as the child of the current
            object. This makes sure that no child will be generated that has the same state as the current object's
            parent has.
        """
        del self.temp
        self.temp = list(self.node)
        self.temp[a] = 0
        self.temp[b] = val
        list_pattern_states = []

        # make a list of states from a list of objects
        for state in states_list:
            list_pattern_states.append(state.node)

        # Compares previous generated states with the new child generated
        if not self.temp in list_pattern_states:
            self.children.append(self.temp)

    def evaluate_heuristic(self):
        """
        :description: Evaluates h(n) value for each state object
        :return: total_dist
        :rtype : int
        """
        misplaced_tile = 0
        sum_dist = 0

        for i in range(9):
            if self.node[i] != self.goal[i]:
                misplaced_tile += 1
        for i in self.node:
            sum_dist += math.fabs(self.node.index(i) - self.goal.index(i))

        total_dist = sum_dist + misplaced_tile
        return total_dist