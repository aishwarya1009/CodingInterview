#https://leetcode.com/problems/decode-ways/
class Solution:
    def numDecodings(self, s: str) -> int:
        # empty string is not valid
        if len(s) == 0:
            return 0
        # string starting with 0 is not valid
        elif s[0] == '0':
            return 0
        else:
            length = len(s)
            dp = [0] * (length + 1)
            dp[0] = 1
            dp[1] = 1
            for i in range(1,length):
                # case of merge only so the state is same as that of t-2 eventie i-1
                if s[i] =='0':
                    if int(s[i-1]+s[i]) <=26 and int(s[i-1]+s[i]) > 0:
                        dp[i+1] = dp[i-1]
                    else:
                        return 0
                # case of merge or no merge
                else:
                    # case where merge and no merge b0th are valid so t-1+t-2
                    if int(s[i-1]) > 0 and int(s[i-1]+s[i]) <= 26:
                        dp[i+1] = dp[i] + dp[i-1]
                    # case where merge is not valid so the ans is same as t-1
                    else:
                        dp[i+1] = dp[i]
            return dp[length]