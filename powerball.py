# lottery powerball
# guessing odds using factorials

from math import factorial as fact

# 69/5 * 68/4 * 67/3 * 66/2 *65/1 * 26
# (69! / 5!(69-5)!) *26


def odds(balls, pick, power=False):
    print(
        "Enter number of balls, number of balls picked, and if they are using powerball, you will be asked for the number of powerballs"
    )
    # false
    p_ball = 1

    # true
    if power:
        p_ball = int(input("Enter number of powerballs: "))

    return (fact(balls)) / (fact(5) * fact(balls - pick)) * p_ball


print(f"{odds(50, 5):,}")
