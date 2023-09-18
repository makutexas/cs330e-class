from unittest import main, TestCase
from Maximum import maximum

class MyUnitTests(TestCase):
    def test_1(self):
        self.assertEqual(maximum(1,2,3), 3)

if __name__ == '__main__': #pragma: no cover
    main()