import random
b = ['rock', 'paper', 'scissors']
win = 0
com_win = 0
round = 0
draw = 0
while True:
    a = random.randint(0,2)
    c = b[a]
    d = input('rock, paper, scissors or q to quit:')
    if(d=='q'):
        break
    elif(d in b):
        print('Computer:',c)
        if(d==c):
            print('Draw!')
            draw+=1
        elif(d=='rock' and c=='scissors'):
            print('You win!')
            win+=1
        elif(d=='paper' and c=='rock'):
            print('You win!')
            win+=1
        elif(d=='scissors' and c=='paper'):
            print('You win!')
            win+=1
        else:
            print('You lost!')
            com_win+=1
        round+=1
    else:
        print('Invalid choice')
print('You won',win,',the computer won',com_win,'draws:',draw)