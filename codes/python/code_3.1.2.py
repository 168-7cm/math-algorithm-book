import math


def prime_factorize(N):
    Answer = []
    LIMIT = int(math.sqrt(N))
    for i in range(2, LIMIT+1):
        while N % i == 0:
           # N = N/i
            N /= i
            Answer.append(i)
    if N >= 2:
        Answer.append(int(N))
    return Answer


print(prime_factorize(25))
