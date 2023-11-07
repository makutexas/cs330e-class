class my_range:
    def __init__(self, b, e):
        self.b = b
        self.e = e
    def __iter__(self):
        # b= self.b
        # e = self.e
        while self.b != self.e:
            yield self.b
            self.b +=1

x = my_range(1,3)
print(list(x),end = "")
print(list(x))