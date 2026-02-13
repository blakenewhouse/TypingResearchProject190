# Program should have a type error, TypeError: can only concatenate str (not "int") to str
# Return type of the function should be a list of integers and strings, if it doesn't error

# mystery function
def mysteryfunction1(x):
    idx = 0
    for i in x:
        x[idx] = i + 1
        idx = idx + 1
    return x
        
# main program
a = [1, 2, "apple"]

result = mysteryfunction1(a)
print(result)
