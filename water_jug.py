from collections import deque

def water_jug_bfs(J1, J2, L):
    queue = deque([(0, 0)])
    visited = set()
    visited.add((0, 0))
    parent = {}

    while queue:
        x, y = queue.popleft()
        print(f"Visiting state: ({x}, {y})")

        if x == L or y == L:
            print("\nFound solution!")
            path = []
            while (x, y) in parent:
                (prev_x, prev_y), action = parent[(x, y)]
                path.append(action)
                x, y = prev_x, prev_y
            path.reverse()
            return path

        moves = [
            ((J1, y), "Fill Jug 1"),
            ((x, J2), "Fill Jug 2"),
            ((0, y), "Empty Jug 1"),
            ((x, 0), "Empty Jug 2"),
            ((x - min(x, J2 - y), y + min(x, J2 - y)), "Pour Jug 1 -> Jug 2"),
            ((x + min(y, J1 - x), y - min(y, J1 - x)), "Pour Jug 2 -> Jug 1")
        ]

        for (next_x, next_y), action in moves:
            if (next_x, next_y) not in visited:
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))
                parent[(next_x, next_y)] = ((x, y), action)

    return "No solution exists!"

J1 = 4
J2 = 3
L = 2

solution = water_jug_bfs(J1, J2, L)
if isinstance(solution, list):
    print("\nSolution Path:")
    for step in solution:
        print(step)
else:
    print(solution)
