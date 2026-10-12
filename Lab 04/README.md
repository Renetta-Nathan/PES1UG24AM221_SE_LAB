
# Endless Runner

A simple endless-runner game built with Python and Pygame. The player jumps over incoming obstacles, earns points by passing them, and can restart with a selected difficulty after a game over.

## Features

- Player jumping with gravity and ground collision.
- Obstacles that move toward the player.
- Collision detection and a maximum game speed to help prevent obstacles from skipping past the player between frames.
- Score tracking when obstacles are successfully passed.
- Game Over screen displaying the final score.
- Replay options with Easy, Medium, and Hard difficulty levels, plus an Exit option.
- Sound effects for jumping, scoring, and game over.
- Separate Git commits for each lab task.

## Requirements

- Python 3
- Pygame

## Setup

1. Clone or download this repository.
2. Open a terminal in the project root (the directory containing `main.py`).
3. Install the required packages:

   ```bash
   python -m pip install -r requirements.txt
   ```

   On Windows, you can also run:

   ```powershell
   py -m pip install -r requirements.txt
   ```

## Run the Game

From the project root, run:

```bash
python main.py
```

On Windows, you can also use:

```powershell
py main.py
```

## Controls

- **Jump:** `Space`, `Up Arrow`, or `W`
- **Game Over menu:** Use the options and key instructions displayed in the game window to select a difficulty or exit.

## Project Structure

```text
39_endless-runner/
├── main.py
├── requirements.txt
└── game/
    ├── game_engine.py
    ├── obstacle.py
    └── player.py
```

Sound assets may be stored in the project's sound directory, depending on the implementation.

## Gameplay

Avoid obstacles by jumping over them. Each obstacle passed awards a point. If the player collides with an obstacle, the game ends and displays the final score. Choose a difficulty to start a new round, or select Exit to close the game.

## Lab Deliverables

For the VibeCoding lab submission, include:

- A 10-second video recorded before changes.
- A 10-second video recorded after all changes.
- The updated source code.
- An exported PDF or document containing the AI chat history.

Keep a separate Git commit for each task, and push the finished work to your own GitHub repository. Do not open a pull request to the instructor's original repository.

## Troubleshooting

- If Pygame is missing, install dependencies using the setup commands above.
- Run commands from the project root so `main.py` and the `game` package can be found.
- If audio is unavailable, check that the sound files exist in the expected location and that your system's audio output is enabled.
