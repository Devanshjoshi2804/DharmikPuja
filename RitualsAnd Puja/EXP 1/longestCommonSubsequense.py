def longest_common_subsequence(X, Y):
    m = len(X)
    n = len(Y)

    # Create a table to store the lengths of LCS for all subproblems
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the dp table in a bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct the LCS
    lcs_length = dp[m][n]
    lcs = [""] * (lcs_length + 1)
    i = m
    j = n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs[lcs_length - 1] = X[i - 1]
            i -= 1
            j -= 1
            lcs_length -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(lcs)


def main():
    X = "AGGTAB"
    Y = "GXTXAYB"
    lcs = longest_common_subsequence(X, Y)
    print("Longest Common Subsequence:", lcs)


if __name__ == "__main__":
    main()
