from random import choice
import subprocess as sp

random_words = ['tiger','ocean', 'mississippi', 'xylophone', 'death', 'water', 'bubble', 'table', 'christmas', 'fire', 'cried', 'father']
guessed = set()
guessed_right = set()
got_wrong = 0


def buildman(strikes):
    row1 = ['   ', ' O ', ' O ', ' O ', ' O ', ' O ', ' O ']
    row2 = ['   ', '   ', ' | ', '/| ', '/|\\', '/|\\', '/|\\']
    row3 = ['   ', '   ', '   ', '   ', '   ', '/  ', '/ \\']
    print('_____')
    print('| ', end='')
    print(row1[strikes])
    print('| ', end='')
    print(row2[strikes])
    print('| ', end='')
    print(row3[strikes])


def round():
    global got_wrong
    for char in word:
        if char in guessed_right:
            print(char, end=' ')
        else:
            print('_', end=' ')
    print()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char in guessed:
            print(' ', end=' ')
        else:
            print(char, end=' ')
    print()
    guess = validate(input('Guess a letter: ').lower(), True)
    guessed.add(guess)
    if guess in word:
        guessed_right.add(guess)
    else:
        got_wrong += 1


def validate(item, isguess):
    if not item.isalpha():
        validate(input('Invalid character, guess again: '), isguess)
    if item in guessed:
        validate(input('Letter already guessed, guess again: '), isguess)
    if isguess and len(item) > 1:
        validate(input('Guess to long, guess again: '), isguess)
    return item


def won():
    return all([char in guessed_right for char in word])


sp.call('clear', shell=True)
if input('Do you want a random word? ') == 'yes':
    word = choice(random_words)
else:
    word = validate(input('Enter Word: ').lower(), False)

buildman(got_wrong)
while not won() and got_wrong < 6:
    if got_wrong >= 6:
        print(word)
        print('You lost!')
    else:
        sp.call('clear', shell=True)
        buildman(got_wrong)
        round()
        if won():
            sp.call('clear', shell=True)
            buildman(got_wrong)
            print(word)
            print('You Won!')