n, w = map(int, input().split())
items = []
for i in range(n):
    weight, profit = map(int, input().split())
    items.append({'weight': weight, 'profit': profit})

dp = [[0] * (w + 1) for _ in range(n + 1)]
selected_items = [[0] * (w + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(w + 1):
        if items[i - 1]['weight'] <= j:
            if dp[i - 1][j] < dp[i - 1][j - items[i - 1]['weight']] + items[i - 1]['profit']:
                dp[i][j] = dp[i - 1][j - items[i - 1]['weight']] + items[i - 1]['profit']
                selected_items[i][j] = i
            else:
                dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[n][w])

result = [0] * n
i, j = n, w
while i > 0 and j > 0:
    if selected_items[i][j] != 0:
        result[selected_items[i][j] - 1] = 1
        j -= items[selected_items[i][j] - 1]['weight']
    i -= 1

for idx, value in enumerate(result, start=1):
    print(f"Item {idx} : {value}")
