#is Unique: Implement an algorithm to determine id a string has all unique characters.What if you cannot use additional structures?

SHOULD_BE_TRUE = 'Should be True'
SHOULD_BE_FALSE = 'Should be False'

def isUnique(string):

    for i in range(1, len(string)):
       index = i
       char = string[index]
       while index > 0:
           if char == string[index - 1]:
               return False
           index = index - 1
    return True


if __name__ == '__main__':
    print(isUnique('mama')) 
    assert isUnique('asd'),"1.-{}".format(SHOULD_BE_TRUE)
    assert isUnique('aasd') is False, "2.-{}".format(SHOULD_BE_FALSE)
    assert isUnique('mama') is False, "3.-{}".format(SHOULD_BE_FALSE)
