
# 階乗を求める関数
def factorial(N):
    if N == 1:
        return N
    return N * factorial(N-1)
