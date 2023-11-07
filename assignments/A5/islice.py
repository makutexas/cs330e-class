def my_islice_generator(iterable, start, stop):
    """Functionally equivalent to itertools.islice()"""
    for i in range (start, stop):
        try:
            yield iterable[i]
        except IndexError:
            return

class my_islice_iterator():
    def __init__(self, iterable, start, stop):
        self.iterable = iterable
        self.start = start
        self.stop = stop
    
    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            if self.start < self.stop:
                self.start += 1
                return self.iterable[self.start - 1]
            else:
                raise StopIteration
        except IndexError:
            raise StopIteration