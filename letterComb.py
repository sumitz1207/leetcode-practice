    def letterCom(self, digits):
        m = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(m[digits[0]])
        prev = self.letterCom(digits[:-1])
        ad = m[digits[-1]]
        return [s + c for s in prev for c in ad]
