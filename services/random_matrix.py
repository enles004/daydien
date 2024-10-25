import random


def generate_random_matrix(N):
    matrix = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(i + 1, N):
            weight = random.randint(1, 20)
            matrix[i][j] = weight
            matrix[j][i] = weight
    return N, matrix
