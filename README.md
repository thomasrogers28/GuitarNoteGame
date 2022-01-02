# GuitarNoteGame
A game designed to help memorise the positions of notes on a guitar.

Current version is for a classical 6-string guitar with standard tuning up to the 19th fret.

Two versions are currently available for this game: the first is played within the python console, and the second creates a front end display using pygame. I have kept these separate for now as an additional quality control, however I intend to merge the two in the future.

# Options
Additional options to change the difficulty settings for frets and strings:

Tuning:
  - Can alter the tuning of the open strings
  - In theory, you can add or remove strings in this tuning and it will still work, however it will mess up the string difficulty setting below (for easy & medium) 

Frets:
  - Easy (1) - Up to 5th fret
  - Medium (2) - Up to 12th fret
  - Hard (3) - Up to 19th fret

Strings:
  - Easy (1) - 1st and 6th strings only
  - Medium (2) - 1st, 2nd, 3rd and 6th strings only
  - Hard (3) - all six strings

# Future Developments
- Add text to the display to show the current question 
- Add text to the display to show what the previous correct answer was when guessed incorrectly
- Add an on-screen timer 
- Create a 'Start' page to allow users to alter options without adjusting code
