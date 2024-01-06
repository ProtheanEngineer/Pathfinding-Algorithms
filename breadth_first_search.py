from collections import deque

def get_neighbors(maze, current):
    x, y = current

    neighbors = []

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Possible movements: up, down, left, right

    for dx, dy in directions:
        nx, ny = x + dy, y + dx
        if 0 <= ny < len(maze) and 0 <= nx < len(maze[0]) and maze[ny][nx] != 1:
            neighbors.append((nx, ny))

    return neighbors

def bfs(maze, start, goal):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        current, path = queue.popleft()
        x, y = current

        if current == goal:
            return path

        if current not in visited:
            visited.add(current)

            neighbors = get_neighbors(maze, current)
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    return []

# def get_neighbors(grid, node):
#     x, y = node
#     neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
#     rows, cols = len(grid), len(grid[0])
#     valid_neighbors = [(i, j) for i, j in neighbors if 0 <= i < rows and 0 <= j < cols and grid[i][j] == 0]
#     return valid_neighbors

# def bfs(grid, start, goal):
#     queue = [(start, [start])]
#     rows, cols = len(grid), len(grid[0])
#     visited = set()

#     while queue:
#         current, path = queue.pop(0)
#         x, y = current

#         if current == goal:
#             return path

#         if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 0 and current not in visited:
#             visited.add(current)
#             for neighbor in get_neighbors(grid, current):
#                 queue.append((neighbor, path + [neighbor]))

    # return []