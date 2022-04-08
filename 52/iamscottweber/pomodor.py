from datetime import datetime, timedelta
import time as time
from random import randint
from playsound import playsound
from pathlib import Path


def start_pomodoro():
	print(f'\n--------------HOW TO USE THIS POMODORO TIMER----------------\n'
		f'Work until the Pomodoro rings\n'
		f'Take a short break (5 minutes)\n'
		f'After 3 Pomodoros (One Set), you get a longer break! (15–30 minutes).\n'
        f'How many sets do you want?')
	amount_of_loops(int(input()))

def amount_of_loops(sets):
    count = 0
    for set in range(sets):
        count += 1
        for i in range(3):
            work_time = randint(20,25)
            print(f'Get started! This Pomodoro is {work_time} minutes. Counting down now!')
            play_sound('Time to Work')
            start_timer(work_time)
            print('Time to take a short five minute break!')
            play_sound('Finish')
            start_timer(5)
        long_break_time = randint(15,30)
        if count < sets: # avoid adding a break on last set
            print(f'Time to take a long {long_break_time} minute break!')
            play_sound('Finish')
            start_timer(long_break_time)
    play_sound('Finish')
    print('All done! Great job!')

def start_timer(Minutes):
    timer = timedelta(seconds=Minutes)
    while timer:
        print(f'{str(timer)} left...')
        time.sleep(1)
        timer -= timedelta(seconds=1)
    print('Time is up!')

def play_sound(method):
    if method == 'Finish':
        playsound('applause.mp3')
    elif method == 'Time to Work':
        playsound('back_to_work.mp3')

if __name__ == '__main__':
    start_pomodoro()