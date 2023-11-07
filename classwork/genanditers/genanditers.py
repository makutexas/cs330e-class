def my_chain(*args):
    for i in args:
        for j in i:
            yield j
    pass

class my_ccount():
    def __init__(self, start, step):
        self.start = start
        self.step = step
    
    def __iter__(self):
        return self
    
    def __next__(self):
        temp = self.start
        self.start += self.step
        return temp
    
class my_crepeat():
    def __init__(self, num, r=-1):
        self.num = num
        self.r = r
        self.count = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.r == -1:
            return self.num
        
        if self.r < self.count:
            self.count += 1
            return self.num
        else:
            raise StopIteration

print(list(my_chain([1,2,3],[4,5,6])))

x = []
for i in (0, 2):
    
    if i > 10:
        break
    x.append(i)
print(x)