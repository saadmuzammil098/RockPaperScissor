# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 13:58:55 2019

@author: SaadMuzammil
"""

import random
def play():
    user = input ("'r'  for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        return 'tie'
    if is_win(user, computer):
        return 'You Won'
    
    return 'You lost'

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True
    

print(play())
