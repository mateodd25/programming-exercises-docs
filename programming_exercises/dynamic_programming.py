"""
This is an example for the sphinx worksheet
"""
__autour__ = 'Mateo Diaz'


def isMatch(s, p):
    """ Perform regular simple expression matching

    Given an input string s and a pattern p, run regular expression
    matching with support for '.' and '*'.

    Parameters
    ----------
    s : str
        The string to match.
    p : str
        The pattern to match.

    Returns
    -------
    bool
        Was it a match or not.
    """

    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    dp[0][0] = True
    # The only way to match a length zero string
    # is to have a pattern of all *'s.
    for ii in range(1, len(p)):
        if p[ii] == "*" and dp[0][ii-1]:
            dp[0][ii + 1] = True

    for ii in range(len(s)):
        for jj in range(len(p)):
            # Matching a single caracter c or '.'.
            if p[jj] in {s[ii], '.'}:
                dp[ii+1][jj+1] = dp[ii][jj]

            elif p[jj] == '*':
                # Double **, which is equivalent to *
                if p[jj-1] not in {s[ii], '.'}:
                    dp[ii+1][jj+1] = dp[ii+1][jj-1]
                    # We can match .* or c* multiple times, once, or zero
                    # times (respective clauses in the or's)
                else:
                    dp[ii+1][jj+1] = dp[ii][jj+1] or dp[ii+1][jj] or dp[ii+1][jj-1]

    return dp[-1][-1]
