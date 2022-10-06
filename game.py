from display import Display
from word import Word
from player import Player
def main():

    #objects
    display = Display()
    word = Word()
    player = Player()

    #globals
    game_loop = False

    #secret word
    word.set_words('words.txt')
    word.set_word()
    word.set_empty_word()

    #start display
    display.print_visual()

    #game loop
    while game_loop == False:
        if game_loop == False:
            print()
            print('_ _ _ _ _')
            print()
            player.set_guess(input('Guess a letter [a-z]: '))
            print()
            if isinstance(player.get_guess(),str):
                if len(player.get_guess()) == 1:
                    correct = 0
                    for letter in word.get_word():
                        if letter == player.get_guess():
                            correct += 1
                    if correct > 0:
                        word.update_empty_word(player.get_guess())
                        print(word.gen_string(word.get_empty_word()))
                        print()
                        display.print_visual()
                        if word.get_empty_word() == word.get_word():
                            print()
                            print('You win!')
                            game_loop = True
                    else:
                        player.remove_life()
                        print(word.gen_string(word.get_empty_word()))
                        print()
                        display.update_visual()
                        display.print_visual()
                        if player.get_lives() == 0:
                            print()
                            print('You loose!')
                            print(f'The word was "{word.gen_string(word.get_word(),"")}".')
                            game_loop = True
                else:
                    print('Make sure your guess is one letter.')
            else:
                print('Make sure your guess is one letter.')

if __name__ == '__main__':
    main()