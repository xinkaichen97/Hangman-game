import random


def hangman():
    #words = ['ubiquitous', 'reciprocal']
    #word = random.choice(words)
    word = input('Enter the word: ')
    counts = 5
    display = ''
    l = len(word)
    for i in range(l):
        display += '_'
    print('The word has', l, 'letters:',display)
    while counts > 0:
        if display.find('_') == -1:
            print('You win!')
            return
        print('Enter a letter: ', end='')
        t = input()
        if t in word:
            str = list(display)
            for i in range(l):
                if word[i] == t:
                    str[i] = word[i]
                    display = "".join(str)
            print('Congrats! Now the word:', display)
        else:
            counts -= 1
            print(t, 'is not in this word. You have', counts, 'chances left.')
    print('You lose! The word is', word)

hangman()