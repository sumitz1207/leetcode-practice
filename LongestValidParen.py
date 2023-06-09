    def longestValidParen(self, s):
        @lru_cache(None)
        def dp(i):
            if i == -1 or s[i] == "(": return 0
            if i >= 1 and s[i-1:i+1] == "()": return dp(i-2) + 2
            P = i - dp(i-1) - 1
            if P >= 0 and s[P] == "(":
                return dp(i-1) + dp(P-1) + 2
            return 0
            
        return max(dp(i) for i in range(len(s))) if s else 0
