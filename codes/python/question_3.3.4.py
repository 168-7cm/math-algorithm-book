
# 2つ選んで、合計500円
# 100円と400円、200円と300円の組み合わせしかない
def combination(N, M):
    a, b, c, d = 0, 0, 0, 0
    for i in range(0, N):
        if M[i] == 100:
            a += 1
        if M[i] == 200:
            b += 1
        if M[i] == 300:
            c += 1
        if M[i] == 400:
            d += 1

    return a * d + b * c


N = 10
M = [100, 200, 300, 400, 500, 150, 250, 350, 450, 500]
print(combination(N, M))
