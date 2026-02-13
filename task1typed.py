# Program should have a type error, TypeError: can only concatenate str (not "int") to str
# Return type of the function should be a list of integers and strings, if it doesn't error

from typing import List, Union, Optional

# mystery function
def mysteryfunction1(x: list[int | str]) -> list[int | str]:
    idx: int = 0
    for i in x:
        x[idx] = i + 1
        idx = idx + 1
    return x
        
# main program
a: list[int | str] = [1, 2, "apple"]

result = mysteryfunction1(a)
print(result)
