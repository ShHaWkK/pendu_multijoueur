# game_logic.py

class Game:
    def __init__(self, word, max_attempts):
        self.word = word
        self.max_attempts = max_attempts
        self.attempts = 0
        self.guessed_letters = []

    def guess(self, letter):
        if letter in self.word and letter not in self.guessed_letters:
            self.guessed_letters.append(letter)
            return True
        else:
            self.attempts += 1
            return False

    def is_game_over(self):
        return self.attempts >= self.max_attempts or all(letter in self.guessed_letters for letter in self.word)

    def display_word(self):
        return ''.join(letter if letter in self.guessed_letters else '_' for letter in self.word)

    def display_hangman(self):
        return f"assets/hangman_images/img-{self.attempts}.png"


if __name__ == "__main__":
    word_to_guess = "pendu"
    max_attempts = 6
    game = Game(word_to_guess, max_attempts)

    while not game.is_game_over():
        print(game.display_word())
        print(game.display_hangman())
        guess = input("Devinez une lettre: ").strip().lower()
        if not guess or len(guess) > 1:
            print("Veuillez entrer une seule lettre.")
            continue
        success = game.guess(guess)
        if success:
            print("Bonne lettre!")
        else:
            print("Mauvaise lettre.")

    if all(letter in game.guessed_letters for letter in game.word):
        print("Félicitations! Vous avez trouvé le mot:", game.word)
    else:
        print("Dommage! Le mot était:", game.word)
        print(game.display_hangman())
