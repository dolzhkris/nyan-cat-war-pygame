# nyan-cat-war-pygame
Python arcade game: control Nyan Cat, dodge UFO fireballs, and rack up points.

## About

It is a simple arcade game where the player controls Nyan Cat.
A UFO flies on the right side of the screen and periodically fires fireballs.
The player's goal is to dodge them. Every projectile that flies past Nyan Cat
and exits the left edge of the screen awards +1 point.

As the score grows, the difficulty increases - the UFO starts firing more often.

The game ends when Nyan Cat collides with a projectile or touches the boundaries
of the play area (the top or bottom "ship" zones).

This project was developed as a university project during the second year of university.
Inspired by an open-source Mario game.

## Controls

| Key             | Action                          |
|-----------------|---------------------------------|
| `Up Arrow`      | Nyan Cat moves up               |
| `Down Arrow`    | Nyan Cat moves down             |
| `Enter`         | Start game / Restart            |
| `Esc`           | Quit game                       |

## Key Variables

- screen_width - width of the game window in pixels;
- screen_height - height of the game window in pixels;
- FPS - frames per second, controls the game loop speed;
- base_flame_rate - base interval (in frames) between UFO shots;
- new_flame_rate - current shot interval, recalculated per level;
- level - current difficulty level (1–4), derived from the score;
- score - player's current score, increases per dodged projectile;
- flame_list - list of active projectiles (`Flames` objects) on screen;
- new_flame_counter - frame counter used to decide when to spawn the next projectile;
- nlo - the UFO instance that moves vertically and shoots;
- nyan_cat - the player-controlled Nyan Cat instance;
- topscore - object storing and updating the session's high score;
- ships_rev_rect - bounding rectangle of the top ship (upper play-area boundary);
- ship_rect - bounding rectangle of the bottom ship (lower play-area boundary).

## Key Functions

- start_game() - displays the start screen and waits for `Enter` or `Esc`;
- game_loop() - main game loop: rendering, updates, input, collisions, scoring;
- game_over() - displays the Game Over screen, plays sound, handles restart / quit;
- check_level(score) - recalculates `level` and `new_flame_rate` based on the current score;
- TopScore.topscore() - updates and returns the session's high score;
- NLO.update() - moves the UFO up/down and renders it;
- Flames.update() - moves a projectile left and renders it;
- NyanCat.update() - moves Nyan Cat per input and triggers `game_over()` on boundary touch.

## How to Run

1. Clone the repository

```bash
git clone https://github.com/dolzhkris/nyan-cat-war-pygame.git
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the game

```bash
python game.py
```

! Make sure the `images/` and `musicandsounds/` folders are next to `game.py`.
