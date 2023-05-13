    def prodExceptSelf(self, n: List[int]) -> List[int]:
        result = [1 for _ in n]
        
        l = 1
        r = 1
        
        for i in range(len(n)):
            result[i] *= l
            result[-1-i] *= r
            l *= n[i]
            r *= n[-1-i]
        
        return result
