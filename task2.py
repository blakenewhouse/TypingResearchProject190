# Program should have no errors, prints 24
# Program should return an integer

# mystery function
def mysteryfunction2(x):
    x = x * 2
    return x
        
# main program
a = [1, 4, 7]



result = 0
for num in a:
    result = result + mysteryfunction2(num)
print(result)