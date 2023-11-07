class my_range():
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step
    def __iter__(self):
        return self
    def __next__(self):
        if self.start >= self.stop:
            raise StopIteration
        yield self.start
        self.start += self.step

print(list(my_range(0, 10, 2)))