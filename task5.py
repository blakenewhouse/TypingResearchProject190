# Program should have a type error, TypeError: can only concatenate str (not "int") to str
# Return type of the function should be a list of integers and strings, if it doesn't error

from typing import List, Union, Optional

# mystery function
def mysteryfunction1(x):
    half = x % 2
    ans = True
    if half == 0:
        return ans
    else:
        ans = False
        return ans
        
# main program
a = [0, 12.0, True, "apple", -1, False]



result = mysteryfunction1(a[0])
print(result)

result1 = mysteryfunction1(a[3])
print(result1)