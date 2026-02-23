# Program should have a type error, TypeError: can only concatenate str (not "int") to str
# Return type of the function should be a list of integers and strings, if it doesn't error

from typing import List, Union, Optional

# mystery function
def mysteryfunction5(x: int) -> bool:
    half: float = x / 2
    ans: bool = True
    if half == 0:
        return ans
    else:
        ans = False
        return ans
        
# main program
a: List[int | bool | str | float] = [0, 12.0, True, "apple", -1, False]



result1 = mysteryfunction5(a[0])
print(result1)

result1 = mysteryfunction5(a[3])
print(result1)