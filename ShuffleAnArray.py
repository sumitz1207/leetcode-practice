class Solution:
    def __init__(self, n):
        self.n = [:]
        self.copy = n[:]

    def reset(self):
        self.n = self.copy[:]
        return self.n
        
    def shuffle(self):
        x = len(self.n)
        for i in range(x):
            j = randint(i, x - 1)
            self.n[i], self.n[j] = self.n[j], self.n[i]
        return self.n
