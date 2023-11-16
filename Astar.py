class Node:
    def __init__(self, value, coord):
        self.value = value
        self.coord = coord
        self.g = 0
        self.h = 0
        self.parent = None

    def __str__(self):
        s = f'{self.coord} f= {self.g+self.h:0.2f} g={self.g:0.2f}, h= {self.h:0.2f}'
        return s

    def move_cost(self, other):
        return 1

def children(current_node, grid):
    x, y = current_node.coord
    links = [(x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)]
    valid_links = [link for row in grid for link in row if link.value != 0]
    valid_children = [link for link in valid_links if link.coord in links]

    return valid_children

def manhattan(node, goal):
    xN, yN = node.coord
    xG, yG = goal.coord
    h = abs(xN - xG) + abs(yN - yG)
    return h

def aStar(start, goal, grid):
    OPEN = list()
    CLOSED = list()
    current = start
    OPEN.append(current)
    i = 0

    while OPEN:
        i += 1
        current = min(OPEN, key=lambda o: o.g + o.h)

        print(f"Iteration {i}: {current}")

        if current == goal:
            path = []
            while current.parent:
                path.append(current)
                current = current.parent
            path.append(current)
            return path[::-1]

        OPEN.remove(current)
        CLOSED.append(current)

        for node in children(current, grid):
            if node in CLOSED:
                new_cost = current.g + current.move_cost(node)
                if new_cost <= node.g:
                    OPEN.append(node)
                    CLOSED.remove(node)
            elif node in OPEN:
                new_cost = current.g + current.move_cost(node)
                if new_cost <= node.g:
                    node.g = new_cost
                    node.parent = current
            else:
                node.g = current.g + current.move_cost(node)
                node.h = manhattan(node, goal)
                node.parent = current
                OPEN.append(node)

    return None

# Initialize grid and start/goal nodes
grid = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 0, 0],
    [1, 1, 0, 1]
]

for x in range(len(grid)):
    for y in range(len(grid[x])):
        grid[x][y] = Node(grid[x][y], (x, y))

start = grid[4][0]
goal = grid[0][3]

# Find the path using A*
path = aStar(start, goal, grid)

# Check if a path was found
if path:
    print("** Path ** ")
    for p in path:
        print(p.coord, end=" ")
else:
    print("No path found")
