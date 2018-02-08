from maze import Maze
from maze import Map


class DepthLimited(Maze):

    def __init__(self, x, y):
        Maze.__init__(self, x, y)
        self._map = self.m

    def create_node(self, x, y):
        self._map.visit(x, y, self.win, "blue")

    def check_neighbours(self, b):
        neighbours = []
        mp = self._map
        i = b.x
        j = b.y
        left = False
        right = False
        top = False
        bot = False
        if i + 1 < 40:
            right = True
        if i - 1 > 0:
            left = True
        if j + 1 < 40:
            bot = True
        if j - 1 > 0:
            top = True
        for z in range(0, 4):
            if not b.walls[z]:
                if z == 0 and top and mp.mapping[i][j - 1] and (mp.mapping[i][j - 1] not in DepthLimited.visited) and not \
                        mp.mapping[i][j - 1].walls[3]:
                        neighbours.append(mp.mapping[i][j - 1])
                if z == 1 and left and mp.mapping[i - 1][j] and (mp.mapping[i - 1][j] not in DepthLimited.visited) and not \
                        mp.mapping[i - 1][j].walls[2]:
                        neighbours.append(mp.mapping[i - 1][j])
                if z == 2 and right and mp.mapping[i + 1][j] and (mp.mapping[i + 1][j] not in DepthLimited.visited) and not \
                        mp.mapping[i + 1][j].walls[1]:
                        neighbours.append(mp.mapping[i + 1][j])
                if z == 3 and bot and mp.mapping[i][j + 1] and (mp.mapping[i][j + 1] not in DepthLimited.visited) and not \
                        mp.mapping[i][j + 1].walls[0]:
                        neighbours.append(mp.mapping[i][j + 1])

        return neighbours

    def DIS(self, root, depth):
        s = self.DFS(root, depth, root)
        print("here")

    stack = []
    visited = {}
    solution = []
    solution_found = False

    def DFS(self, current, count):
        if count > 500:
            DepthLimited.solution_found = True
            return
        if DepthLimited.solution_found:
            self._map.visit(current.x, current.y, self.win, "yellow")
            return
        DepthLimited.stack.append(current)
        goal = self._map.mapping[self._map.row - 5][self._map.col - 5]
        if current.x == goal.x and current.y == goal.y:
            self._map.visit(current.x, current.y, self.win, "yellow")
            return
        DepthLimited.visited[count] = current
        neighbours = self.check_neighbours(current)
        for z in range(0, len(neighbours)):
            self.DFS(neighbours[z], count + 1)

'''
     def DFLS(self, node, depth, parent):
        current = node
        print("visiting: x: ", current.x, " y: ", current.y)
        DepthLimited.stack.append(current)
        goal = self._map.mapping[self._map.row - 1][self._map.col - 1]
        if node.x == goal.x and node.y == goal.y:
            return node
        if depth == 0:
            return False
        else:
            cut_off_occurred = False
            neighbours = self.check_neighbours(current, parent)
            for z in range(0, len(neighbours)):
                print("-----------> child: x: ", neighbours[z].x, " y: ", neighbours[z].y)
                s = self.DFS(neighbours[z], depth - 1, current)
                if not s:
                    cut_off_occurred = True  # CutOff occurred on path so cut down root to path somehow
                elif s:
                    return node
        if cut_off_occurred:
            return False
        else:
            return False
'''

def _visit(stack, mp, win):
    b = stack.copy()
    for i in b:
        cur = b.pop()
        mp.visit(cur.x, cur.y, win, "yellow")
    win.getMouse()


def main():
    d = DepthLimited(20, 20)
    d.DFS(d.m.mapping[0][0], 0)

main()
