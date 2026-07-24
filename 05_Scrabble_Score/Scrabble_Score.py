# Dictionary containing the Scrabble point value for each English letter
LETTER_POINTS = {
    "A": 1,
    "B": 3,
    "C": 3,
    "D": 2,
    "E": 1,
    "F": 4,
    "G": 2,
    "H": 4,
    "I": 1,
    "J": 8,
    "K": 5,
    "L": 1,
    "M": 3,
    "N": 1,
    "O": 1,
    "P": 3,
    "Q": 10,
    "R": 1,
    "S": 1,
    "T": 1,
    "U": 1,
    "V": 4,
    "W": 4,
    "X": 8,
    "Y": 4,
    "Z": 10,
}


def scrabble_points(word):
    """
    Calculate the Scrabble score of an English word.
    Letters that are not found in the dictionary contribute 0 points.
    """
    word = str(word).upper()
    return sum(LETTER_POINTS.get(letter, 0) for letter in word)


def main():

    print("\n=== Scrabble Score Analysis ===")

    # Example test
    print("\nScrabble score of all alphabet letters:")
    print(scrabble_points("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    # Read all words from the input file
    try:
        with open("english_words.txt", "r", encoding="utf-8") as file:
            words = [line.strip() for line in file]

    except FileNotFoundError:
        print("\nError: The file 'english_words.txt' was not found.")
        return

    except OSError:
        print("\nError: The file could not be opened.")
        return

    # Store each word together with its Scrabble score
    scores = [(scrabble_points(word), word) for word in words]

    # Calculate the total score of all words
    total_score = sum(score for score, _ in scores)
    print("\nTotal Scrabble score of all words:")
    print(total_score)

    if not scores:
        print("\nError: The file does not contain any words.")
        return

    # Find the word with the highest score
    highest_score = max(scores)
    print("\nWord with the highest Scrabble score:")
    print(f"{highest_score[1]} ({highest_score[0]} points)")

    # Count how many words have exactly 29 points
    number_of_words = sum(score == 29 for score, _ in scores)
    print("\nNumber of words with exactly 29 points:")
    print(number_of_words)


# Start the program
if __name__ == "__main__":
    main()
