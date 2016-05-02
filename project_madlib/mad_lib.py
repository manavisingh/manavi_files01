#My first mad lib game written in python!

import time

'''
Defining Function to get the common words between the strings passed.
'''

def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None 
            

'''
Defining the function that uses the function word_in_pos to 
replace the common words with answers given by the users and display the final result.           
'''
        
def play_game(text, parts_of_speech):
    #print word_in_pos(word, parts_of_speech)
    #parts_of_speech  = ["__1__","__2__","__3__","__4__"]
    #text = "Python is a __1__ language that provides constructs intended to enable clear programs on both small and large scale. Python implementation was started in December __2__ by Guido von Rossum. The most simple __3__ in Python is __4__ and normally used at the beginning to tell Python to write 'Hello World' on the screen."
    replaced = []
    text = text.split()
    answers = ["manavi","cat","dog","animal"]
    for word in text:
        replacement = word_in_pos(word, parts_of_speech)
        #print replacement
        if replacement != None:
            user_input = raw_input("Type in: " + replacement + " ")
            i = 0
            while i < len(answers):
                if user_input == answer[i]:
                    
            word = word.replace(replacement, user_input)
            replaced.append(word)
            print user_input
        else:
            replaced.append(word)
    replaced = " ".join(replaced)
    print
    time.sleep(1)
    print "Result Time! your result is....."
    print
    time.sleep(1)
    return replaced
    print  
    time.sleep(1)
       
'''
This is the main section that takes in the input from the user
and then uses the above two functions to replace the blanks and 
output the final result
'''

print "Welcome to my first mad lib quiz with user input"
while True:
    # Game level 1 (Easy)
    difficulty_level = raw_input("Which difficulty level would you like? Type EASY, MEDIUM or HARD to continue.  ")
    if difficulty_level.upper() == "EASY":
        time.sleep(1)
        print "You chose Easy. Here's your text. Fill in the blanks for blanks __1__ to __4__ "
        print
        time.sleep(1)
        print "Python is a __1__ language that provides constructs intended to enable clear programs on both small and large scale. Python implementation was started in December __2__ by Guido von Rossum. The most simple __3__ in Python is __4__ and normally used at the beginning to tell Python to write 'Hello World' on the screen."
        print
        # A list of replacement words to be passed in. 
        parts_of_speech  = ["__1__", "__2__", "__3__", "__4__"]
        # The following is the text for easy level to pass in to the text function.
        text = "Python is a __1__ language that provides constructs intended to enable clear programs on both small and large scale. Python implementation was started in December __2__ by Guido von Rossum. The most simple __3__ in Python is __4__ and normally used at the beginning to tell Python to write 'Hello World' on the screen."
        # Calling the two functions defined above to replace the blanks and output the result.
        print play_game(text, parts_of_speech)

    # Game Level 2 (Medium)
    if difficulty_level.upper() == "MEDIUM":
        time.sleep(1)
        print "You chose Medium. Here's your text. Fill in the blanks for blanks __1__ to __4__ "
        print
        time.sleep(1)
        print "A string object is __1__, i.e. it cannot be modified after it has been created. An important concept in Python and other programming languages is __2__. You use them to store a value. To assign a value to a Variable you use the __3__ operator. A more versatile data type in Python is __4__. They contain items separated by commas and within square brackets. To some extent they are similar to arrays in C."
        print
        # A list of replacement words to be passed in.
        parts_of_speech  = ["__1__", "__2__", "__3__", "__4__"]
        # The following is the text for medium level to pass in to the text function.
        text = "A string object is __1__, i.e. it cannot be modified after it has been created. An important concept in Python and other programming languages is __2__. You use them to store a value. To assign a value to a Variable you use the __3__ operator. A more versatile data type in Python is __4__. They contain items separated by commas and within square brackets. To some extent they are similar to arrays in C."
        # Calling the two functions defined above to replace the blanks and output the result.
        print play_game(text, parts_of_speech)

    # Game Level 3 (Difficult)
    if difficulty_level.upper() == "HARD":
        time.sleep(1)
        print "You chose Hard. Here's your text. Fill in the blanks for blanks __1__ to __4__ "
        print
        time.sleep(1)
        print "Similar to other programming languages, Python has flow controls. The most known statement is the __1__ statement. It can be combined with an else statement and helps to process a logic based on a specific condition. For more repetitive processing one needs to use loops. __2__ loops execute a sequence of statements multiple times and abbreviates the code that manages the loop variable.__3__ loops repeat a statement or group of statements while a given condition is TRUE. It tests the __4__ before executing the loop body."
        print
        # A list of replacement words to be passed in to the play game function. 
        parts_of_speech  = ["__1__", "__2__", "__3__", "__4__"]
        # The following are some test strings to pass in to the play_game function.
        text = "Similar to other programming languages, Python has flow controls. The most known statement is the __1__ statement. It can be combined with an else statement and helps to process a logic based on a specific condition. For more repetitive processing one needs to use loops. __2__ loops execute a sequence of statements multiple times and abbreviates the code that manages the loop variable. __3__ loops repeat a statement or group of statements while a given condition is TRUE. It tests the __4__ before executing the loop body."
        # Checks if a word in parts_of_speech is a substring of the word passed in.
        print play_game(text, parts_of_speech)

    else:
        print "Oops! your didnt choose between EASY, MEDIUM or HARD! Try again...."
        time.sleep(1)
    
    

    

