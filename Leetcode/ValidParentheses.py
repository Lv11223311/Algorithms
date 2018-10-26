""" Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid. """

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # use stack, a simple exp
        stack = []
        for i in s:
            if i in ['(', '[', '{']:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if (top == '(' and i != ')') or (top == '(' and i != ')') or (top == '{' and i != '}'):
                    return False
        return True if len(stack)==0 else False
