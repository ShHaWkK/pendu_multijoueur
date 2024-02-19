# game_logic.py

class Game:
    def __init__(self, word, max_attempts):
        self.word = word
        self.max_attempts = max_attempts
        self.attempts = 0
        self.guessed_letters = []

    def guess(self, letter):
        # Logique de vérification de la lettre devinée
        pass

    def is_game_over(self):
        # Vérifier si le jeu est terminé (le mot a été deviné ou le nombre maximal de tentatives a été atteint)
        pass

    def display_word(self):
        # Afficher le mot avec les lettres devinées
        pass

    def display_hangman(self):
        # Afficher l'image du pendu en fonction du nombre d'erreurs
        pass

if __name__ == "__main__":
    word_to_guess = "pendu"
    max_attempts = 6
    game = Game(word_to_guess, max_attempts)
    # Logique de gestion du jeu
