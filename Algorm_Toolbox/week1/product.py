# python3
import sys

def Product(nums):
    n = len(nums)
    index1 = -1
    for i in range(n):
        if nums[index1] < nums[i] or index1 == -1:
            index1 = i
    index2 = -1
    for j in range(n):
        if j != index1 and (index2 == -1 or nums[j] > nums[index2]):
            index2 = j
    return nums[index1] * nums[index2]


if __name__ == "__main__":
    input_n = int(input())
    input_nums = [int(x) for x in input().split()]
    print(Product(input_nums))