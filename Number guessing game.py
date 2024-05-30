import random
def computer_guess(x):
    low=1
    high=x
    feedback=""
    guess=0
    while feedback!='c':
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low
        feedback=input(f'Is number {guess} too High ("H"), too Low ("L"), or Correct ("C"). Enter your feedback :').lower()
        if feedback=='h':
            high=guess-1
        elif feedback=='l':
            low=guess+1
    print(f'Yaay! Computer has guessed the number {guess} correctly')
computer_guess(1000)
