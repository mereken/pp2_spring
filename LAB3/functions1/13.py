import random
def guess():
    print('Hello! What is your name?')
    
    name = input()
    
    print('Well, ', name, ' , I am thinking of a number between 1 and 20.')
    print('Take a guess.')
    
    m = 0
    random_number = random.randint(1, 20)
    while True:
        x = int(input())
        if x == random_number:
            m += 1 
            print('Good job,', name, '! You guessed my number in', m, 'guesses!')
            break
        else:
            m += 1
            if x < random_number:
                print('Your guess is too low.')
            else:
                print('Your guess is too high.')
            print('Take a guess.')
guess()