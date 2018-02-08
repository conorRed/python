"""
While there are unvisited cells
    If the current cell has any neighbours which have not been visited
     Choose randomaply one of the unvisited neighbours
     Push the current cell to the stack
     Remapove the wall between the current cell and the chosen cell
     Make the chosen cell the current cell and mapark it as visited
    Else if stack is not emappty
     Pop a cell fromap the stack
     Make it the current cell

"""

from graphics import *
from random import randint


class Maze:

    def __init__(self, row, col):
        self.win = GraphWin('Floor', 500, 500)
        self.win.setBackground('grey')
        self.m = Map(row, col, self.win)
        self.draw(self.m, self.win)

    def draw(self, m, win):
        stack = []
        current = m.mapping[0][0]
        stack.append(current)
        while stack:
            current.visited = True
            if m.check_neighbours(current) is not None:
                stack.append(current)
                next_node = m.check_neighbours(current)
                current = next_node
            elif len(stack) > 0:
                current = stack.pop()
        m.delete_walls(m.mapping[0][0])
        m.delete_walls(m.mapping[m.row - 1][m.col - 1])
        m.draw(win)


class Block:

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.visited = False
        self.walls = [True, True, True, True]

    def draw_rec(self, win,  scale_row, scale_col, color):
        x_scale = self.x * scale_row
        y_scale = self.y * scale_col
        rec = Rectangle(Point(x_scale, y_scale), Point(x_scale + self.size, y_scale + self.size))
        rec.setFill(color)
        rec.draw(win)

    def tostring(self):
        print("Block : ", self.x, " ", self.y)

    def draw(self, win, scale_row, scale_col):
        x_scale = self.x * scale_row
        y_scale = self.y * scale_col
        top = Line(Point(x_scale, y_scale), Point(x_scale + self.size, y_scale))
        left = Line(Point(x_scale, y_scale), Point(x_scale, y_scale + self.size))
        right = Line(Point(x_scale + self.size, y_scale), Point(x_scale + self.size, y_scale + self.size))
        bottom = Line(Point(x_scale, y_scale + self.size),
                      Point(x_scale + self.size, y_scale + self.size))
        top.setFill('black')
        top.setWidth(3)
        left.setFill('black')
        left.setWidth(3)
        right.setFill('black')
        right.setWidth(3)
        bottom.setFill('black')
        bottom.setWidth(3)
        if self.walls[0]:
            top.draw(win)
        if self.walls[1]:
            left.draw(win)
        if self.walls[2]:
            right.draw(win)
        if self.walls[3]:
            bottom.draw(win)


class Map:

    def __init__(self, row, col, win):
        self.row = row
        self.col = col
        self.mapping = [[[] for j in range(row)] for i in range(col)]
        for x in range(0, self.row):
            for y in range(0, self.col):
                self.mapping[x][y] = Block(x, y, win.getHeight() / self.row)

    def draw(self, win):
        for x in range(0, self.row):
            for y in range(0, self.col):
                if self.mapping[x][y].visited:
                    self.mapping[x][y].draw(win, win.getHeight()/self.row, win.getHeight()/self.col)

    def check_neighbours(self, b):
        i = b.x
        j = b.y
        neighbours = []
        count = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                if i + x >= self.row or j + y >= self.col or i + x < 0 or j + y < 0:
                    continue
                if x == 0 and y == 0:
                    continue
                if x**2 == 1 and y**2 == 1:
                    continue
                if not self.mapping[i + x][j + y].visited:
                    neighbours.append(self.mapping[i + x][j + y])
                    count += 1
        if count <= 0:
            return None
        rand_neighbour = neighbours[randint(0, count - 1)]
        self.remove_wall(self.mapping[i][j], rand_neighbour)
        return rand_neighbour

    def visit(self, x, y, win, color):
        b = self.mapping[x][y]
        b.draw_rec(win, win.getHeight()/self.row, win.getHeight()/self.col, color)

    def remove_wall(self, a, b):
        x_cord = a.x - b.x
        y_cord = a.y - b.y

        if x_cord == 1:
            a.walls[1] = False
            b.walls[2] = False
        elif x_cord == -1:
            a.walls[2] = False
            b.walls[1] = False
        if y_cord == 1:
            a.walls[0] = False
            b.walls[3] = False
        elif y_cord == -1:
            a.walls[3] = False
            b.walls[0] = False

    def delete_walls(self, b):
        for i in range(0, 4):
            b.walls[i] = False


