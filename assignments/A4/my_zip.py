def my_zip(*args):
    """Functionally equivalent to zip()"""
    # Check if there are any arguments
    if not args:
        return

    # Create iterators for each argument
    iter_args = [iter(arg) for arg in args]

    # Continue yielding tuples until any iterator is exhausted
    while True:
        iter_tuple = ()
        try:
            for i in range(len(iter_args)):
                iter_tuple += (next(iter_args[i]),)
            yield iter_tuple
        except StopIteration:
            break
