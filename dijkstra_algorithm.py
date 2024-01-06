import heapq

def dijkstra(maze, start, goal):
    heap = [(0, start, [])]
    visited = set()

    while heap:
        cost, current, path = heapq.heappop(heap)
        x, y = current

        if current == goal:
            return path

        if current not in visited:
            visited.add(current)

            # Explore neighbors
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dy, y + dx
                if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze) and maze[ny][nx] != 1 and (nx, ny) not in visited:
                    heapq.heappush(heap, (cost + 1, (nx, ny), path + [(nx, ny)]))

    return []