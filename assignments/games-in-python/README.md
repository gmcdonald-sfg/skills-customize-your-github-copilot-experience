# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic word-guessing game using Python strings, loops, and user input.

## 📝 Tasks

### 🛠️ Build a Hangman Game

#### Description
Create a Hangman game where players guess letters to reveal a hidden word before running out of attempts.

**Skills practiced:** String manipulation, loops, conditionals, random selection

#### Requirements
Completed program should:

- Randomly select words from a predefined list
- Accept letter guesses and show current progress (_ _ _ format)
- Track incorrect guesses remaining
- End when word is guessed or attempts exhausted
- Display win/lose messages

#### Example Input
```python
# Word list your program should use
word_list = ["python", "coding", "hangman", "computer", "keyboard"]
```

#### Example Output
```
Welcome to Hangman!
Word: _ _ _ _ _ _
Guesses remaining: 6

Enter a letter: e
Good guess!
Word: _ _ _ _ e _
Guesses remaining: 6

Enter a letter: a
Good guess!
Word: _ _ _ _ e a
Guesses remaining: 6

Enter a letter: z
Wrong! Try again.
Word: _ _ _ _ e a
Guesses remaining: 5
```
