def threeSum(self, array):
    final = []
    array.sort()
    for i in xrange(len(array)-2):
        if i > 0 and array[i] == array[i-1]:
            continue
        l, r = i+1, len(array)-1
        while l < r:
            s = array[i] + array[l] + array[r]
            if s < 0:
                l +=1 
            elif s > 0:
                r -= 1
            else:
                final.append((array[i], array[l], array[r]))
                while l < r and array[l] == array[l+1]:
                    l += 1
                while l < r and array[r] == array[r-1]:
                    r -= 1
                l += 1; r -= 1
    return final
