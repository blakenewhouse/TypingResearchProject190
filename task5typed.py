# Program should have a type error after printing True, TypeError: unsupported operand type(s) for /: 'str' and 'int'
# Return type of the function should be a boolean, if it doesn't error

from typing import List, Union, Optional

# mystery function
def mysteryfunction1(x: int) -> bool:
    half: float = x % 2
    ans: bool = True
    if half == 0:
        return ans
    else:
        ans = False
        return ans
        
# main program
a: List[int | bool | str | float] = [0, 12.0, True, "apple", -1, False]



result1 = mysteryfunction1(a[0])
print(result1)

result1 = mysteryfunction1(a[3])
print(result1)