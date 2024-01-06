import heapq

def heuristic(current, goal):
    # Manhattan distance heuristic for A*
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

def astar(maze, start, goal):
    heap = [(0 + heuristic(start, goal), 0, start, [])]
    visited = set()

    while heap:
        _, cost, current, path = heapq.heappop(heap)
        x, y = current

        if current == goal:
            return path

        if current not in visited:
            visited.add(current)

            # Explore neighbors
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dy, y + dx
                if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze) and maze[ny][nx] != 1 and (nx, ny) not in visited:
                    heapq.heappush(heap, (cost + 1 + heuristic((nx, ny), goal), cost + 1, (nx, ny), path + [(nx, ny)]))

    return []