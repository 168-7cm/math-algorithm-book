
def GCD(A, B):
    while A >= 1 and B >= 1:
        if A < B:
            B = B % A  # A < B の場合、大きい方Bを書き換える
        else:
            A = A % B  # A >= B の場合、大きい方Aを書き換える
    if A >= 1:
        return A
    return B


N = 4
A = [100, 20, 4, 2]

# まずは2つで最大公約数を出す。
R = GCD(A[0], A[1])

# ↑で出した最大公約数と残りの要素で最大公約数を出す。
for i in range(2, N):
    R = GCD(R, A[i])

print(R)
