ROMAN_VALUES = {
    "MMM": 3000,
    "MM": 2000,
    "M": 1000,
    "CM": 900,
    "DCCC": 800,
    "DCC": 700,
    "DC": 600,
    "D": 500,
    "CD": 400,
    "CCC": 300,
    "CC": 200,
    "C": 100,
    "XC": 90,
    "LXXX": 80,
    "LXX": 70,
    "LX": 60,
    "L": 50,
    "XL": 40,
    "XXX": 30,
    "XX": 20,
    "X": 10,
    "IX": 9,
    "VIII": 8,
    "VII": 7,
    "VI": 6,
    "V": 5,
    "IV": 4,
    "III": 3,
    "II": 2,
    "I": 1,
}


# Converts an integer number to Roman numeral format
def to_roman(number):

    roman_number = ""

    for symbol, value in ROMAN_VALUES.items():

        # Determine how many times the current Roman symbol can be used
        count = number // value

        if count != 0:
            roman_number += symbol * count
            number -= count * value

    return roman_number


# Converts a Roman numeral string to an integer
def from_roman(roman_number):

    decimal_number = 0
    index = 0

    while index < len(roman_number):

        # Check if a two-character Roman symbol exists (e.g. IV, IX, CM)
        if (
            index + 1 < len(roman_number)
            and roman_number[index : index + 2] in ROMAN_VALUES
        ):
            decimal_number += ROMAN_VALUES[roman_number[index : index + 2]]
            index += 2

        elif roman_number[index] in ROMAN_VALUES:
            decimal_number += ROMAN_VALUES[roman_number[index]]
            index += 1

        else:
            raise ValueError("Invalid Roman numeral.")

    return decimal_number


# Counts how many integers produce Roman numerals longer than 7 characters
def count_large_integers(filename):

    count = 0

    with open(filename, "r") as file:

        for line in file:
            number = int(line.strip())

            if len(to_roman(number)) > 7:
                count += 1

    return count


# Counts how many Roman numerals represent numbers divisible by 7
def count_divisible_romans(filename):

    count = 0

    with open(filename, "r") as file:

        for line in file:
            roman_number = line.strip()

            if from_roman(roman_number) % 7 == 0:
                count += 1

    return count


def main():

    # Example conversions
    print("\n=== Roman Numerals Example Conversions ===")
    print("\n3948 in Roman numerals:", to_roman(3948))
    print("MDCCLXII in decimal:", from_roman("MDCCLXII"))

    try:
        integers_count = count_large_integers("integers.txt")
        roman_count = count_divisible_romans("roman_numerals.txt")

        print("\n\n=== File Analysis Results ===")
        print("\nRoman numerals with more than 7 characters:", integers_count)
        print("Roman numerals divisible by 7:", roman_count)

    except FileNotFoundError as error:
        print(f"\nError: {error.filename} was not found.")


# Start the program
if __name__ == "__main__":

    main()
