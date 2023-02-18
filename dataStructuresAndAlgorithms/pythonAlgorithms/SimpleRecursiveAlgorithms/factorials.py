'''
factorial formula: n! = (n) * (n-1) * (n-3)...
'''

def iterative_factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
        print(fact)
    return fact
def recursive_factorial(n):
    if n == 1:
        return n
    else:
        temp = recursive_factorial(n-1)
        temp = temp * n
    return temp
# can write less code for same result using recursion
# def recur_factorial(n):
#     if n==1: return n
#     else: return n * recur_factorial(n - 1)

#recursively swap two letters
def permute(string, pocket=""): #pocket for new, swapped string
    if len(string) == 0: #edge case, if string is empty, return the empty pocket(default)
        print(pocket)
    else:
        for i in range(len(string)):
            letter = string[i] #each letter in the string
            front = string[0:i] #front of the string
            back = string[i+1:] #back of the string
            together = front + back
            permute(together, letter + pocket)



'''
# iterative version ( more efficient )

from math import factorial

def permutations(str):
    for p in range(factorial(len(str))):
        print(''.join(str))
        i = len(str) - 1
        while i > 0 and str[i - 1] > str[i]:
            i -= 1
        str[i:] = reversed(str[i:])
        if i > 0:
            q = i
            while str[i - 1] > str[q]:
                q += 1
            temp = str[i - 1]
            str[i - 1] = str[q]
            str[q] = temp
s = 'abc'
s = list(s)
permutations(s)
'''

'''N queens problem:
find all possible permutations of queens on an 8x8 chessboard without them being able to attack another

code to be uploaded...

'''