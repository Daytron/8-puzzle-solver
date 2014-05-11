class State:
    def __init__(self,start_tile):
        self.tiles = start_tile
        self.index = 0
        self.children = []
        self.temp = []

    def generate_children(self,master_list):
        # n is the element position
        # t is the element value
        for n, t in enumerate(self.tiles):
            if t == 0:
                if n == 0:
                    a = self.tiles[1]
                    b = self.tiles[3]
                    self.generate_child(1,0,a,master_list)
                    self.generate_child(3,0,b,master_list)
                    break

                if n == 1:
                    a = self.tiles[0]
                    b = self.tiles[2]
                    c = self.tiles[4]
                    self.generate_child(0,1,a,master_list)
                    self.generate_child(2,1,b,master_list)
                    self.generate_child(4,1,c,master_list)
                    break

                if n == 2:
                    a = self.tiles[1]
                    b = self.tiles[5]
                    self.generate_child(1,2,a,master_list)
                    self.generate_child(5,2,b,master_list)
                    break

                if n == 3:
                    a = self.tiles[0]
                    b = self.tiles[4]
                    c = self.tiles[6]
                    self.generate_child(0,3,a,master_list)
                    self.generate_child(4,3,b,master_list)
                    self.generate_child(6,3,c,master_list)
                    break

                if n == 4:
                    a = self.tiles[1]
                    b = self.tiles[3]
                    c = self.tiles[5]
                    d = self.tiles[7]
                    self.generate_child(1,4,a,master_list)
                    self.generate_child(3,4,b,master_list)
                    self.generate_child(5,4,c,master_list)
                    self.generate_child(7,4,d,master_list)
                    break

                if n == 5:
                    a = self.tiles[2]
                    b = self.tiles[4]
                    c = self.tiles[8]
                    self.generate_child(2,5,a,master_list)
                    self.generate_child(4,5,b,master_list)
                    self.generate_child(8,5,c,master_list)
                    break

                if n == 6:
                    a = self.tiles[3]
                    b = self.tiles[7]
                    self.generate_child(3,6,a,master_list)
                    self.generate_child(7,6,b,master_list)
                    break

                if n == 7:
                    a = self.tiles[6]
                    b = self.tiles[4]
                    c = self.tiles[8]
                    self.generate_child(6,7,a,master_list)
                    self.generate_child(4,7,b,master_list)
                    self.generate_child(8,7,c,master_list)
                    break

                if n == 8:
                    a = self.tiles[5]
                    b = self.tiles[7]
                    self.generate_child(5,8,a,master_list)
                    self.generate_child(7,8,b,master_list)
                    break


    # Returns object list, later to be used to append to master_list
    def get_tiles(self):
        return self.tiles

    # Checks if the generated child is already in previous generated states (master_list)
    # If not, add it to self.children
    def generate_child(self,a,b, val, states_list):
        del self.temp
        self.temp = list(self.tiles)
        self.temp[a] = 0
        self.temp[b] = val

        if not self.temp in states_list:
            self.children.append(self.temp)

