
""" Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows. """

# plan 1
def reverse(x):
    s = str(x)
    if x < 0:
        sign = s[0]
        digit = s[1:]
        new = digit[::-1]
        res = int(sign + new)
    else:
        res = int( s[:: -1])
    return res if -2**31 < res < 2**31 else 0

# plan 2
def reverse2(x):
    # use pythonic sign = [1,-1][x<0], learnt a new thing
    sign = [1, -1][x < 0]
    s = sign * int(str((abs(x)))[::-1])
    return s if -2**31<s<2**31 else 0