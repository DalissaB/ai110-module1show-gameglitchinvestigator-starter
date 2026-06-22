# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
When I opened it, the settings sidebar was opened. the difficuly levels and their ranges were messed up. It should be Easy = 1-20; Normal = 1-50; Hard = 1-100
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
1) difficuly levels and their ranges were messed up
2) the hints didn't match the relation the guess had with the tatger number


**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|Setting = Hard| The range should be 1-100 | The range was  1-50 | Swapped ranges for hard and normal mode |

| 1 | "Go Higher" since that is the min | "Go lower" which is out of range | "Go lower" |

| New Game | any num 1-20  | 32 | Produces a secret number out of range |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude built into VS Code. It was my first time ever officially using a coding agent straight into my IDE.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Claude caught a bug that related to the range issue I had. It would also generate secret number that were out of the selected range.I verified  this was happening by pressing "New Game" and generating new secret numbers. This error stemmed from the fact the ranges were messed up and I was able to fix that as well.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
Claude caught an error and suggested that I  change the code to receive an int since it was a string. I though this was misleading since I didn't notice a bug that was caused by this.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I went over the logic myself and if it seemed doable and I could understand it myself without the AI, then I pushed it. I ran tests after every bug I fixed. 
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
 Itested inputs 1, 65, 54, and 46 (which was the secret) to ensure that the ranges and hints were right. I also made sure that the secret number was generated within range.
- Did AI help you design or understand any tests? How?
Yes, I ran a pytest as well in which it ran 9 tests verifying all different types of test cases for the bugs we worked on.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?'
This was my first time using Streamlit. I would just descrbie it as a pretty app version of the terminal. For example, when you use Linux in your terminal, you open the vi editor in which you write the code. Running streamlit run app.py is the same ass using g++ and ./a.out to save and run your file.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
I would like to continue using pytests. I liked how it was able to identigy different test cases that might be used to find other bugs in your code or where it will break.
- What is one thing you would do differently next time you work with AI on a coding task?
I need to get used to the interface. VS Code and Claude on one screen can be a little overwhelming.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
You can't just blindly follow it. LAthough it write it for you, you need to verify that it is working as intended. You then must be able to guide it and specifically tell it what you found wrong. At the end of the day, you get the final say in the code.
