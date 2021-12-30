# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 18:25:38 2021
Last Edited Thu Dec 30 12:21:05 2021
@author: Thomas Rogers
"""
from random import randrange

#create a list of the correct answers to compare to
#each line refers to a fret, and then each element within it referes to 
#a string starting at the lowest string
answer_grid =  [["E","A","D","G","B","E"]
                ,["F","A#","D#","G#","C","F"]
                ,["F#","B","E","A","C#","F#"]
                ,["G","C","F","A#","D","G"]
                ,["G#","C#","F#","B","D#","G#"]
                ,["A","D","G","C","E","A"]
                ,["A#","D#","G#","C#","F","A#"]
                ,["B","E","A","D","F#","B"]
                ,["C","F","A#","D#","G","C"]
                ,["C#","F#","B","E","G#","C#"]
                ,["D","G","C","F","A","D"]
                ,["D#","G#","C#","F#","A#","D#"]
                ,["E","A","D","G","B","E"]];

finished_grid =  [["","","","","",""]
                ,["","","","","",""]
                ,["","","","","",""]
                ,["","","","","",""]
                ,["","","","","",""]
                ,["","","","","",""]
                ,["","","","","",""]
                ,["","","","","",""]
                ,["","","","","",""]
                ,["","","","","",""]
                ,["","","","","",""]
                ,["","","","","",""]
                ,["","","","","",""]];

guess_scores = [];

#this is to allow a max round number (to avoid having to complete 72 iterations each test)
count = 1

#loop until finished_grid is complete
while (answer_grid != finished_grid) and count <= 5:
    #pick a random fret and string to guess against
    compare = "H";
    while compare != "":
        string = randrange(6);
        fret = randrange(13);
        compare = finished_grid[fret][string];
    
    #convert to text for the pop up
    #since element 1 = string 6, we also need to flip the string number
    string_str = str(6 - string);
    fret_str = str(fret);
    
    #create a suffix to show 1st, 2nd, 3rd or nth for string
    if string_str in ("1"):
        string_suffix = "st"
    elif string_str in ("2"):
        string_suffix = "nd"
    elif string_str in ("3"):
        string_suffix = "rd"
    else:
        string_suffix = "th";
    
    #create a suffix to show open, 1st, 2nd, 3rd or nth for fret    
    if fret_str in ("0"):
        fret_suffix = "open"
    elif fret_str in ("1"):
        fret_suffix = fret_str + "st"
    elif fret_str in ("2"):
        fret_suffix = fret_str + "nd"
    elif fret_str in ("3"):
        fret_suffix = fret_str + "rd"
    else:
        fret_suffix = fret_str + "th";
    
    #pop up the question
    question = string_str + string_suffix + " string, " + fret_suffix + " fret: ";
    
    #submit guess
    guess = input(question);
    
    #fix formatting of the guess
    guess = guess.capitalize();
    
    #change flats to sharps to match the answer grid
    if len(guess) == 2 and guess[1] == "b" and guess[0] == "A":
        guess = "G#"
    elif len(guess) == 2 and guess[1] == "b":
        guess = chr(ord(guess[0]) - 1) + "#";
        
    #print the guess for trouble shooting
    print(guess);
    
    #find answer from starting grid
    answer = answer_grid[fret][string];
    
    #show if the answer is correct
    if guess == answer:
        print("Correct!")
        guess_scores.append(1);
    else:
        print("Incorrect - The answer is " + answer)
        guess_scores.append(0);
    
    #update blank grid
    finished_grid[fret][string] = answer;
    
    count = count + 1;
 
#display results  
print("Congratulations, you've scored:")  
print(100 * sum(guess_scores)/len(guess_scores));

