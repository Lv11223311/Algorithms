# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):

    if len(text)==1:
        return 1

    opening_brackets_stack = []
    pos = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(next)
        if next in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) == 0:
                return i+1
            else:
                top = opening_brackets_stack.pop()
                if are_matching(top, next):

                else:
                    return i+1
    return True if len(opening_brackets_stack) == 0 else len
        
    



def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if mismatch is True:
        print('Success')
    else:
        print(mismatch)



if __name__ == "__main__":
    main()