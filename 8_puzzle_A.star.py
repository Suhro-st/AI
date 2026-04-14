from collections import deque

# Cek apakah state valid
def is_valid(M_left, C_left):
    M_right = 3 - M_left
    C_right = 3 - C_left

    # Tidak boleh negatif atau lebih dari 3
    if M_left < 0 or C_left < 0 or M_left > 3 or C_left > 3:
        return False

    # Kiri aman
    if M_left > 0 and M_left < C_left:
        return False

    # Kanan aman
    if M_right > 0 and M_right < C_right:
        return False

    return True


# BFS untuk mencari solusi
def bfs():
    start = (3, 3, 0)
    goal = (0, 0, 1)

    queue = deque()
    queue.append((start, []))

    visited = set()

    while queue:
        (M_left, C_left, boat), path = queue.popleft()

        if (M_left, C_left, boat) in visited:
            continue

        visited.add((M_left, C_left, boat))

        # Jika sampai tujuan
        if (M_left, C_left, boat) == goal:
            return path + [(M_left, C_left, boat)]

        # Kemungkinan perpindahan
        moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]

        for m, c in moves:
            if boat == 0:  # dari kiri ke kanan
                new_state = (M_left - m, C_left - c, 1)
            else:  # dari kanan ke kiri
                new_state = (M_left + m, C_left + c, 0)

            new_M, new_C, new_boat = new_state

            if is_valid(new_M, new_C):
                queue.append((new_state, path + [(M_left, C_left, boat)]))

    return None


# Jalankan BFS
solution = bfs()

# Tampilkan hasil
if solution:
    print("Solusi ditemukan:\n")
    for step in solution:
        print(step)
else:
    print("Tidak ada solusi")
