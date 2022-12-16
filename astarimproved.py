# this main script will be focusing on text based game
import math


class Node:
    def __init__(self, loc, parent=None, type=0):

        # gcost, distance from startnode
        self.gcost = 0
        # distance from end
        self.hcost = 0
        # total
        self.cost = 0

        self.loc = loc
        self.parent = parent

        # 0, normal walkable path, 1, blocks, 2 goals, 3 end, 4 walked path
        self.type = type

    def __repr__(self):
        if self.type == 0:
            return str(self.cost)if self.cost != 0 else ' .'
        elif self.type == 1:
            return ' X'
        elif self.type == 2:
            return ' S'
        elif self.type == 3:
            return ' E'
        elif self.type == 4:
            return ' 0'
        elif self.type == 5:
            return '/'

class Grid:

    def __init__(self, size, startxy, endxy):
        self.size = size
        self.grid = [[Node(loc=(x,y)) for y in range(size[1])] for x in range(size[0])]

        # set start and end node
        self.startxy = startxy
        self.endxy = endxy
        self.startnode = self.grid[self.startxy[0]][self.startxy[1]]
        self.endnode = self.grid[self.endxy[0]][self.endxy[1]]
        self.startnode.type = 2
        self.endnode.type = 3

        # start node costs
        self.startnode.gcost = 0
        self.startnode.hcost = self.distance(startxy, endxy)
        self.startnode.cost = self.distance(startxy, endxy)

        # pool for sorting the node with lowest cost
        self.pool = []

    def draw_text(self):
        for row in self.grid:
            print(row)

    def draw_simple(self):
        print()
        dis = {0:'.', 1:'█', 2:'S', 3:'E', 4:'o', 5:'X'}
        for row in self.grid:
            for node in row:
                print(dis[node.type], end='  ')
            print()

    def get_grid(self) -> list:
        return [[c.type for c in r] for r in self.grid]

    # return distance between two points (tuples)
    @staticmethod
    def distance(p1, p2) -> float:
        return int(round(math.sqrt(sum((px - py) ** 2 for px, py in zip(p1, p2))), 1) * 10)


    # check node - input a loc to reveal all next to it
    def checknode(self, loc:tuple):
        locs = [(1,1), (1,0), (1,-1), (0,1), (0,-1), (-1,1), (-1,0), (-1,-1)]
        parentnode = self.grid[loc[0]][loc[1]]

        for i in locs:
            xy = (loc[0] + i[0], loc[1] + i[1])
            # check if node exists
            if xy[0] < 0 or xy[1] < 0 or xy[0] >= self.size[0] or xy[1] >= self.size[1]:
                continue

            # fetch object
            node = self.grid[xy[0]][xy[1]]

            # found the end node
            if node.type == 3:
                node.parent = parentnode
                return True

            if node.type != 0:
                continue

            # print(node, xy)
            # first time exploring the node
            projectedcost = parentnode.gcost + self.distance(xy, loc) + self.distance(self.endxy, xy)
            if node.cost == 0 or projectedcost < node.cost:
                node.gcost = parentnode.gcost + self.distance(xy, loc)
                node.hcost = self.distance(self.endxy, xy)
                node.cost = projectedcost
                node.parent = parentnode

            # print(node.cost)

            if node not in self.pool:
                self.pool.append(node)

    # solving the board, return a bool of whether its solved, and the next location
    def step_solve(self, nextnode) -> tuple:
        solved = self.checknode(nextnode)
        self.pool.sort(key=lambda x: (x.cost, x.hcost))

        return (solved, self.pool[0])



# script apis
def creategrid(id=0):
    grid = None

    if id == 0:
        grid = Grid(size=(15, 15), startxy=(1, 1), endxy=(13, 13))
    elif id == 1:
        grid = Grid(size=(15, 15), startxy=(1, 1), endxy=(8, 6))
        # declare obstructions
        for i in range(6):
            grid.grid[7][1 + i].type = 1
            grid.grid[0 + i][3].type = 1
    elif id == 2:
        grid = Grid(size=(15, 15), startxy=(1, 1), endxy=(8, 6))
        for i in range(5):
            grid.grid[1][0].type = 1
            grid.grid[2][0].type = 1
            grid.grid[2][0+i].type = 1

    return grid


def quicksolve(grid, display=True, skip=False):
    nextnode = grid.startnode
    solved = False
    while not solved:

        if not skip:
            input()

        solved, nextnode = grid.step_solve(nextnode.loc)

        grid.pool.remove(nextnode)

        if display:
            print('\n\n')
            grid.draw_simple()
            print(solved, nextnode.loc)

        nextnode.type = 4

    return True

def backtrack(grid):
    # solved now backtracking
    backtrack = False
    targetnode = grid.endnode.parent
    while not backtrack:
        targetnode.type = 5
        targetnode = targetnode.parent
        if targetnode == grid.startnode:
            backtrack = True

