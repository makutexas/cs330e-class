def my_map(func, iterable):
    # n_iterable = []
    for i in iterable:
        yield func(i)
    # return iter(n_iterable)

x = my_map(lambda x : x ** 2, [7,2,3,4])
print(list(x))
print(list(x))