# 入力
N = int(input())
# N = 10
A = list(map(int, input().split()))
# A = [1,2,3,4,5,6,7,8,9,10]

# 答えを求める
# N個の要素を持つ配列を0で初期化
cnt = [0 for i in range(100000)]
for i in range(N):
    cnt[A[i]] += 1

Answer = 0
# Aが100,000以下なので、その半分の50,000にする
for i in range(1, 50000):
    Answer += cnt[i] * cnt[100000 - i]
Answer += cnt[50000] * (cnt[50000] - 1) // 2

# 出力
print(Answer)
