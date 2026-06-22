# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] **Describe the game's purpose.** It's a Streamlit number-guessing game. The app picks a secret number within a range that depends on the chosen difficulty (Easy 1–20, Normal 1–50, Hard 1–100). The player types guesses, and after each guess the game responds "Too High" or "Too Low" to steer them toward the answer, updates a running score, and declares a win when the guess matches the secret (or a loss when attempts run out).

- [x] **Detail which bugs you found.**
  - **Reversed hints.** "Too High" told the player to "Go HIGHER!" and "Too Low" told them to "Go LOWER!" — the exact opposite of helpful, making the game effectively unwinnable by following the hints.
  - **Secret compared as a string.** On even-numbered attempts the secret was converted to a string before being compared to the integer guess, so the High/Low feedback was wrong (and could behave unpredictably) every other turn.
  - **Difficulty ranges swapped.** "Normal" used the 1–100 range and "Hard" used 1–50, which didn't match the sidebar labels.

- [x] **Explain what fixes you applied.**
  - Refactored `check_guess` out of `app.py` into `logic_utils.py` and corrected the hint direction: "Too High" → "Go LOWER!", "Too Low" → "Go HIGHER!".
  - Coerced both `guess` and `secret` to `int` inside `check_guess`, then removed the even-attempt `str()` branch in `app.py` so comparisons are always numeric and reliable.
  - Swapped the difficulty ranges in `get_range_for_difficulty` so Normal = 1–50 and Hard = 1–100, matching the captions.
  - Added pytest cases in `tests/test_game_logic.py` that lock in both fixes (string-secret comparison and correct hint direction).

## 📸 Demo Walkthrough

A sample game on **Hard** difficulty (range 1–100) where the secret number is **55**. Follow along without running anything:

1. The app starts, shows "Make a guess," and keeps the secret number fixed at 55 across submissions (it no longer changes on every click).
2. The player enters a guess of **40**. The game compares 40 to 55 and returns **"Too Low"** with the hint **"📈 Go HIGHER!"** — correctly pointing the player upward.
3. The player enters a guess of **70**. The game returns **"Too High"** with the hint **"📉 Go LOWER!"** — correctly pointing the player downward.
4. The score updates after each guess: it starts at 0, drops by 5 on each off-target guess, then jumps on the win — so a correct guess on the fourth attempt awards a bonus, landing the player at a final score of **40**.
5. The player enters **55**. The game recognizes the match, shows **"🎉 Correct!"**, triggers balloons, displays the final score, and ends the round in the "won" state.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
$ python -m pytest tests/ -v
============================= test session starts ==============================
platform darwin -- Python 3.13.13, pytest-9.1.0, pluggy-1.6.0
collected 9 items

tests/test_game_logic.py::test_winning_guess PASSED                      [ 11%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 22%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [ 33%]
tests/test_game_logic.py::test_string_secret_win PASSED                  [ 44%]
tests/test_game_logic.py::test_string_secret_too_high PASSED             [ 55%]
tests/test_game_logic.py::test_string_secret_too_low PASSED              [ 66%]
tests/test_game_logic.py::test_string_guess_also_coerced PASSED          [ 77%]
tests/test_game_logic.py::test_too_high_message_says_go_lower PASSED     [ 88%]
tests/test_game_logic.py::test_too_low_message_says_go_higher PASSED     [100%]

============================== 9 passed in 0.02s ===============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
