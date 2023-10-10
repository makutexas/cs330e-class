def my_zip(*args):
    """Functionally equivalent to zip()"""
    if not args:
        return []

    # Create iterators for all args
    iter_args = []
    for i in args:
        if isinstance(i, (list, tuple)) and not i:  # Check for empty list or tuple
            return []
        iter_args.append(iter(i))

    # Create tuples and add to result
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
    pass
