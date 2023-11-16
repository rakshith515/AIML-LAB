class Node:
    def __init__(self, index, cost, visited=False, and_map=False, solved=False):
        self.index = index
        self.cost = cost
        self.visited = visited
        self.and_map = and_map
        self.solved = solved
        self.children = None
        self.path = None

    def __str__(self):
        return f'{self.index}:{self.cost}'

EDGE = 5
cost = [None, 0, 40, 2, 4, 1, 2, 3, 50, 60, 70, 80, 4, 5, 8, 9, 6, 7, 90, 90, 90, 90]
children = {1: [2, 3, 4], 2: [5, 6, 7], 3: [8, 9], 4: [10, 11], 5: [12, 13], 6: [14, 15], 7: [16, 17],
            8: [18], 9: [19], 10: [20], 11: [21]}
print(len(cost))
nodes = [Node(i, cost[i]) for i in range(len(cost))]
for k, v in children.items():
    nodes[k].children = [nodes[i] for i in v]

ae = {1: [3, 4], 2: [5, 6, 7]}
and_edges = {}
for k, v in ae.items():
    and_edges[nodes[k]] = tuple([nodes[i] for i in v])
    for i in v: nodes[i].and_map = True

for a in nodes:
    if not a.children:
        a.solved = True

for a in nodes:
    print(f'{a} solved: {a.solved}, and_map: {a.and_map}')

def eval_arcs(arc, head):
    if arc.and_map:
        ae = and_edges[head]
        cost = sum(aek.cost + EDGE for aek in ae)
        solved = all(aek.solved for aek in ae)
        return ae, cost, solved
    else:
        return (arc,), arc.cost + EDGE, arc.solved

def aostarUtil(head):
    eval_nodes = {}
    for c in head.children:
        arc, cost, solved = eval_arcs(c, head)
        if solved: head.solved = True
        c.path = False
        eval_nodes[arc] = cost

    head.cost = min(eval_nodes.values())
    best = min(eval_nodes, key=eval_nodes.get)

    if head.solved:
        head.path = True
        for b in best: b.path = True

    if not head.visited:
        head.visited = True
        print(f'Explore head: {head}')
        return

    print(f'Update head costs: {head}')
    print('Best Move: ', end='')
    for a in best: print(a, end=' ')
    print()

    for b in best:
        if not b.solved: aostarUtil(b)

def aostar(head):
    i = 0
    while not head.solved and i < MAX:
        print(f'\nIteration: {i} *****')
        aostarUtil(head)
        i += 1

MAX = 1000
head = nodes[1]
aostar(head)

print(f'Cost of solution on {head}')
for a in nodes:
    if a.path:
        print(a)
