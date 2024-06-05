def print_shapes(n):
  
    
    print("Lower Triangular:")
    for i in range(1, n + 1):
        print('*' * i)
    
    print("\nUpper Triangular:")
    for i in range(n, 0, -1):
        print('*' * i)
    
    print("\nPyramid:")
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars + spaces)


print_shapes(5)