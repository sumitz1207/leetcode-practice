 def threeSumClosest(self, n: List[int], t: int) -> int:
        
        n.sort()
        
        
        r = float('inf')
        s = 0
        
        for i in range(len(n) - 2):
            
            left = i + 1
            right = len(n) - 1
            
            while left < right:
                
                k = n[i] + n[left] + n[right]
                
                if k > t:
                    right -= 1
                elif k < t:
                    left += 1
                else:
                    return k
                
                if abs(t - k) < r:
                    r = abs(t - k)
                    s = k
                
        return s
