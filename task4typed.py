# program will have not have an error, will print "hello_" 5 times
# Return type of the function should be a string, the specified word the specific number of times
from typing import List

# function
def mystery_function4(items: list[int | str]) -> int | str:
    return items[0] * items[1]

# main
items = ["hello_", 5, "world_", 2]

result = mystery_function4(items)

print(result)