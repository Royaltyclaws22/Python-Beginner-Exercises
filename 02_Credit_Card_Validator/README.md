# 💳 Credit Card Validator

A simple Python program that checks whether a given 16-digit credit card number is valid using the Luhn algorithm.


## 🔎 Preview
<img width="1280" height="679" alt="Credit_Card_Validator" src="https://github.com/user-attachments/assets/58c18dc7-b79f-4c9e-86a0-d258ce5d7b74" />


## ⚙️ Features

- Accepts 16-digit integer credit card numbers.
- Supports numbers entered with spaces or hyphens between every group of four digits.
- Removes separators before performing validation.
- Checks that the first digit is between 4 and 7.
- Doubles the digits in the odd positions (1st, 3rd, 5th, ..., 15th).
- Converts doubled two-digit results into single digits by adding their digits together.
- Calculates the final digit sum and checks whether it is a multiple of 10.
- Reads multiple credit card numbers from an input file and counts the valid ones.


## 💻 Installation & Running

1. Clone the repository:
```bash
git clone https://github.com/Royaltyclaws22/Python-Beginner-Exercises.git
```
2. Navigate to the project folder:
```bash
cd Python-Beginner-Exercises/02_Credit_Card_Validator
```
3. Run the program:
```bash
python Credit_Card_Validator.py
```

Make sure that the input file `credit_card_numbers.txt` is located in the same directory as `Credit_Card_Validator.py`.


## 💡 Usage

Place the credit card numbers you want to validate inside `credit_card_numbers.txt`.

Run the program. It will display:
- The total number of processed lines
- The number of valid credit card numbers

**Example:**

```text
Lines_Sum = 100
Numbers_Sum = 85
```
