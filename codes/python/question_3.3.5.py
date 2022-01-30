
def a(N, A):
    # N枚のカードを2枚選ぶ場合、「赤」、「青」、「黄」の同じ色を選ぶパターン数はいくつか

    red, yellow, blue = 0, 0, 0

    for i in range(0, N):
        if A[i] == 1:
            red += 1
        if A[i] == 2:
            yellow += 1
        if A[i] == 3:
            blue += 1

    return combination(red, 2) + combination(yellow, 2) + combination(blue, 2)
   # 別解
   # return red * (red - 1) // 2 + yellow * (yellow - 1) // 2 + blue * (blue - 1) // 2


def combination(N, M):
    # combinationを出す関数（nCm）
    return factorial(N)/factorial(M)


def factorial(N):
    # 階乗を求める関数
    if N == 1:
        return N
    return N * factorial(N-1)


N = 10
M = [1, 2, 3, 2, 3, 1, 2, 1, 2, 3]

print(a(N, M))
