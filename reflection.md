# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
ANSWER: 
  1. In the enter your guess bar it says to click Enter to apply however, when I click apply nothing happens, the guess is not submitted.
  2. The "Go lower" and "Go higher" hints are incorrect and should be the opposite.
  3. After clicking the New Game button istead of creating a new game it does not do anything.
  4. The sidebar when changing difficulty does not change the actual game and it stays on 
  5. Hard mode ranges between 1 - 50 and Normal mode ranges between 1- 100, I assume those two are mixed up.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
ANSWER:
  1. I used Claude to help me fix the bugs and set up venv to download all the requirements for the project.
  2. The New Game button didn't restart the game. Claude suggested taht the it resets attpts to 0 but leves the status as "won" or "lost", which prevents the game from continuing. Plus it's using a hardcoded range instead of respecting the difficulty setting. Therefore, Claude suggested to change the varibles status = "playing", history = [], uses random.randint(low, high) (which was hardcoded to 1-100).
  3. For some reason Claude decided to break the UI structure of the columns of Submit Game, New Game and Show hint buttons/checkbox. It seperated the button left them under the guessing textbox but took the checkbox and put it above the textbox.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

ANSWER:
1. I tested the specific behavior that was broken, if the symptom was gone and no other behavior broke, I considered it fixed. I also ran the pytest tests to confirm the fix held up in code, not just visually.
2. test_guess_too_high in test_game_logic.py calls check_guess(60, 50) and asserts the outcome is "Too High" with the message "📉 Go LOWER!". Before the fix, this test would have failed because the hints were reversed — the function was returning "Go HIGHER!" when the guess was above the secret. Running it after the fix confirmed the condition logic was corrected.
3. Yes, Claude suggested writing separate unit tests for check_guess and get_range_for_difficulty since those were the two functions with the clearest bugs. It helped me see that pulling logic into logic_utils.py made the functions testable in isolation, without needing to run the full Streamlit app.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

ANSWER:
1. Every time I intereacted with the app streamlit reran te entire Python script. And since random.randint() was called outside of a session state check, it generated a brand new number on every rerun.
2. Imagine every button click causes the whole app to restart from scratch. That's a Streamlit rerun. stsession_state is like a sticky note that survives those restarts. Anything you save there stays put between reruns and anything you don't is deleted.
3. Wrapping the random.randint() call in if "secret" not in st.session_state: — so the number is only generated once (the very first run), and every rerun after that just reads the saved value instead of making a new one.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

ANSWER:
1. One habit I want to resuse in the future is creating unit tests for individual funcitons using AI as I fix bugs, to define exactly what is correct.
2. In this project Claude fixed the New Game logic correclty but also broke the UI layout, therefore next time I will look at the diff more carefully to understand what the changes will actually influence before commiting the changes. 
3. AI allowed me too find, explain and debug bugs more easily, however it doesn't understand the full context of what I am trying to keep the same and what I need changed. 