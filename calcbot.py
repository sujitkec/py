'''
calcbot.py to do simple calculation
'''

from greet import *

greeting = greet_random()
quit_msg = ['quit', 'bye', 'exit']
print(greeting, "I am a calcbot.")

while True:
    msg = input()
    if msg in quit_msg:
        quit_choice = input("do you want to quit [y/n]?")
        if quit_choice == 'y':
            print('Bye...')
            break
    else:
        s = 0
        for i in msg.split():
            try:
                tmp = float(i)
                if "add" in msg:
                    s += tmp
                if "sub" in msg:
                    if s == 0:
                        s = tmp
                    else:
                        s -= tmp
                if "mul" in msg:
                    if s == 0:
                        s = tmp
                    else:
                        s *= tmp
                if "div" in msg:
                    if s == 0:
                        s = tmp
                    else:
                        s /= tmp
                if "sqr" in msg:
                    if s == 0:
                        s = tmp
                    else:
                        s = s ** tmp
            except:
                continue
        print(s)
