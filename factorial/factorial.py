# counting factorial with recursion


# def factorial(x):
#     # 0! = 1
#     total = 1

#     # run loop till condition is met
#     while x > 0:
#         # total = 5
#         # x = 5
#         total *= x

#         # 5*4*3*2*1
#         x -= 1
#     print(total)


tests = [-1, 1, 2, 3, 4, 5, 6]


def factorial(n):
    # factorial starts from 0!
    if n > -1:
        if n == 0:
            return 1
        else:
            # n = 5
            # 5 * (5-1) * (5-2) * (5-3) * (5-4)
            return n * factorial(n - 1)
    else:
        return "Negative"


for test in tests:
    # do not use print in recursion
    # values need to be saved and used again
    print(factorial(test))
