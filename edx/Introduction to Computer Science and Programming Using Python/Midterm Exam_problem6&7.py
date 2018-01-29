def sumDigits(N):
    '''
    N: inteiro não negativo
    :returns A soma dos algarismos
    '''
    if len(str(N)) == 1:
        return N
    else:
        return N%10 + sumDigits(N//10)
#print(sumDigits(993))

def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you.
    f takes in an integer, applies a function, returns another integer
    g takes in an integer, applies a Boolean function,
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """

    new_L = [L[i] for i in range(len(L)) if g(f(L[i])) == True]
    L[:] = new_L

    if len(L) > 0:
        return max(L)
    else:
        return -1