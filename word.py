import random
class Word():

    def __init__(self):
        self.__word = []
        self.__words = []
        self.__empty_word = []

    def set_words(self,file_name):
        with open(file_name) as file:
            for item in file:
                item = item.strip()
                self.__words.append(item)

    def get_words(self):
        return self.__words

    def gen_num(self):
        return random.randint(1,len(self.get_words()))

    def set_word(self):
        for letter in self.__words[self.gen_num()-1]:
            self.__word.append(letter)

    def get_word(self):
        return self.__word

    def set_empty_word(self):
        for letter in self.__word:
            self.__empty_word.append('_')

    def get_empty_word(self):
        return self.__empty_word

    def update_empty_word(self,guess):
        i = 0
        for letter in self.__word:
            if guess == letter:
                self.__empty_word[i] = letter
            i += 1

    def gen_string(self, list, x=' '):
        return x.join(list)