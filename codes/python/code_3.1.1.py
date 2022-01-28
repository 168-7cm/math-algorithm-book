import math


def isprime(N):
    # 総数判定
    sqrt = int(math.sqrt(N))
    for i in range(2, sqrt):
        if N % i == 0:
            return False
    return True


print(isprime(83))
