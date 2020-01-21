import random

random_num = random.randint(1,21)
print(random_num)
num_guesses = 0
name= input('hello what is your name? ')
print(name + ", am thinking of a number btn 1-30?. can you guess the number?")

while num_guesses < 5:
    guess = int(input('Guess a number: '))
    num_guesses += 1
    print(num_guesses)
    guessLeft = 5-num_guesses

    if guess < random_num:
        guessLeft=str(guessLeft)
        print('your guess is too low! you have '+guessLeft+' guesses left')

    elif guess > random_num:
        guessLeft=str(guessLeft)
        print('your guess is high! you have ' + guessLeft+' guesses left')
    else:
        pass
        break

if guess == random_num:
    num_guesses=str(num_guesses)
    print('good job!!! you guessed correct')
elif guess!=random_num:
    random_num=str(random_num)
    print('sorry. the no i was thinking of was '+random_num+" :)")

