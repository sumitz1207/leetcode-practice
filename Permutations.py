def permute(self, x):
    temp = []
    self.perm(x, [], temp)
    return temp
    
def perm(self, x, y, temp):
    if not x:
        temp.append(y)
    for i in xrange(len(x)):
        self.perm(x[:i]+x[i+1:], y+[x[i]], temp)
