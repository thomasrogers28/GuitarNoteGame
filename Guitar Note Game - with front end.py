# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 17:52:56 2022

@author: Admin
"""

from random import randrange
import pygame
import ctypes

pygame.init()

width = 998 #dimensions of image 
height = 269 #dimensions of image 
gameDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption('Guitar Note Game')

clock = pygame.time.Clock()
guitarImg = pygame.image.load('Guitar-Fretboard-Blank-v3.jpg')

font = pygame.font.Font(None, 32)
input_box = pygame.Rect((width/2)-70, height - 50, 140, 32)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
text = ''
guess= ''

########## DECLARE PARAMETERS ############

#define the open tuning for fret 0 (open fret)
tuning = ["E", "A", "D", "G", "B", "E"]

#set difficulty parameters from 1-3
diff_fret = 2;
diff_string = 3;

#this is to allow a max round number (to avoid having to complete up to 120 iterations each test)
count = 1
max_count = 10
compare = "H";

########## SETTING FUNCTIONALITY ############

#start with a list of notes (for stepping through and cycling)
notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

#create a list of the correct answers to compare to
#each line refers to a fret, and then each element within it refers to a string starting at the lowest string
answer_grid = []
next_fret = []
fret_count = 19 #classical guitars go up to 19 frets, but this could be increased if preferred
i = 0

while i <=  fret_count:
    for strings in tuning:
        next_note = notes[(notes.index(strings) + i) % 12]
        next_fret.append(next_note)
    answer_grid.append(next_fret)
    next_fret = []
    i += 1

#set difficulty settings - fret
if diff_fret == 1:
    del answer_grid[6:];
elif diff_fret == 2:
    del answer_grid[13:];

#set difficulty settings - string
if diff_string == 1:
    for list in answer_grid:
        del list[4] #remove G string
        del list[3] #remove B string
        del list[2] #remove D string
        del list[1] #remove A string
elif diff_string == 2:
    for list in answer_grid:
        del list[2] #remove D string
        del list[1] #remove A string

#create finished grid to track previous questions
finished_grid = answer_grid;
finished_grid = [["" for y in x] for x in finished_grid];
guess_grid = finished_grid

#create list to track successful guesses
guess_scores = [];

GameOver = False
question_toggle = True

while not GameOver:

    gameDisplay.blit(guitarImg, (0, 0))
    
    for x in range (0, len(answer_grid)):
        for y in range (0, len(answer_grid[0])):
            if guess_grid[x][y] != answer_grid[x][y] and guess_grid[x][y] != "":
                pygame.draw.circle(gameDisplay, (255, 0, 0), (33 + x * 47.2, 34 + (5 - y) * 33), 10)
            if guess_grid[x][y] == answer_grid[x][y] and guess_grid[x][y] != "":
                pygame.draw.circle(gameDisplay, (0, 255, 0), (33 + x * 47.2, 34 + (5 - y) * 33), 10)

    if (answer_grid == finished_grid) or count > max_count: 
        EndMessage = "Congratulations, you've scored:" ;
        EndMessage += str(100 * sum(guess_scores)/len(guess_scores))
        EndMessage += "%"
        ctypes.windll.user32.MessageBoxW(0, EndMessage, "Game Over", 0)
        GameOver = True
        
    #pick a random fret and string to guess against
    while compare != "":
        string_range = len(finished_grid[0]); #number of available strings
        fret_range = len(finished_grid); #number of available frets
        string = randrange(string_range);
        fret = randrange(fret_range);
        compare = finished_grid[fret][string];
    
    #pygame.draw.circle(gameDisplay, (255 - guess * 255, guess * 255, 0), (33 + fret * 47.2, 34 + (string) * 33), 10)
    pygame.draw.circle(gameDisplay, (0, 255 - int(fret) * (230/24), 255), (33 + int(fret) * 47.2, 34 + int(5 - string) * 33), 10)
    
    #convert to text for the pop up
    #since element 1 = string 6, we also need to flip the string number
    fret_str = str(fret);
    
    if diff_string == 3:
        string_str = str(6 - string);
    elif diff_string == 2:
        if string == 0:
            string_str = str(6 - string);
        else:
            string_str = str(4 - string);
    elif diff_string == 1:
        if string == 0:
            string_str = str(6);
        else:
            string_str = str(1);

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
    if question_toggle:
        print(question)
        question_toggle = False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameOver = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if input_box.collidepoint(event.pos):
                # Toggle the active variable.
                active = not active
            else:
                active = False
            # Change the current color of the input box.
            color = color_active if active else color_inactive
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    guess = text
                    #fix formatting of the guess
                    guess = guess.capitalize();
                    
                    #change flats to sharps to match the answer grid
                    if len(guess) == 2 and guess[1] == "b":
                        guess = notes[(notes.index(guess[0]) - 1) % 12]
                    #change sharps to whole notes to match the answer grid (e.g. B# => C)
                    elif len(guess) == 2 and guess[1] == "#" and guess not in notes:
                        guess = notes[(notes.index(guess[0]) + 1) % 12];
                        
                    #print the guess for trouble shooting
                    print(guess);
                    text = ''
                    question_toggle = True
                    compare = "H";
                    count += 1
                    
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
                    guess_grid[fret][string] = guess;

                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
        
    # Render the current text.
    txt_surface = font.render(text, True, color)
    # Blit the text.
    gameDisplay.blit(txt_surface, (input_box.x+5, input_box.y+5))
    # Blit the input_box rect.
    pygame.draw.rect(gameDisplay, color, input_box, 2)
    
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
