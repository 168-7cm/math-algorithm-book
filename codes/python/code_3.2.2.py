
def GCD(A, B):
    # 片方が0になるまで処理を続ける
    while A >= 1 and B >= 1:
        if A < B:
            B = B % A  # A < B の場合、大きい方Bを書き換える
        else:
            A = A % B  # A >= B の場合、大きい方Aを書き換える
    if A >= 1:
        return A
    return B


print(GCD(77, 66))
