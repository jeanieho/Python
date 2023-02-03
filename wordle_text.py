# Name: Jeanie Ho
# UTEID: jth3929
#
# On my honor, <Jeanie Ho>, this programming assignment is my own work
# and I have not provided this code to any other student.

# secret words are actual answers, other valid words will not be picked
# method for when user enters guess, check if its in sercret or others, update data structure to hold letters player has guessed and unguessed
# while guess has not beeen create
import random
import string


def main():
    """ Plays a text based version of Wordle.
        1. Read in the words that can be choices for the secret word
        and all the valid words. The secret words are a subset of
        the valid words.
        2. Explain the rules to the player.
        3. Get the random seed from the player if they want one.
        4. Play rounds until the player wants to quit.
    """
    secret_words, all_words = get_words()
    welcome_and_instructions()
    final_word = random.choice(secret_words)
    play_again = play(final_word, all_words)
    while (play_again):
        final_word = random.choice(secret_words)
        play_again = play(final_word, all_words)


# def play(final_word, all_words):
#     """ Play a single round of Wordle.
#         1. Get the user's guess.
#         2. Check if the guess is valid.
#         3. Check if the guess is correct.
#         4. If the guess is correct, print a message.
#         5. Ask the user if they want to play again.
#         'y,y,200,bEESt,bEAst,YEAST,bEETS,bEsET,y,gAUNT,gAMERs,gAMER,AUNTs,gauge,gregs,great,tears,no i dont want to'
#     """
#     dict = {}
#     if (final_word[i] not in dict):
#         dict[final_word[i]] = 1
#     else:
#         dict[final_word[i]] += 1
#     alphabet = string.ascii_uppercase
#     found = False
#     prev_guesses = ''
#     tries = 0
#     while not found and tries < 6:
#         guess = input('\nEnter your guess. A 5 letter word: ').strip().upper()
#         if (guess not in all_words):
#             print('\n' + guess + ' is not a valid word. Please try again.')
#             continue
#         tries += 1
#         # make check a dictionary with the colors as keys and num times in final_word as values
#         check = ['-', '-', '-', '-', '-']
#         repeat = ''
#         repeat_o = ''
#         for i in range(len(guess)):
#             # remove guess[i] from alphabets
#             alphabet = alphabet.replace(guess[i], '')
#             # check if guess[i] is in alphabet to avoid duplicates
#             if (guess[i] == final_word[i]):
#                 check[i] = 'G'
#                 if (guess[i] in dict):
#                     dict[guess[i]] -= 1
#                 for j in range(i):
#                     if (guess[j] == guess[i]):
#                         check[j] = '-'
#                 repeat = final_word[i]
#             elif (guess[i] in final_word and guess[i] != final_word[i] and guess[i] != repeat and guess[i] != repeat_o):
#                 check[i] = 'O'
#                 repeat_o = guess[i]
#             elif (guess[i] == repeat or guess[i] == repeat_o):
#                 check[i] = '-'
#                 if (guess == final_word):
#                     check[i] = 'G'
#         prev_guesses += ('\n' + ''.join(check) + '\n' + guess)
#         print(prev_guesses)
#         print('\n' + "Unused letters: " + ' '.join(alphabet))
#         if (guess == final_word):
#             found = True
#     print_message(tries, found, final_word)
#     play_again = input('\nDo you want to play again? Type Y for yes: ').lower()
#     if (play_again == 'y'):
#         return True


def play(final_word, all_words):
    """ Play a single round of Wordle.
        1. Get the user's guess.
        2. Check if the guess is valid.
        3. Check if the guess is correct.
        4. If the guess is correct, print a message.
        5. Ask the user if they want to play again.
        'n,y,1313,oomph,orzos,mockoo,oTtoS,sHOOT,n'
        y,y,49,barbs,roara,roars,kites,kittens,knights,kribs,krocks,ricks,BRICk,nope
    """
    orig_dict = {}
    for i in range(len(final_word)):
        if (final_word[i] not in orig_dict):
            orig_dict[final_word[i]] = 1
        else:
            orig_dict[final_word[i]] += 1
    alphabet = string.ascii_uppercase
    found = False
    prev_guesses = ''
    tries = 0
    while not found and tries < 6:
        dict = {}
        for i in range(len(final_word)):
            if (final_word[i] not in dict):
                dict[final_word[i]] = 1
            else:
                dict[final_word[i]] += 1
        guess = input('\nEnter your guess. A 5 letter word: ').strip().upper()
        if (guess not in all_words):
            print('\n' + guess + ' is not a valid word. Please try again.')
            continue
        tries += 1
        # make check a dictionary with the chars as keys and num times in final_word as values
        check = ['-', '-', '-', '-', '-']
        for i in range(len(guess)):
            # remove guess[i] from alphabets
            alphabet = alphabet.replace(guess[i], '')
            # check if guess[i] is in alphabet to avoid duplicates
            if (guess[i] == final_word[i]):
                check[i] = 'G'
                dict[guess[i]] -= 1
                for j in range(i):
                    if (guess[j] == guess[i] and guess != final_word and dict[guess[i]] < 0):
                        check[j] = '-'
            elif (guess[i] in final_word and guess[i] != final_word[i] and dict[guess[i]] > 0):
                check[i] = 'O'
                dict[guess[i]] -= 1
        prev_guesses += ('\n' + ''.join(check) + '\n' + guess)
        print(prev_guesses)
        print('\n' + "Unused letters: " + ' '.join(alphabet))
        if (guess == final_word):
            found = True
    print_message(tries, found, final_word)
    play_again = input('\nDo you want to play again? Type Y for yes: ').lower()
    if (play_again == 'y'):
        return True


def print_message(tries, found, final_word):
    """ Print a message to the player. """
    if found:
        if tries == 1:
            print('\nYou win. Genius!')
        elif tries == 2:
            print('\nYou win. Magnificent!')
        elif tries == 3:
            print('\nYou win. Impressive!')
        elif tries == 4:
            print('\nYou win. Splendid!')
        elif tries == 5:
            print('\nYou win. Great!')
        elif tries == 6:
            print('\nYou win. Phew!')
    else:
        print('\nNot quite. The secret word was ' + final_word + '.')


def welcome_and_instructions():
    """
    Print the instructions and set the initial seed for the random
    number generator based on user input.
    """
    print('Welcome to Wordle.')
    instructions = input('\nEnter y for instructions, anything else to skip: ')
    if instructions == 'y':
        print('\nYou have 6 chances to guess the secret 5 letter word.')
        print('Enter a valid 5 letter word.')
        print('Feedback is given for each letter.')
        print('G indicates the letter is in the word and in the correct spot.')
        print('O indicates the letter is in the word but not that spot.')
        print('- indicates the letter is not in the word.')
    set_seed = input(
        '\nEnter y to set the random seed, anything else to skip: ')
    if set_seed == 'y':
        random.seed(int(input('\nEnter number for initial seed: ')))


def get_words():
    """ Read the words from the dictionary files.
        We assume the two required files are in the current working directory.
        The file with the words that may be picked as the secret words is
        assumed to be names secret_words.txt. The file with the rest of the
        words that are valid user input but will not be picked as the secret
        word are assumed to be in a file named other_valid_words.txt.
        Returns a sorted tuple with the words that can be
        chosen as the secret word and a set with ALL the words,
        including both the ones that can be chosen as the secret word
        combined with other words that are valid user guesses.
    """
    temp_secret_words = []
    with open('secret_words.txt', 'r') as data_file:
        all_lines = data_file.readlines()
        for line in all_lines:
            temp_secret_words.append(line.strip().upper())
    temp_secret_words.sort()
    secret_words = tuple(temp_secret_words)
    all_words = set(secret_words)
    with open('other_valid_words.txt', 'r') as data_file:
        all_lines = data_file.readlines()
        for line in all_lines:
            all_words.add(line.strip().upper())
    return secret_words, all_words


if __name__ == '__main__':
    main()
