#  CLI Quiz Game Application

An interactive, terminal-based quiz game built in Python. Test your knowledge across multiple categories, track your speed with a built-in timer, and get instant feedback on your performance!

---

##  Features

- ** External JSON Data Storage:** Questions and categories are loaded dynamically from a `questions.json` file, making it easy to add or modify content without changing the code.
- ** Randomized Questions:** Uses Python's `random.shuffle()` to mix up the question order every time you play.
- ** Response Timer:** Measures how long you take to answer each question using the `time` module.
- ** Robust Error Handling:** Implements `try/except` blocks to handle invalid choices (anything outside A, B, C, D) or empty inputs gracefully without crashing the program.
- ** Scoring & Feedback:** Calculates your final score percentage and provides tailored performance feedback (*"Excellent"*, *"Good"*, or *"Try Again"*).
- ** Category Selection:** Choose between different quiz tracks (e.g., Python Programming, General Knowledge).

---

##  Project Structure

```text
cli-quiz-game/
│
├── quiz_game.py       # Main Python script containing game logic
├── questions.json     # External database holding categories and questions
└── README.md          # Project documentation

# Getting Started
Prerequisites
Make sure you have Python 3.x installed on your system.

## Installation & Running
  1. Download or clone this repository to your local machine.

  Repository link;

  ```
  https://github.com/Derroww/Quiz_game.git

  ```

  2. Ensure both quiz_game.py and questions.json are in the same directory.

  3. Open your terminal, and run the script:

# Built With
Python (Standard Library modules: json, random, time)


# License

This project is open-source software licensed under the MIT License.



