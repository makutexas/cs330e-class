from islice import *

def test_my_isslice () :
    print("isslice generator")    
    
    assert list(my_islice_generator('', 2, 5))             == [] 
    assert list(my_islice_generator('ABCDEFG', 2, 5))      == ['C', 'D', 'E'] 
    assert list(my_islice_generator('ABCDEFG', 2, 7))      == ['C', 'D', 'E', 'F', 'G'] 
    
    print("isslice iterator")   
 
    p = my_islice_iterator('', 2, 5)
    assert hasattr(p, "__iter__")
    assert hasattr(p, "__next__")
    q = iter(p)
    assert q is p

    assert list(p) == []
    
    p = my_islice_iterator('ABCDEFG', 2, 5)
    assert hasattr(p, "__iter__")
    assert hasattr(p, "__next__")
    q = iter(p)
    assert q is p
    assert list(p) == ['C', 'D', 'E'] 

    p = my_islice_iterator('ABCDEFG', 2, 7)
    assert hasattr(p, "__iter__")
    assert hasattr(p, "__next__")
    q = iter(p)
    assert q is p
    assert list(p) == ['C', 'D', 'E', 'F', 'G'] 

test_my_isslice()