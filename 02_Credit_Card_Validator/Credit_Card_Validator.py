def luhn_check(number):
    """
    Applies the Luhn algorithm to a 16-digit number.
    Returns True if the number is valid, otherwise False.
    """

    total_sum = 0

    for i in range(16):
        digit = int(number[i])

        # Double every second digit starting from the first position
        if i % 2 == 0:
            digit *= 2

            # If the result has two digits, add them together
            if digit > 9:
                digit = digit // 10 + digit % 10

        total_sum += digit

    return total_sum % 10 == 0


def is_valid_number(s):
    """
    Checks whether the given number follows the required format
    and passes the Luhn validation.
    
    Accepted formats:
    - 16 consecutive digits
    - 4 groups of 4 digits separated by spaces
    - 4 groups of 4 digits separated by hyphens
    """

    s = s.strip()

    # Remove separators if the number is written in groups
    if len(s) == 19:

        if s[4] == " " and s[9] == " " and s[14] == " ":
            s = s.replace(" ", "")

        elif s[4] == "-" and s[9] == "-" and s[14] == "-":
            s = s.replace("-", "")

        else:
            return False

    # The final number must contain exactly 16 digits
    elif len(s) != 16:
        return False

    # Check that all characters are digits
    if not s.isdigit():
        return False

    # The first digit must be between 4 and 7
    if int(s[0]) < 4 or int(s[0]) > 7:
        return False

    return luhn_check(s)


def main():
    """
    Reads numbers from set4.txt and counts valid entries
    """

    numbers_sum = 0
    lines_sum = 0

    try:
        with open("credit_card_numbers.txt", "r") as file:

            for line in file:
                line = line.strip()

                lines_sum += 1

                if is_valid_number(line):
                    numbers_sum += 1

    except FileNotFoundError:
        print("\nError: credit_card_numbers.txt was not found in the current directory.")
        return

    print("\nLines_Sum =", lines_sum)
    print("Numbers_Sum =", numbers_sum)


if __name__ == "__main__":
    main()