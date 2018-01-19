# coding: utf-8
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) == 0:
        return False
    if len(aStr) == 1:
        if char == aStr:
            return True
        else:
            return False
    else:
        i = len(aStr) // 2  # Posição do elemento sendo testado
        if char > aStr[i]:
            return isIn(char, aStr[i + 1:])
        elif char < aStr[i]:
            return isIn(char, aStr[:i])
        else:
            return True



print(isIn('v', 'ccdffhhlmrrvy'))
print(isIn('n', 'deoqww'))
print(isIn('c', 'acddghlnswxx'))
print(isIn('c', 'acddghlnswxx'))
print(isIn('v', 'qv'))
print(isIn('c', 'cin'))
print(isIn('d', 'cdefhjjnuy'))
print(isIn('j', 'hpq'))
print(isIn('u', 'affiuwyz'))