# Coach Guidance: Golden Square Debugging

## Intro

Introduce the topic and then work through the following parts. When you demo different tools, try not to actually fix the bugs! Just demonstrate getting visibility / tracking down the problem.

### Temperature Check

Ask the learners: *“Does debugging feel like a chaotic guessing game, or a structured investigation?”*

> Get them to answer the question by privately messaging you on Zoom

### Session Strategy

In this workshop you are demonstrating the "detective's mindset." The goal is to show that no single tool is a silver bullet; rather, a combination of the REPL, strategic printing, and the debugger provides the visibility needed to solve complex logic issues.

### Demo 1: "Change Debugging"

* **The Problem:** Use the provided `code.py` (the text wrapper).
* **The First Trap:** Run `wrap_text("hello lovely people", 22)`. The words appear in reverse order.
* **The "Guess":** Speculate that `pop()` is the culprit. Show how `pop()` works in the REPL.
* **The Fix:** Change to `words.pop(0)`.
* **Coach Tip:** Deliberately forget to reload the code in the REPL after the fix to demonstrate that the REPL isn't dynamic. This is a vital "mini-lesson" for learners.

### Demo 2: Gaining Visibility

* **Visual Aids:** When things get complex, add "ruler" lines to the output.
* Change line 10 to: `lines = ["-"*limit]`.
* **The Trace:** Add `print(line_so_far)` inside the `while` block.
* **The Discovery:** This reveals a leading space issue. Work with the learners to implement the `if count_so_far == 0` logic to handle the first word on a line correctly.

### Demo 3: The VS Code Interactive Debugger

* **The "Missing Word" Mystery:** Run a longer string: *"The quick brown fox jumped over the lazy dogs"*. One word will vanish.
* **The Tool:** Transition from print statements to the **VS Code Debugger**.
* **The Solution:** Show how the `else` block drops the current `word` because it isn't added back to the list or the current line.
* **The "Magic" Trick:** While paused in the debugger, use the **Debug Console** to change variable values on the fly (e.g., changing the word "jumped" to "ju") to show how it affects the logic immediately.

## Main

Give the learners 20-30 mins to fix the bugs using the approaches you have demonstrated. If they work in pairs, they can take turns to observe and give feedback on each other's process.

## Plenary

Regroup and work though a few of the bugs, under the guidance of the cohort.

Wrap up by revisiting the "Temperature Check." Ask the learners: *“Does debugging feel like a chaotic guessing game, or a structured investigation now?”*
