N = 10
A = [9, 2, 10, 99, 45, 33, 3, 29, 76, 65]

# 選択ソート
# 最後に残ったものはソートしなくていいので、N-1
for i in range(N - 1):
    min_position = i
    min_value = A[i]
    for j in range(i + 1, N):
        # A[0] = 2, A[1] = 1
        if A[j] < min_value:
            min_position = j  # min_position は最小値のインデックス（0 ～ N-1）（min_position = 1）
            min_value = A[j]  # min_value は現時点での最小値（min_value = 2）
    # A[i] と A[min_position] を交換（A[0] = 9 → A[1] = 2, A[1] = 2 → A[i] = 9）
    A[i], A[min_position] = A[min_position], A[i]

# 出力
for i in range(N):
    print(A[i])
