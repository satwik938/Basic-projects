import random
def play():
    while True:
        comp=random.choice(['r','p','s'])
        user=input("What's your choice, 'r' for Rock, 's' for Scissors, 'p' for Paper, 'stop' to stop playing :").lower()
        if user=='stop':
            break
        if user==comp:
            print(f'Computer : {comp}',f'You : {user}\n',"It's a tie!")
        elif is_win(user,comp):
            print(f'Computer : {comp}',f'You : {user}\n',"yaay, you won!")
        else:
            print(f'Computer : {comp}',f'You : {user}\n',"You lost!")
    return "Game stopped"
def is_win(player,computer):
    if (player=='r' and computer=='s') or (player=='p' and computer=='r') or (player=='s' and computer=='p'):
        return True
print(play())
