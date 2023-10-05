def my_zip(*args):
    """Functionally equivalent to zip()"""

    #Turn all args into iterators
    iter_args = []
    for i in args:
        if i == list() or i == tuple():
            pass
        if type(i) == list or type(i) == tuple:
            iter_args.append(iter(i))
        else:
            iter_args.append(i)

    #Create tuples and add to result
    result = []
    while True:
        iter_tuple = ()
        try:
            for i in range(len(iter_args)):
                iter_tuple += (next(iter_args[i]),)
            result.append(iter_tuple)
        except StopIteration:
            break

    return result

if __name__ == "__main__":
    print(my_zip((2, 3), (4, 5), (6, 7)))
        