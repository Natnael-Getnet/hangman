import requests
import art

# url = "https://random-word-api.herokuapp.com/word"
#
# response = requests.get(url=url)
# word = response.json()[0]
word = 'word'


def play_game():
    is_over = input('Hello, do you want to play hangman? (Y) or (N)')
    while is_over.lower() == 'y':
        word_length = len(word)
        dash = ['_' for _ in range(word_length)]
        print(word)
        hangman_count = len(art.HANGMANPICS)
        get_word = 0
        won = True
        fail = 0
        while hangman_count != 0:
            print(''.join(dash))
            guess = input('Guess the letter.')
            index = 0
            find = False
            for char in word:
                if char == guess and char not in dash:
                    get_word += 1
                    find = True
                    dash[index] = guess
                elif char == guess and char in dash:
                    find = True
                    print('Already guessed the letter!!!')
                index += 1
            if not find:
                print(art.HANGMANPICS[fail])
                fail += 1
                hangman_count -= 1
            if hangman_count == 0:
                won = False
            if get_word == word_length:
                break
        if won:
            print('You won. Saved your man!!! :)')
        else:
            print('You lost your man. :(')
        is_over = input('Do you want to play hangman again? (Y) or (N)')


play_game()
