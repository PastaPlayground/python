def binary_to_decimal(binary_str):
    decimal = 0
    # get the highest power in the binary string
    power = len(binary_str) - 1
    for digit in binary_str:
        # if digit = 1, get decimal value with 2 ** power
        if digit == '1':
            decimal += 2 ** power

        # reduce power for next digit
        power -= 1
    return decimal


def decimal_to_binary(decimal):
    binary_str = ""
    if decimal == 0:
        return "0"
    while decimal > 0:
        remainder = decimal % 2
        binary_str = str(remainder) + binary_str
        decimal = decimal // 2
        print(binary_str, decimal)
    return binary_str

# 33
# remainder: 33 % 2 = 1
# binary str: 1
# decimal: 33 // 2 = 16

# remainder: 16 % 2 = 0
# binary str: 01
# decimal: 16 // 2 = 8

# remainder: 8 % 2 = 0
# binary str: 001
# decimal: 8 // 2 = 4

# remainder: 4 % 2 = 0
# binary str: 0001
# decimal: 4 // 2 = 2

# remainder: 2 % 2 = 0
# binary str: 00001
# decimal: 2 // 2 = 1

# remainder: 1 % 2 = 1
# binary str: 100001
# decimal: 1 // 2 = 0


def main():
    while True:
        print("Choose an option:")
        print("1. Convert Binary to Decimal")
        print("2. Convert Decimal to Binary")
        print("3. Quit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            binary_str = input("Enter a binary number: ")
            decimal = binary_to_decimal(binary_str)
            print(f"Decimal: {decimal}")
        elif choice == '2':
            decimal = int(input("Enter a decimal number: "))
            binary_str = decimal_to_binary(decimal)
            print(f"Binary: {binary_str}")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
