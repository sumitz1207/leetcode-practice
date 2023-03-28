    def rob(self, nums):
        temp, final = 0, 0
        for i in nums: temp, final = final, max(temp + i, final)
                
        return final
