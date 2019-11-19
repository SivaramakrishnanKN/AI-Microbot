# AI-Microbot

![](Media/Demo.gif)

A prototype of an Artificially Intelligent Microbot for targeted drug delivery in the human circulatory system. A map consisting of Arteries, Veins, Capillaries, and Organs each having their own set of characteristics and properties is randomly generated. The micro-bot, having a set of sensors and electromagnets, will have to traverse the map given a randomly generated starting point and target organ in the most optimal path possible. The bot's speed in the system will also depend on the thickness of the blood vessel.

## Circulatory System
1. Arteries: Denoted by red pipes, arteries have a thickness varying between. Blood flow and hence bot movement is available in both directions.
2. Veins: Veins are dentoed by cyan colored pipes. They have a thickness varying between . Blood flow is only available in one direction.
3. Organs: Organs denoted by pink colored rectangles are the target sites for the microbot.

## Microbot
 The microbot has been trained by AI to suggest the most optimal direction the Doctor must take to reach the Target Organ by looking ahead with its sensors and deducing the least cost path (heuristic). This isn't always accuracte, which is where the Doctor's discretion comes into play and he makes his own call. It will receive feedback on how successful it's journey has been based on a reward system.
 
## Setup

### Install Packages

1. Numpy Library:
To install the numpy library run the following in command prompt

```
pip install numpy
```

To check the library which are already installed on your PC use command

```
pip list
```

2. Pygame:
To download pygame run the following in command prompt

```
pygame‑1.9.2a0‑cp35‑none‑win32.whl
```

To install the downloaded software

```
C:\Users\name\> cd Downloads
C:\Users\name\Downloads> pip install pygame-1.9.2a0-cp35-none-win32.whl
```
