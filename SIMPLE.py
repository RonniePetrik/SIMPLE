#!/usr/bin/python
import random
import string
def coin_collector():
    print("This is the game")
print('                                                                                    ____________________________________________________________')
print('                                                                                   |                                                           |')
print('                                                                                   |        Welcome to SIMPLE, Basic Operating System          |')
print('                                                                                   |                                                           |')
print('                                                                                   |                 version 0.0.0.0.1                         |')
print('                                                                                   |                                                           |')
print('                                                                                   |             Original Release:2/23/2025                    |')
print('                                                                                   |            Last Major Update:1/2/2025                     |')
print('                                                                                   |           Read User Manual (type \'help\')                |')
print('                                                                                   |                                                           |')
print('                                                                                   |                                                           |')
print('                                                                                   |                                                           |')
print('                                                                                   |                                                           |')
print('                                                                                   |                                                           |')
print('                                                                                   |                                                           |')
print('                                                                                   |___________________________________________________________|')
print('\n\n\n')


while True:
    input_mode = input('MM>')  #change input mode
    if input_mode == 'A':     #if typed 'A'
        input_mode_a = input('A>>')  #switched to input mode 'A'
        if input_mode_a == 'random_numb':     #if typed random_numb
            random_numb = random.randrange(0, 100)   #generate a random number
            random_numb_2 = random.randrange(0, 1000)  #generate a random number
            print(random_numb)   #print a random number between 1 and 100
        elif input_mode_a == 'random_numb_2':
            print(random_numb_2)
        elif input_mode_a == 'note':       #unfinished
            type_1 = input('TYPE NOTE HERE--')
        elif input_mode_a == 'show_note':
            print('\n\n\n\n\n')
            print(type_1)               #print what was typed
        elif input_mode_a == 'note_2':
            type_2 = input('TYPE NOTE 2 HERE--')
        elif input_mode_a == 'show_note_2':
            print('\n\n\n\n\n')
            print(type_2)
        else:  
            print('SYNTAX ERROR, MISTYPE?')
    elif input_mode == 'B':
        input_mode_b = input('B>>>')
    elif input_mode == 'C':
        input_mode_c = input('C>>>>')
        if input_mode_c == 'simplegame_coincollector':
            coin_collector()
        elif input_mode_c == 'simplegame_shootthefruit':
            pass
        else:
            print('Error, No such command')
    else:
        print('No such input!')
                
        
