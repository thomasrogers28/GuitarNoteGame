# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 18:25:38 2021

@author: Admin
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

#pick a random fret and string to guess against
string = randrange(6);
fret = randrange(13);

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

#create a suffix to show 1st, 2nd, 3rd or nth for fret    
if fret_str in ("1"):
    fret_suffix = "st"
elif fret_str in ("2"):
    fret_suffix = "nd"
elif fret_str in ("3"):
    fret_suffix = "rd"
else:
    fret_suffix = "th";

#pop up the question
question = string_str + string_suffix + " string, " + fret_str + fret_suffix + " fret: ";

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
else:
    print("Incorrect - The answer is " + answer);

#update blank grid
finished_grid[fret][string] = answer;

