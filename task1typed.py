from typing import List, Union, Optional

# mystery function
def mysteryfunction1(x: list[int | str]) -> list[int | str]:
    for i in x:
        i += 1
        
# main program
a: list[int | str] = [1, 2, "apple"]

result = mysteryfunction1(a)

