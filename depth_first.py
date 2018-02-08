from maze import Maze


def _print(stack):
    b = stack.copy()
    for i in b:
        cur = b.pop()
        cur.tostring()


def _visit(stack, mp, mz):
    b = stack.copy()
    for i in b:
        cur = b.pop()
        mp.visit(cur.x, cur.y, mz.win, "yellow")
    mz.win.getMouse()


def check_neighbours(b, mp, explored):
    neighbours = []
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
            if z == 0 and top and mp.mapping[i][j - 1] and not mp.mapping[i][j - 1].walls[3] \
                    and mp.mapping[i][j - 1] not in explored:
                    neighbours.append(mp.mapping[i][j - 1])
            if z == 1 and left and mp.mapping[i - 1][j] and not mp.mapping[i - 1][j].walls[2] \
                    and mp.mapping[i - 1][j] not in explored:
                    neighbours.append(mp.mapping[i - 1][j])
            if z == 2 and right and mp.mapping[i + 1][j] and not mp.mapping[i + 1][j].walls[1] \
                    and mp.mapping[i + 1][j] not in explored:
                    neighbours.append(mp.mapping[i + 1][j])
            if z == 3 and bot and not mp.mapping[i][j + 1].walls[0] and mp.mapping[i][j + 1] not in explored:
                    neighbours.append(mp.mapping[i][j + 1])
    return neighbours


def main():
    row = col = 40
    mz = Maze(row, col)
    mp = mz.m
    x = 0
    y = 0
    current = mp.mapping[x][y]
    stack = []
    mp.visit(0, 0, mz.win, "red")
    goal = mp.mapping[row - 1][col - 1]
    explored = []
    stack.append(current)
    while stack:
        current = stack.pop()
        mp.visit(current.x, current.y, mz.win, "yellow")
        if current not in explored:
            explored.append(current)
            if len(check_neighbours(current, mp, explored)) > 0:
                neighbours = check_neighbours(current, mp, explored)
                for z in range(0, len(neighbours)):
                    stack.append(neighbours[z])
            if current.x == goal.x and current.y == goal.y:
                _visit(explored, mp, mz)


main()

