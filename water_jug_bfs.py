from collections import deque

def water_jug_bfs(cap1, cap2, target):
    # 1. BUAT Antrean (QUEUE)
    queue = deque([(0, 0, [])])
    # 2. BUAT Set untuk mencatat yang sudah dikunjungi
    visited = set()

    # 3. SELAMA antrean TIDAK KOSONG
    while queue:
        # a. Ambil data dari DEPAN (popleft)
        j1, j2, path = queue.popleft()

        # b. JIKA Target tercapai
        if j1 == target or j2 == target:
            return path + [(j1, j2)]

        # c. JIKA belum dikunjungi\]
        if (j1, j2) not in visited:
            visited.add((j1, j2))

            # d. Definisikan semua kemungkinan AKSI
            moves = [
                (cap1, j2), (j1, cap2), # Isi
                (0, j2), (j1, 0),       # Kosongkan
                (j1 - min(j1, cap2 - j2), j2 + min(j1, cap2 - j2)), # Tuang 1 ke 2
                (j1 + min(j2, cap1 - j1), j2 - min(j2, cap1 - j1))  # Tuang 2 ke 1
            ]

            # e. Masukkan hasil aksi ke BELAKANG antrean
            for m in moves:
                if m not in visited:
                    queue.append((m[0], m[1], path + [(j1, j2)]))

    return None

# Eksekusi BFS
print("=== SOLUSI BFS (OPTIMAL) ===")
solusi_bfs = water_jug_bfs(5, 3, 4)
for i, step in enumerate(solusi_bfs):
    print(f"Langkah {i}: {step}")
