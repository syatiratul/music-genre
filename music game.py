#!/usr/env python

import random

def MusicGenre():
    """Start a music genre guessing game."""
    print("Guess the music genre!")
    max_trials = 5
    trials = 0
    
    music = [
        "popular",
        "country",
        "rock",
        "techno",
        "classic",
        "islamic",
        "rap",
        "jazz"
        ]
    
    x = random.choice(music)
    guess = None
    
    while trials < max_trials:
    
        guess = str(input("What is my favourite music genre?"))
        trials += 1
        
        if x == guess:
            print("You get it right!")
            print("Congratulation.You got the answer!")
            
        else:
            print("Try again!")
    else:
        print("Game End")
                      
MusicGenre()