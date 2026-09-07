def greaterThanXNum(numbers, x):
    count = 0
    for num in numbers:
        if num > x:
            count += 1
    print(count)

numbers = [10, 5, 20, 8, 30, 15]
greaterThanXNum(numbers, 12)
