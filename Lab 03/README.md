# Lab 4 – VibeCoding

## Endless Runner Game

**Student ID:** PES1UG24AM221  
**Lab:** Software Engineering – Lab 4  
**Topic:** VibeCoding and AI-Assisted Software Development

---

## 1. Objective

The objective of this lab is to use AI-assisted coding tools to identify and fix existing code issues and implement additional features in a Python-based game. The lab focuses on writing effective prompts, making incremental code changes, testing the implementation, and maintaining separate Git commits for individual tasks.

For this lab, the selected project is the **Endless Runner Game**, developed using Python and Pygame.

---

## 2. System Scenario

The Endless Runner Game is a simple game in which the player must jump over incoming obstacles to avoid collisions and achieve a higher score.

The game continuously generates obstacles that move toward the player. The score increases whenever the player successfully passes an obstacle. If the player collides with an obstacle, the game ends and displays the final score.

The game was enhanced using AI-assisted coding to improve collision detection, provide a proper Game Over screen, introduce difficulty selection and replay functionality, and add sound effects.

### Main Functions

- Allow the player to jump over obstacles.
- Generate and move obstacles across the screen.
- Detect collisions between the player and obstacles.
- Increase the score when obstacles are passed.
- Prevent obstacles from skipping past the player's collision area at high speeds.
- Display a Game Over screen with the final score.
- Allow the player to restart the game.
- Provide Easy, Medium, and Hard difficulty levels.
- Allow the player to exit the game.
- Play sound effects for jumping, scoring, and game over.

---

## 3. Problems Identified in the Original System

The original game contained several incomplete features and implementation issues that needed to be addressed.

### 3.1 Collision Detection and Speed Increase

The game speed increased continuously without a maximum limit. Collision detection was performed after obstacles moved, which could allow an obstacle to pass completely across the player's collision area between frames.

**Solution:**
- Introduce a maximum game speed.
- Improve collision detection to account for obstacles crossing the player's hitbox between frames.

### 3.2 Missing Game Over Screen

The original game detected collisions and printed the final score in the terminal, but it did not provide a proper Game Over screen inside the game window.

**Solution:**
- Display a Game Over message.
- Show the final score inside the Pygame window.
- Stop gameplay updates after the game ends.

### 3.3 Missing Replay and Difficulty Selection

The original game did not provide a complete replay system with difficulty selection.

**Solution:**
- Add Easy, Medium, and Hard difficulty levels.
- Allow the player to restart with a selected difficulty.
- Reset the score, player state, obstacles, and relevant timers when restarting.
- Provide an Exit option.

### 3.4 Missing Sound Effects

The original game lacked sound effects for important gameplay events.

**Solution:**
- Add a sound effect when the player jumps.
- Add a sound effect when the player scores a point.
- Add a sound effect when the game ends.

---

## 4. AI-Assisted Development Approach

The project was developed using an iterative VibeCoding approach. Instead of implementing all features in a single prompt, each task was handled independently.

The development process involved:

1. Inspecting the existing source code.
2. Identifying the problems and incomplete features.
3. Writing specific prompts for the AI coding tool.
4. Reviewing the suggested code changes.
5. Applying the changes to the project.
6. Running the game and testing the implementation.
7. Fixing any issues discovered during testing.
8. Creating a separate Git commit for each task.

This approach made the development process easier to manage and helped preserve the functionality of previously implemented features.

---

## 5. Features Implemented

The project was divided into four tasks.

### Task 1: Collision Detection and Speed Control

The first task focused on improving collision detection and preventing the game speed from increasing indefinitely.

The speed increase was limited using a maximum speed value. Collision detection was improved to handle cases where an obstacle could cross the player's collision area between consecutive frames.

This helps ensure that collisions are detected more reliably as the game becomes faster.

### Task 2: Game Over Screen

The second task involved implementing a proper Game Over screen.

When the player collides with an obstacle, the game displays a Game Over message and the final score inside the game window. Gameplay updates stop after the game ends.

This improves the user experience by providing clear feedback about the end of a game session.

### Task 3: Replay and Difficulty Selection

The third task introduced replay functionality and difficulty selection.

The player can choose between Easy, Medium, and Hard difficulty levels or exit the game. Each difficulty level is intended to provide a different level of challenge.

When the player starts a new round, the game resets the score, player state, obstacles, and relevant timers so that the previous game does not affect the new session.

### Task 4: Sound Effects

The fourth task involved adding sound effects for important gameplay events.

The required sound effects include:

- **Jump Sound:** Plays when the player successfully jumps.
- **Scoring Sound:** Plays when the player passes an obstacle and earns a point.
- **Game Over Sound:** Plays when a collision ends the game.

Sound playback should be triggered by the corresponding events and should not repeat continuously while the Game Over screen is displayed.

---

## 6. Technologies and Tools Used

| Technology / Tool | Purpose |
|---|---|
| Python | Main programming language |
| Pygame | Game development, graphics, input handling, and audio |
| VS Code | Code editing and project development |
| AI Coding Tool | Code analysis, debugging, and feature implementation |
| Git | Version control and separate commits for each task |
| GitHub | Repository hosting and submission of updated code |
| Screen Recording Software | Recording gameplay before and after implementation |

---

## 7. Testing and Validation

After implementing the features, the game should be tested to verify that the new functionality works correctly and that existing gameplay is preserved.

### Test Cases

| Test Case | Expected Result |
|---|---|
| Launch the game | The game opens without errors |
| Jump over an obstacle | The player jumps correctly |
| Collide with an obstacle | Collision is detected and the game ends |
| Play at increasing speeds | Collisions continue to register reliably |
| Pass an obstacle | The score increases by one |
| Trigger Game Over | The final score appears on the Game Over screen |
| Select Easy | The game starts with an easier difficulty |
| Select Medium | The game starts with normal difficulty |
| Select Hard | The game starts with a greater challenge |
| Restart the game | The score and gameplay state reset |
| Trigger jump, scoring, and game-over events | The corresponding sounds play |
| Select Exit | The game closes cleanly |

---

## 8. Version Control and Deliverables

Git was used to maintain the project's development history. Each task was committed separately to make the changes easier to track and review.

The expected commit sequence is:

1. `Fix collision detection and speed ramp`
2. `Add game over screen and final score`
3. `Add replay and difficulty selection`
4. `Add jump scoring and game over sounds`

The completed lab submission includes:

- A 10-second video recorded before making changes.
- A 10-second video recorded after implementing all features.
- The updated source code.
- The exported AI chat history in PDF or document format.

The updated code must be pushed to the student's personal GitHub repository. A pull request must not be created against the original `SETAPESU26` repository.

---

## 9. Conclusion

This lab demonstrated the use of AI-assisted coding to improve an existing Python game through iterative development. The project involved fixing collision detection, controlling the game's speed, implementing a Game Over screen, adding replay and difficulty selection, and introducing sound effects.

The lab also emphasized the importance of writing clear prompts, reviewing AI-generated code, testing features independently, debugging errors, and maintaining separate Git commits. Overall, the exercise provided practical experience in software maintenance, incremental feature development, version control, and AI-assisted software engineering.
