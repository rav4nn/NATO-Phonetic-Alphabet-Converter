NATO Phonetic Alphabet Converter

A simple Python project that converts any user‑entered word or name into its corresponding NATO phonetic alphabet representation.

For example:
```
Input: Hardeep
Output: ['Hotel', 'Alfa', 'Romeo', 'Delta', 'Echo', 'Echo', 'Papa']
```

---

📌 Project Overview

This project:

- Takes a word or name as input from the user
- Reads NATO phonetic data from a CSV file
- Converts each letter into its NATO phonetic code word
- Outputs the result as a Python list

It’s a beginner‑friendly project that demonstrates:

- File handling with CSVs
- Dictionary comprehension
- List comprehension
- Basic use of the pandas library

---

📂 Project Structure
```
.
├── main.py
├── nato_phonetic_alphabet.csv
└── README.md
```

---

▶️ How to Run the Project

Clone the repository:

git clone https://github.com/your-username/nato-phonetic-alphabet.git
cd nato-phonetic-alphabet

Install dependencies:
```
pip install pandas
```
Run the script:
```
python main.py
```
Enter a word or name when prompted.

---

🧠 How It Works

- The program reads the CSV file using pandas
- Converts the data into a dictionary like:
```
{"A": "Alfa", "B": "Bravo", ...}
```
- Takes user input and converts it to uppercase
- Maps each letter to its NATO phonetic equivalent

---

🚀 Possible Improvements

- Handle invalid characters (numbers, symbols, spaces)
- Add error handling for missing CSV files
- Convert output into a formatted string instead of a list
- Build a GUI or web version

