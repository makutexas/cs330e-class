from my_zip import *

# tests for my_zip
def test_zip () :
   print("my_zip()")

   assert list(my_zip()) == []
   assert list(my_zip([])) == []
   assert list(my_zip((), ())) == []
   assert list(my_zip([2, 3])) == [(2,), (3,)]
   assert list(my_zip((2, 3), (4, 5), (6, 7))) == [(2, 4, 6), (3, 5, 7)]
   assert list(my_zip([2, 3, 4], [5, 6, 7])) == [(2, 5), (3, 6), (4, 7)]
   assert list(my_zip(iter([2, 3, 4]), iter([5, 6, 7]))) == [(2, 5), (3, 6), (4, 7)]

   a = [2, 3, 4]
   b = [5, 6, 7]
   c = my_zip(a, b)
   assert next(c) == (2, 5)
   assert next(c) == (3, 6)   
   assert next(c) == (4, 7)

test_zip()