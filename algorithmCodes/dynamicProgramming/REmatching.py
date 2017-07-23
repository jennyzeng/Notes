"""
LeetCode #10.
based on
https://discuss.leetcode.com/topic/6183/my-concise-recursive-and-dp-solutions-with-full-explanation-in-c
"""
def isMatch(s, p):
    """
    '.' Matches any single character.
    '*' Matches zero or more of the preceding element.
    The matching should cover the entire input string (not partial).
    :type s: str
    :type p: str
    :rtype: bool
    """
    m = len(s)
    n = len(p)
    dp = [[None] * (n+1) for _ in range((m + 1))]
    # dp[i][j] means s[:i] matches p[:j]
    dp[0][0] = True  # base case, both s, p empty, so is True
    for i in range(1, m+1):
        # base case when p is empty but
        dp[i][0] = False

    for j in range(1, n+1):
        dp[0][j] = j > 1 and p[j - 1] == '*' and dp[0][j - 2]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if p[j - 1] != '*':
                # for match s[:i] and p[:j], ensure s[:i-1] and p[:j-1] is matched
                # then check if the current last char in the s[:i] and p[:j] matches
                dp[i][j] = dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')
            else:
                # * repeats 0 times             repeat 1+ times, so have to check if the previous repeat time is True
                dp[i][j] = dp[i][j - 2] or ((s[i - 1] == p[j - 2] or p[j - 2] == '.') and dp[i - 1][j])
    return dp[m][n]


if __name__ == '__main__':
    assert isMatch("aa", "a") == False
    assert isMatch("aa", "a.") == True
    assert isMatch("aaa", "a*") == True
    assert isMatch("ab", ".*") == True
    assert isMatch("aab", "c*a*b") == True
