    def threeSumC(self, n, t):
        n.sort()
        res = n[0] + n[1] + n[2]
        for i in range(len(n) - 2):
            j, k = i+1, len(n) - 1
            while j < k:
                sum = n[i] + n[j] + n[k]
                if sum == t:
                    return sum
                
                if abs(sum - t) < abs(res - t):
                    res = sum
                
                if sum < t:
                    j += 1
                elif sum > t:
                    k -= 1
            
        return res
