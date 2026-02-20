# program should have no errors, prints 2.0
# program should return a float (decimal)
from typing import List

# function
def mystery_function3(nums: List[int]) -> float:
    total = 0

    for n in nums:
        total += n

    return total / len(nums)

# main
test = [1, 2, 3]
result = mystery_function3(test)
print(result)