from unittest import main, TestCase
from Avg import avg

class MyUnitTests(TestCase):
    def test_1(self):
        self.assertEqual(avg([1,2,3]), 2)

if __name__ == '__main__':
    main()