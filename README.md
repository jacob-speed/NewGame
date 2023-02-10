# Pygame Readme

## Overview

This is a Pygame game where the player controls a rectangle and has to avoid bouncing balls that randomly spawn on the screen. If there is a collision between the player and the ball, the player will lose hitpoints based on the speed and size of the ball. If the player's hitpoints reach 0, the game restarts. The goal is to last as long as possible and score points based on the time the player lasts.

The game has a global speed modifier which increases the speed of the balls as the game progresses. There are also different colored balls that, if collided with, provide upgrades to the player such as:
- Blue ball provides increased hitpoints and size, 
- Green ball provides increased speed
- Red ball increaces the size of the world to allow more space for dodging balls.

## Files

The code is split into three .py files:

- `objects.py`: This file defines the `Ball` and `Character` objects used in the game.

- `functions.py`: This file defines all the functions used in the game.

- `main.py`: This file includes the main while loop that runs the game.

## Requirements

- Pygame library

## How to Play

1. Clone the repository to your local machine

```git clone https://github.com/[username]/pygame.git```

2. Install the Pygame library

```pip install pygame```

3. Run the `main.py` file

```python main.py```

4. Use the arrow keys to move the rectangle and avoid the bouncing balls.

5. The game is over when the player's hitpoints reach 0. Try to last as long as possible to score points!

## Contributing

If you would like to contribute to the development of this game, feel free to submit a pull request.

## License

This project is licensed under the [MIT](LICENSE) license.
