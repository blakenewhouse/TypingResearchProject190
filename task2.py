# Program should have no errors, prints 24
# Program should return an integer

# mystery function
def mysteryfunction2(x):
    x = x * 2
    return x
        
# main program
a = [1, 4, 7]
result = 0
for i in a:
    result += mysteryfunction2(i)

    
print(result)

