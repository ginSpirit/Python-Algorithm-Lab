def lcs(a, b):
    m, n= len(a), len(b)
    dp = [[0] * (n+1) for _ in range(m+1)] #initialize korlam

    for i in range(1, m+1):
        for j in range(1, n+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # Retrieve the longest common subsequence from the matrix
    i = m
    j = n
    lcs = ""
    while i > 0 and j > 0:
        if a[i-1] == b[j-1]:
            lcs = a[i-1] + lcs
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return lcs

a = "university"
b = "united now"

print(lcs(a, b))
