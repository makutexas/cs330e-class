def reduce_for(bf, iter, seed):
    res = seed
    for i in iter:
        res = bf(res, i)
    return res

def reduce_for_range(bf, iter, seed):
    res = seed
    for i in range(len(iter)):
        res = bf(res, iter[i])
    return res

def reduce_while(bf, iterable, seed):
    res = 0
    y = iter(iterable)
    i = seed
    while y:
        res = bf(res, i)
        i = next(y)

    return res

print(reduce_for(lambda x, y: x + y, [1, 2, 3, 4, 5], 0))
print(reduce_for_range(lambda x, y: x + y, [1, 2, 3, 4, 5], 0))
print(reduce_while(lambda x, y: x + y, [1, 2, 3, 4, 5], 0))