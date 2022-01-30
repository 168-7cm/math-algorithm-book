# 最大公約数を返す関数
def GCD(A, B):
    while A >= 1 and B >= 1:
        if A < B:
            B = B % A  # A < B の場合、大きい方Bを書き換える
        else:
            A = A % B  # A >= B の場合、大きい方Aを書き換える
    if A >= 1:
        return A
    return B

# 最大公倍数を返す関数
def LCM(A, B):
    return int(A*B/GCD(A, B))

N = 4
A = [100, 20, 4, 2]

# まずは2つで最小公倍数を出す。
R = LCM(A[0], A[1])

# ↑で出した最小公倍数と残りの要素で最小公倍数を出す。
for i in range(2, N):
    R = LCM(R, A[i])

print(R)
