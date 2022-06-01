import random
number = random.randint(1,9)

print ('guess a number between 1 and 9')
chance = 0
while chance < 5:
    guess = int (input('enter guess'))
    if guess == number:
        print('congrates, you are lucky')
        break
    elif guess < number:
        print('you have guessed a lower number,guess a higher number')
    else:
        print('you have guessed a higher number,guess a lower number')
    chance = chance +1 
if not chance <5:
    print ('you lost')

