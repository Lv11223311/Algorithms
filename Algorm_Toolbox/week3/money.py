# using python3 

def money_change(n):
    tens = n // 10
    res = n % 10
    fives = res // 5
    ones = n % 5
    result = tens + fives + ones
    return result

if __name__ == "__main__":
    input_n = int(input())
    print(money_change(input_n))