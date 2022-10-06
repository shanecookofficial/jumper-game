class Player():

    def __init__(self):
        self.__lives = 4
        self.__guess = None

    def get_lives(self):
        return self.__lives

    def remove_life(self):
        self.__lives -= 1

    def set_guess(self, guess):
        self.__guess = guess

    def get_guess(self):
        return self.__guess