from Parameters import s, e
from mixer import jumbler
from random import shuffle

def values():
    answer = jumbler[0]
    return answer

def game():
    solution = values()
    while True:
        print(f'Guess a number between{s} and {e-1}, or press X to give up.')
        task = input()
        if task.upper() == 'X':
            break
        elif int(task) == solution:
            print('Great job, you got it!')
            break
        else:
            print('you are trash!')
            continue
    while True:
        check = input('Type "y" to play again. or "any other key" to leave.')
        if check.upper() == 'Y':
            print('Well I do not want to play again. You smell, bye!')
            break
        elif check.upper() == 'ANY OTHER KEY':
            print('Way to follow instructions, have a star! *')
            break
        else:
            print('I said type"any other key" idiot!')
            break






game()




