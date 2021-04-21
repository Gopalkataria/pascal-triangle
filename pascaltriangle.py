# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
## variables to keep storing calculations in memory
## so after each calculation is done, it just gets stored in ram for future use
## dramatically improves speed 
factorials = {} 
combinations = {} 


# %%
## function to find factorial with memoization
def factorial( n : int ) :
    if n == 0 or n ==1  :
        return 1 
    elif n < 0 :
        return 0 
    elif n in factorials :
        return factorials[n]
    else :
        factorials[n] = n* factorial(n-1)
        return factorials[n]


# %%
## function to find combinations with memoization
def combination(inp : tuple ) :
    n , r = inp[0] , inp[1]
    if n == r or r == 0 :
        combinations[inp] = 1 
        return combinations[inp] 
    elif inp in combinations :
        return combinations[inp]
    else : 
        combinations[inp] = int(factorial(n) / ( factorial(r) * factorial(n-r ))) 
        return combinations[inp] 


# %%
## function to print nth row of pascal triangle
def pascal_triangle(row : int ) :
    for x in range(row + 1 ) :
        print(combination( (row , row - x) ), end=" ")


# %%
for c in range( 10):
    pascal_triangle(c)
    print("\n")


# %%



