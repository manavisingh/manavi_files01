#!/usr/bin/python
# -*- coding: utf-8 -*-
# My first mad lib game written in python!

import time

# !/usr/bin/python
# -*- coding: utf-8 -*-

'''
Defining the global variables used in this program
'''

blanks = ['__1__', '__2__', '__3__', '__4__']

easy_text = 'Most __1__ today is very much like an Egyptian pyramid with millions of __2__ piled on top of each other, with no structural __3__, but just done by brute force and thousands of __4__. '
easy_answers = ["computing", "programmers", "mathematical", "algorithms"]

medium_text = '__1__ today is a race between __2__ engineers striving to build bigger and better idiot-proof __3__ , and the Universe trying to produce bigger and better idiots. So far, the __4__ is winning.'
medium_answers = ["Programming", "software", "programs", "universe"]

hard_text = '__1__ today is a race between __2__ engineers striving to build bigger and better idiot-proof __3__ , and the Universe trying to produce bigger and better idiots. So far, the __4__ is winning.'
hard_answers = ["Programming", "software", "programs", "universe"]

'''
The below function is for the user to input the
difficulty level of the game
'''


def user_input():
    difficulty_level = raw_input('Which difficulty level would you like? Type EASY, MEDIUM or HARD to continue.')
    level_chosen = difficulty_level.lower()
    return level_chosen

'''
This function gives the text with blanks based on
the user input level of game.
'''


def select_level():
    level_chosen = user_input()
    if level_chosen == 'easy':
        level_answers, level_text = easy_answers, easy_text
        print "Here's your text: " + str(easy_text)

    elif level_chosen == 'medium':
        level_answers, level_text = medium_answers, medium_text
        print "Here's your text: " + str(medium_text)

    elif level_chosen == 'hard':
        level_answers, level_text = hard_answers, hard_text
        print "Here's your text: " + str(difficult_text)

    else:
        level_answers, level_text = "invalid", "invalid"
        print "Invalid choice of level, choose again!\n"
        main()

    return level_answers, level_text

'''
This function plays the game by calling select_level(),
asking user to input answers and comparing it with the
stored list blanks
'''


def play_game(text, blanks, answers):

    i = 0
    while i < len(answers):
        user_input = raw_input('Type in answer:')
        if user_input == answers[i]:
            text = text.replace(blanks[i], user_input)
            print "Right answer, well done!!"
            time.sleep(1)
            print text
            i = i + 1
        else:
            print "Wrong answer buddy!:("
    else:
        print text
    time.sleep(1)
    return text

'''
Main block function
'''


def main():
    print 'Welcome to my first mad lib quiz with user input'
    level_answers, level_text = select_level()
    if level_answers != "invalid":
        print play_game(level_text, blanks, level_answers)

print main()
