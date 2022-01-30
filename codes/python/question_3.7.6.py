# 入力
N = 3
A = [2, 4, 5]

# i日目に勉強する場合のこれまでの実力アップの最大値（0日目〜N日目）
dp1 = [None] * (N + 1)
# 1日目から勉強できるので、0日目は、0にする
dp1[0] = 0

# i日目に勉強しない場合のこれまでの実力アップの最大値（0日目〜N日目）
dp2 = [None] * (N + 1)
# 1日目から勉強できるので、0日目は、0にする
dp2[0] = 0

for i in range(1, N + 1):  # （1日目〜N日目）
    # i日目に勉強する場合→i-1 日目に勉強しない。
    dp1[i] = dp2[i-1] + A[i - 1]
    # i日目に勉強しない場合→①i-1日目に勉強する、②i-1日目に勉強しない。
    dp2[i] = max(dp1[i-1], dp2[i-1])

Answer = max(dp1[N], dp2[N])
print(Answer)
