# 入力
N = 3
S = 11
A = [2, 5, 9]

# bp[i][j] 左からi枚まで使用して、合計jにする組み合わせがある場合「True」,ない場合「False」
dp = [[None] * (S + 1) for i in range(N + 1)]

# 0枚使用して合計0にするパターン（選択しない場合だけなので0）
dp[0][0] = True
# 0枚使用して、合計を出すパターン（できない）
for i in range(1, S + 1):
    dp[0][i] = False

# 動的計画法
for i in range(1, N + 1):
    for j in range(0, S + 1):
        if j < A[i - 1]:
            # j < A[i-1] （例：J = 1、A[i-1] = 2の場合）カード引くことできない。
            dp[i][j] = dp[i - 1][j]
        else:
            # j >= A[i-1]（例：J = 2, A[i-1] = 2の場合）カード引く or カード引かない 2つの選択肢がある
            if dp[i - 1][j] == True:
                # カードを引かない場合（カード[i-1]を足さなくてもJになる）
                dp[i][j] = True
            elif dp[i - 1][j - A[i - 1]] == True:
                # カードを引く場合（カード[i-1]を足してJになる）
                dp[i][j] = True
            else:
                dp[i][j] = False

if dp[N][S] == True:
    print("Yes")
else:
    print("No")
