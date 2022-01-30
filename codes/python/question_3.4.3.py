def expectedValue(N, A, B):
    # 期待値を求める関数
    answer = 0
    for i in range(0, N):
        answer += (1 / 3) * A[i] + (2 / 3) * B[i]
    return answer


N = 10
A = [10, 1, 3, 4, 6, 10, 3, 8, 4, 5]
B = [9, 3, 0, 0, 2, 1, 3, 11, 12, 7]

print(expectedValue(N, A, B))
