""" Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

"""

def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ''
    shortest = min(strs, key=len)

    for i, char in enumerate(shortest):
        for element in strs:
            if element[i] != char:
                return shortest[:i]
    return shortest


if __name__ == '__main__':
    strs = ['flower', 'flow', 'flight']
    print(longestCommonPrefix(strs))