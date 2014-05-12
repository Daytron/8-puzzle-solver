import math

class State:
    def __init__(self,node,start,goal,gn):
        self.start = start
        self.goal = goal
        self.node = node
        self.gn = gn
        self.hn = self.evaluate_heuristic()
        self.index = 0

        self.children = []
        self.temp = []
        self.fn = self.gn + self.hn

    def generate_children(self,master_list):
        # n is the element position
        # t is the element value
        for n, t in enumerate(self.node):
            if t == 0:
                if n == 0:
                    a = self.node[1]
                    b = self.node[3]
                    self.generate_child(1,0,a,master_list)
                    self.generate_child(3,0,b,master_list)
                    break

                if n == 1:
                    a = self.node[0]
                    b = self.node[2]
                    c = self.node[4]
                    self.generate_child(0,1,a,master_list)
                    self.generate_child(2,1,b,master_list)
                    self.generate_child(4,1,c,master_list)
                    break

                if n == 2:
                    a = self.node[1]
                    b = self.node[5]
                    self.generate_child(1,2,a,master_list)
                    self.generate_child(5,2,b,master_list)
                    break

                if n == 3:
                    a = self.node[0]
                    b = self.node[4]
                    c = self.node[6]
                    self.generate_child(0,3,a,master_list)
                    self.generate_child(4,3,b,master_list)
                    self.generate_child(6,3,c,master_list)
                    break

                if n == 4:
                    a = self.node[1]
                    b = self.node[3]
                    c = self.node[5]
                    d = self.node[7]
                    self.generate_child(1,4,a,master_list)
                    self.generate_child(3,4,b,master_list)
                    self.generate_child(5,4,c,master_list)
                    self.generate_child(7,4,d,master_list)
                    break

                if n == 5:
                    a = self.node[2]
                    b = self.node[4]
                    c = self.node[8]
                    self.generate_child(2,5,a,master_list)
                    self.generate_child(4,5,b,master_list)
                    self.generate_child(8,5,c,master_list)
                    break

                if n == 6:
                    a = self.node[3]
                    b = self.node[7]
                    self.generate_child(3,6,a,master_list)
                    self.generate_child(7,6,b,master_list)
                    break

                if n == 7:
                    a = self.node[6]
                    b = self.node[4]
                    c = self.node[8]
                    self.generate_child(6,7,a,master_list)
                    self.generate_child(4,7,b,master_list)
                    self.generate_child(8,7,c,master_list)
                    break

                if n == 8:
                    a = self.node[5]
                    b = self.node[7]
                    self.generate_child(5,8,a,master_list)
                    self.generate_child(7,8,b,master_list)
                    break


    # Returns object list, later to be used to append to master_list
    def get_tiles(self):
        return self.node

    # Checks if the generated child is already in previous generated states (master_list)
    # If not, add it to self.children
    def generate_child(self,a,b, val, states_list):
        del self.temp
        self.temp = list(self.node)
        self.temp[a] = 0
        self.temp[b] = val
        list_pattern_states = []

        # state_list is a list of objects not list of patterns
        # change list of objects to list of patterns
        for state in states_list:
            list_pattern_states.append(state.node)

        if not self.temp in list_pattern_states:
            self.children.append(self.temp)

    def evaluate_gn(self):
        pass

    def evaluate_heuristic(self):
        misplacedTile = 0
        sumDist=0

        for i in range(9):
            if self.node[i]!=self.goal[i]:
                misplacedTile +=1
        for i in self.node:
            sumDist +=math.fabs(self.node.index(i)-self.goal.index(i))

        totalDist = sumDist + misplacedTile

        return totalDist



