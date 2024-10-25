import heapq

a = [[0, 1, 2, 0], [1, 0, 4, 6], [2, 4, 0, 3], [0, 6, 3, 0]]


def prim_alg(N, matrix):
    total_length = 0
    mst_edges = []
    visited = [False] * N
    min_heap = [(0, 0, -1)]
    while min_heap:
        length, u, prev = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        total_length += length
        if prev != -1:
            mst_edges.append((prev, u, length))
        for v in range(N):
            if not visited[v] and matrix[u][v] > 0:
                heapq.heappush(min_heap, (matrix[u][v], v, u))
    return total_length, mst_edges


