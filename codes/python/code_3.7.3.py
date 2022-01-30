# 入力
N = 4
W = 10
w = [3, 6, 4, 2]
v = [100, 210, 130, 57]

# 配列の初期化
dp = [[None] * (W + 1) for i in range(N + 1)]
# dp[i][j]：品物iまでの中から、重さの合計がjとなるように選んだ時の価値の最大値
dp[0][0] = 0

# dp[0]（何も選ばない）場合は、重さも0になる
for i in range(1, W + 1):
    dp[0][i] = 0
print(dp)

# 動的計画法
# アイテムは0~4個なので、N + 1
for i in range(1, N + 1):
    # 重さも0~10なので、W + 1
    for j in range(0, W + 1):
        # アイテム1個で重さ0
        if j < w[i - 1]:
            print(i, j)
            # j < w[i-1]のときは方法Aしか選べない（品物i-1までの重さの総和がjであり、品物iを選ばない）
            dp[i][j] = dp[i - 1][j]
        else:
            # j >= w[i-1] のとき、方法 A・方法 B どちらも選べる（品物i-1までの重さの総和がj-wiであり、品物iを選ぶ）
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i - 1]] + v[i - 1])

# 答えを計算して出力
print(dp)
answer = max(dp[N])
print(answer)
