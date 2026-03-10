def outer_function(a,b):
    square = a ** 2
    def inner_function(a,b):
        return a + b
    add = inner_function(a,b)
    return add + 5
result = outer_function(5,10)
print(result)