# AI-Microbot

![](Media/Demo.gif)

A prototype of an Artificially Intelligent Microbot for targeted drug delivery in the human circulatory system. A map consisting of Arteries, Veins, Capillaries, and Organs each having their own set of characteristics and properties is randomly generated. The micro-bot, having a set of sensors and electromagnets, will have to traverse the map given a randomly generated starting point and target organ in the most optimal path possible. The bot's speed in the system will also depend on the thickness of the blood vessel.

## Setup
### Requirements
1. You must have Python 3.7 or higher installed on your computer.
2. Your system must be running a 64-bit version of Windows. 

### Install CxFreeze
Run the following command in Command Prompt or inside an Anaconda Environment.
```
python -m pip install cx_Freeze --upgrade
```

### Cloning the Repository
You can either download the zip file and extract it into a folder or you can clone it using the following command- 
```
git clone https://github.com/SivaramakrishnanKN/AI-Microbot 
```

### Building the Game
Once you have cloned into the repository move into the folder containing the game and run the following command -
```
cd ~/.../AI-Microbot
python setup.py build
```
Now copy the folders labelled "Media" and "Fonts" into "~\...\AI-Microbot\build\exe.win-amd64-3.7" and you're all set to run the game!

Double-click on gui.exe to play the game.

## Aim of the Game
 The microbot has been trained by AI to suggest the most optimal direction the Doctor must take to reach the Target Organ by looking ahead with its sensors and deducing the least cost path (heuristic). This isn't always accuracte, which is where the Doctor's discretion comes into play and he makes his own call. It will receive feedback on how successful it's journey has been based on a reward system.
 
## Rules
1. The bot (black square) can only move in the directions indicated by the arrows. Sometimes, it might reach the end of an artery or a vein and the player will not be able to move any further in which case the game must be reset (Press R)
2. The bot can move freely, backwards and forwards in an Artery (Red lines) whereas it can move only in the displayed direction in a Vein (Blue Line).
3. Aim to reach the target organ (Dark Pink) with the highest score possible.
4. The bot's score is deducted based on the move the player makes, for instance if it comes in contact with the wrong organ (Light Pink) it is heavily penalised.
