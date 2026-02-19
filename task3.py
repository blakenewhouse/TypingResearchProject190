# program should have no errors, prints 2.0
# program should return a float (decimal)

# function
def mystery_function1(nums):
    total = 0

    for n in nums:
        total += n

    return total / len(nums)

# main
test = [1, 2, 3]
result = mystery_function1(test)
print(result)