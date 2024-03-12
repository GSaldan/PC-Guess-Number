import random
# instructions: pick a number and the computer will try to guess your number, if it guesses higher type h, 
# if it guesses lower type l, and if it guesses correctly type c.


player_number = int(input('Enter a whole positive number: '))


def computer(x):
    tries = 1
    low = 1
    high = x
    player = ''

    while player != 'c':
        guess = random.randint(low, high)
        player = input(f'Is {guess} high (H), low (L) or correct (C)?: '.lower())
        if player == 'h':
            high = guess - 1
            tries += 1
        elif player == 'l':
            low = guess + 1
            tries += 1
        elif player == 'c':
            print(f'The computer guessed your number, {guess}, correctly in {tries} tries!!')
        else:
            print('Please answer with h, l or c')


# feed the function with the player_number for the high variable
computer(player_number)