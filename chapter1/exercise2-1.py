import unittest
from collections import Counter

def isPermutation(string1, string2):

     if len(string2) > len(string1):
         return False

     counter_string = Counter(string1)
     for c in string2:
          if counter_string.get(c, 0) == 0:
              return False
          counter_string[c] -= 1

     return True

class Test(unittest.TestCase):
    true_cases = [(['abcd', 'bacd']), (['3563476', '7334566']),
             (['wef34f', 'wffe34'])]

    false_cases = [(['abcd', 'd2cba']), (['2354', '1234']), (['dcw4f', 'dcw5f'])]

    def test_permutation(self):
        for case in self.true_cases:
            result = isPermutation(*case)
            self.assertTrue(result)

        for case in self.false_cases:
            result = isPermutation(*case)
            self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
