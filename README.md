# Nonsense: The Game
## CS 110 Final Project
### Fall 2018

[https://github.com/binghamtonuniversity-cs110/final-project-fall18-the](#)

[link to demo presentation slides](#)

### Team: __THE__
* Michael Spano
* Kevin Apyapong
* Brain DeVries

***

## Project Description
 __Nonsense: The Game__ is a 5-minigame survival gauntlet that gets progressively more demented as it continues. Gameplay is as follows: The player is led through an assortment of games and scenarios that are rotated according to a randomized timer. Success in each scene will raise the player’s score. Failure will increase the insanity meter, resulting in a series of undesirable graphical, audio, and logical distortions. It’s game over once the insanity meter reaches 6.


***    

## User Interface Design
* A wireframe or drawing of the user interface concept along with a short description of the interface. You should have one for each screen in your program.
    * For example, if your program has a start screen, game screen, and game over screen, you should include a wireframe / screenshot / drawing of each one and a short description of the components
    * You should also have a screenshot of your final GUI

***        

## Program Design
* Additional Libraries:
    * None
* Class Interface:
    * A simple drawing that shows the class relationships in your code (see the sample Proposal document for an example).
    * This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm.
* List of Classes:
    * Controller Class: Randomly chooses a new scene based off of the levels that have already been completed. Used to display insanity, score, clock, and handle related effects.
    * Club Class: Contains the game loop for club level
      * Model Classes include Character, Arrows, and Dialogue
    * Typing Class: Contains the game loop for typing level
      * No Model Classes
    * Platformer Class: Contains the game loop for platformer level
      * Model Classes include: Player_Platform, Enemy, Player_Death, Dragon, Explosion, Fireball, and Platforms_Map
    * Maze Class: Contains the game loop for maze level
      * Model Classes include: Player, insanity5face
    * Space Class: Contains the game loop for space shooter level
      * Model Classes include: Hero, Enemy, HeroBlast, and Explosion
***

## Tasks and Responsibilities
### Software Lead - Brian DeVries
Overseer of Club and Typing levels

### Front End Specialist - Kevin Apyapong
Overseer of Space Shooter Level

### Back End Specialist - Michael Spano
Overseer of Maze and Platform Level


## Testing
* Describe your testing strategy for your project.
    * We run our code after every update and verify that it works by printing or just visual feedback.

### Menu Testing

Description


### Game Testing

Description

* Outline for graph of testing visual

| Step                  | Procedure     | Expected Results  | Actual Results |
| ----------------------|:-------------:| -----------------:| -------------- |
|  1  | Run Counter Program  | GUI window appears with count = 0  |          |
|  2  | click count button  | display changes to count = 1 |                 |
etc...
