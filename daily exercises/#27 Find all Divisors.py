# write a function to find all the divisors of a number.
# Expected : [1, 2, 3, 4, 6, 12]

def findDivisors(num):
    # using list comprehension
    result = [i for i in range(1, num+1) if num % i == 0]
    return result
    # for i in range(1, num+1):
    #     if num % i == 0:
    #         print(i)
    # return i

print(findDivisors(12))