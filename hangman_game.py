import random

# Hangman stages as ASCII art
HANGMAN_STAGES = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """
]

# List of possible words (you can expand this)
WORDS = ["python", "hangman", "challenge", "programming", "artificial"]

def play_hangman():
    # Select a random word
    word = random.choice(WORDS).upper()
    word_letters = set(word)  # Unique letters in the word
    guessed_letters = set()   # Letters the player has guessed
    attempts = 6              # Number of incorrect guesses allowed
    
    # Display initial state
    display_word = ["_" if letter.isalpha() else letter for letter in word]
    
    print("Welcome to Hangman!")
    print("====================:)")
    print(f"The word has {len(word)} letters.")
    
    # Game loop
    while attempts > 0 and set(display_word) != set(word):
        print(HANGMAN_STAGES[6 - attempts])
        print(f"Attempts left: {attempts}")
        print("Word: " + " ".join(display_word))
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) or 'None'}")
        
        # Get player's guess
        guess = input("Guess a letter: ").upper()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        # Check if letter was already guessed
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        
        guessed_letters.add(guess)
        
        # Check if guess is in the word
        if guess in word_letters:
            print("Good guess!")
            for i, letter in enumerate(word):
                if letter == guess:
                    display_word[i] = guess
        else:
            print("Incorrect guess!")
            attempts -= 1
    
    # Game over
    if attempts > 0:
        print(HANGMAN_STAGES[6 - attempts])
        print("Congratulations! You won!")
        print(f"The word was: {word}")
    else:
        print(HANGMAN_STAGES[6])
        print("Game Over! You lost.")
        print(f"The word was: {word}")

# Start the game
if __name__ == "__main__":
    play_hangman()