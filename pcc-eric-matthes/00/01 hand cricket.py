import random
import time
import sys

hc_numbers = [1, 2, 3, 4, 5, 6]
# hc_numbers = [1,2,3,4,5,6,7,8,9,10,20] -> longer version 

def batfirst():
    print('\nYou\'re Batting now!')
    score = 0
    while True:
        print()
        user_bat = int(input('U : '))
        if user_bat in hc_numbers:
            cpu_bowl = random.choice(hc_numbers)
            print(f'CPU : {cpu_bowl}')
            if user_bat == cpu_bowl:
                print(f'You\'re OUT. You\'ve Scored {score} runs.')
                break
            else:
                score += user_bat
        else:
            print(f'You can only bat {hc_numbers}')
    bowlsecond(score)

def bowlsecond(score):
    print('\nYou\'re Bowling now!')
    print(f'Target Score for CPU is {score}')
    cpu_score = 0
    while cpu_score < score:
        print()
        user_bowl = int(input('U : '))
        if user_bowl in hc_numbers:
            cpu_bat = random.choice(hc_numbers)
            print(f'CPU : {cpu_bat}')
            if user_bowl == cpu_bat:
                print(f'You WIN ! The CPU only scored {cpu_score} runs.\n')
                tryagain = input('Do you want to try again? Y/N : ')
                if tryagain == 'Y' or tryagain == 'y':
                    main()
                else:
                    sys.exit('GGs!')
            else:
                cpu_score += cpu_bat
        else :
            print(f'You can only bowl {hc_numbers}')
    print (f'The CPU Scored {cpu_score} runs.')
    tryagain = input('You Lose. Do you want to try again? Y/N : ')
    if tryagain == 'Y' or tryagain == 'y':
        main()
    else:
        sys.exit('GGs!')

def bowlfirst():
    print('\nYou\'re Bowling now!')
    cpu_score = 0
    while True :
        print()
        user_bowl = int(input('U : '))
        if user_bowl in hc_numbers:
            cpu_bat = random.choice(hc_numbers)
            print(f'CPU : {cpu_bat}')
            if user_bowl == cpu_bat:
                print(f'The CPU is OUT ! The score to chase is {cpu_score}')
                break
            else:
                cpu_score += cpu_bat
        else :
            print(f'You can only bowl {hc_numbers}')
    batsecond(cpu_score)

def batsecond(cpu_score):
    print('\nYou\'re Batting now!')
    score = 0
    while score < cpu_score:
        print()
        user_bat = int(input('U : '))
        if user_bat in hc_numbers:
            cpu_bowl = random.choice(hc_numbers)
            print(f'CPU : {cpu_bowl}')
            if user_bat == cpu_bowl:
                print(f'You\'re OUT. You\'ve Scored {score} runs.')
                tryagain = input('You Lose. Do you want to try again? Y/N : ')
                if tryagain == 'Y' or tryagain == 'y':
                    main()
                else:
                    sys.exit('GGs!')
            else:
                score += user_bat
        else:
            print(f'You can only bat {hc_numbers}')
    tryagain = input('You Win !!! Do you want to try again? Y/N : ')
    if tryagain == 'Y' or tryagain == 'y':
        main()
    else:
        sys.exit('GGs!')

def main():
    print('\nWelcome to Hridyesh\'s Hand Cricket Game !!! ')
    choice = input('Heads or Tails ? : ')
    toss = ['h', 't']
    toss_result = random.choice(toss)
    print('Flipping Coin ...\n')
    time.sleep(2)
    
    if choice[0] == toss_result:
        user_win = input('You won the toss ! Do you want to bowl or bat ? ')
        if user_win[1].lower() == 'a':
            batfirst()
        elif user_win[1].lower() == 'o':
            bowlfirst()
        else:
            print('Invalid choice. Please enter "Bowl" or "Bat".')
            main()
    else:
        cpu_win_choice = ['Bat', 'Bowl']
        cpu_win = random.choice(cpu_win_choice)
        print(f'You lost the toss. The CPU has decided to {cpu_win}.')
        if cpu_win[1]== 'a':
            bowlfirst()
        elif cpu_win[1] == 'o':
            batfirst()

main()
