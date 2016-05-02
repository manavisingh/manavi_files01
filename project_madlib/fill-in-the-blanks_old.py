#!/usr/bin/python
# -*- coding: utf-8 -*-
# My first mad lib game written in python!

import time

#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
The below function taken in the user input and compares it
with the list of stored answers to tell the user if their input is correct or not.
On an incorrect input, it gives user the chance to fill in again the correct answer.
'''

def play_game(text, parts_of_speech):
    parts_of_speech = ['__1__', '__2__', '__3__', '__4__']
    i = 0
    while i < len(answers):
        user_input = raw_input('Type in answer:')
        if user_input == answers[i]:
            text = text.replace(parts_of_speech[i], user_input)
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

print 'Welcome to my first mad lib quiz with user input'
while True:

'''
This section is for getting the user input on the difficulty level
and for filling in the blanks as per the string passed in
'''

    # Game level 1 (Easy)

    difficulty_level = raw_input('Which difficulty level would you like? Type EASY, MEDIUM or HARD to continue.  '
                  )
    if difficulty_level.upper() == 'EASY':
        time.sleep(1)
        print "You chose Easy. Here's your text. Fill in the blanks for blanks __1__ to __4__ \n"
        time.sleep(1)
        print 'Most __1__ today is very much like an Egyptian pyramid with millions of __2__piled on top of each other, with no structural __3__, but just done by brute force and thousands of __4__. \n'
        
        #Blank strings and Answers stored for the game level EASY
        
        parts_of_speech = ['__1__', '__2__', '__3__', '__4__']
        answers = ["softwares","bricks","integrity","slaves"]
                   
        # The following is the text for easy level to pass in to the text function.

        text = "Most __1__ today is very much like an Egyptian pyramid with millions of __2__piled on top of each other, with no structural __3__, but just done by brute force and thousands of __4__."

        # Calling the two functions defined above to replace the blanks and output the result.
        
        print play_game(text, parts_of_speech)

    # Game Level 2 (Medium)

    elif difficulty_level.upper() == 'MEDIUM':
        time.sleep(1)
        print "You chose Medium. Here's your text. Fill in the blanks for blanks __1__ to __4__ \n"
        time.sleep(1)
        print 'The best programs are written so that __1__ machines can perform them quickly and so that human beings can understand them clearly. A __2__ is ideally an essayist who works with traditional aesthetic and literary forms as well as __3__ concepts, to communicate the way that an __4__ works and to convince a reader that the results will be correct. \n'

        #Blank strings and Answers stored for the game level MEDIUM

        parts_of_speech = ['__1__', '__2__', '__3__', '__4__']
        answers = ["computing","programmers","mathematical","algorithms"]
        
        # The following is the text for medium level to pass in to the text function.

        text = 'The best programs are written so that __1__ machines can perform them quickly and so that human beings can understand them clearly. A __2__ is ideally an essayist who works with traditional aesthetic and literary forms as well as __3__ concepts, to communicate the way that an __4__ works and to convince a reader that the results will be correct.'

        # Calling the two functions defined above to replace the blanks and output the result.

        print play_game(text, parts_of_speech)

    # Game Level 3 (Difficult)

    elif difficulty_level.upper() == 'HARD':
        time.sleep(1)
        print "You chose Hard. Here's your text. Fill in the blanks for blanks __1__ to __4__ \n"
        time.sleep(1)
        print '__1__ today is a race between __2__ engineers striving to build bigger and better idiot-proof __3__ , and the Universe trying to produce bigger and better idiots. So far, the __4__ is winning. \n'

        #Blank strings and Answers stored for the game level HARD
        
        parts_of_speech = ['__1__', '__2__', '__3__', '__4__']
        answers = ["Programming","software","programs","universe"]
        
        # The following is the text to be passed in.

        text = '__1__ today is a race between __2__ engineers striving to build bigger and better idiot-proof __3__ , and the Universe trying to produce bigger and better idiots. So far, the __4__ is winning.'

        # Checks if a word in parts_of_speech is a substring of the word passed in.

        print play_game(text, parts_of_speech)        

    else:
        print 'Oops! your didnt choose between EASY, MEDIUM or HARD! Try again....'
        time.sleep(1)
    break


			

			
