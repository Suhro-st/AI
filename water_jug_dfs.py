import heapq

goal = ((1,2,3),(4,5,6),(7,8,0))

# Heuristic: Manhattan Distance
def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                goal_x = (val - 1) // 3
                goal_y = (val - 1) % 3
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

# Cari posisi 0 dan gerakan
def get_neighbors(state):
    neighbors = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x, y = i, j

    moves = [(-1,0),(1,0),(0,-1),(0,1)]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(tuple(tuple(row) for row in new_state))

    return neighbors

def astar(start):
    open_list = []
    heapq.heappush(open_list, (0, start, []))
    closed = set()

    while open_list:
        f, state, path = heapq.heappop(open_list)

        if state in closed:
            continue

        path = path + [state]

        if state == goal:
            return path

        closed.add(state)

        for neighbor in get_neighbors(state):
            if neighbor not in closed:
                g = len(path)
                h = heuristic(neighbor)
                heapq.heappush(open_list, (g + h, neighbor, path))

    return None


# Initial State
start = ((1,2,3),
         (4,0,6),
         (7,5,8))

result = astar(start)

# Output
print("=== SOLUSI A* ===")
for i, step in enumerate(result):
    print(f"Langkah {i}:")
    for row in step:
        print(row)
    print("-----")
