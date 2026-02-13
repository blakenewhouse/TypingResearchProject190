# Program should have no errors, prints 24
# Program should return an integer

from typing import List, Union, Optional

# mystery function
def mysteryfunction2(x: int) -> int:
    x = x * 2
    return x
        
# main program
a: List[int] = [1, 4, 7]
result = 0
for i in a:
    result += mysteryfunction2(i)
    
print(result)

