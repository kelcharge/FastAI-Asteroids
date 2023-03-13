# Python / FastAI Vision Learner - Playing Asteroids

> This code was used to gather and process data while playing Asteroids.
> The network was then trained using the FastAI Libary.

## Setup

- I used dual monitors with a game playing at a 800 X 600 resolution on one screen.
- You can start data collection by running capture.py
- Pressing B will start the screen / key grab. These will be stored in lists until the episode is done.
- Once the episode ( Round ) ends pressing h will stop the screen / key grab process and all data will be moved to a numpy array.
- Then I used a script in util folder called CreateImages.py to put then onto a disk drive in folders corresponding to their actions.

## Train

- Use the file called training.py

## Run Agents

- Fully random agent is RandomAgent.py
- Trained Agent is TrainedAgent.py
- You will have to load in the pkl created from training.

## Inputs (Observations)

- Uses inputs to the neural network (Observations) of pixes in the game.
- 224 X 224

## Forked from

- YouTube <a href="https://www.youtube.com/claritycoders" target="_blank">Clarity Coders</a>
