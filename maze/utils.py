import random

def generate_maze(width, height):
    # 初始化
    grid = [[1 for _ in range(width)] for _ in range(height)]
    start_x, start_y = 1, 1
    grid[start_y][start_x] = 0

    # 生成迷宮 (Recursive Backtracker)
    stack = [(start_x, start_y)]
    while stack:
        x, y = stack[-1]
        neighbors = []
        for dx, dy in [(-2,0), (2,0), (0,-2), (0,2)]:
            nx, ny = x+dx, y+dy
            if 1 <= nx < width-1 and 1 <= ny < height-1 and grid[ny][nx]==1:
                neighbors.append((nx, ny))
        if neighbors:
            nx, ny = random.choice(neighbors)
            grid[ny][nx] = 0
            grid[y + (ny - y)//2][x + (nx - x)//2] = 0
            stack.append((nx, ny))
        else:
            stack.pop()

    # 求解路徑（唯一解）與 dead_ends
    solution, dead_ends = solve_maze_dfs(grid)
    return {
        "width": width,
        "height": height,
        "grid": grid,
        "solution": solution,
        "dead_ends": dead_ends
    }

def solve_maze_dfs(grid):
    height = len(grid)
    width = len(grid[0])
    start, end = (1,1), (width-2, height-2)
    stack = [(start, [start])]
    visited = set([start])
    dead_ends = set()

    while stack:
        (x, y), path = stack[-1]
        if (x, y) == end:
            return path, list(dead_ends)

        neighbors = []
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < width and 0 <= ny < height and grid[ny][nx]==0 and (nx, ny) not in visited:
                neighbors.append((nx, ny))

        if neighbors:
            nx, ny = neighbors[0]
            visited.add((nx, ny))
            stack.append( ((nx, ny), path + [(nx, ny)]) )
        else:
            dead_ends.add((x, y))
            stack.pop()
    return [], list(dead_ends)