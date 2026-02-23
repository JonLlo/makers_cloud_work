

## 📋 Coach Facing Guidance: Truth, Falsy, and Other Traps

### Session Strategy

This session works best when it feels like a series of "puzzles." The goal is to encourage participation via guesses and then reveal the surprising reality of Python's logic.

### Workshop Content & "Traps"

#### 1. The Memory Maze (Mutable vs. Immutable)

Demonstrate how lists and integers handle assignment differently.

* **Integer Trap:** Show that `int_b = int_a` creates a separate value when `int_a` is incremented.
* **List Trap:** Show that `new_list = list` creates a reference. Changing `list` changes `new_list`.
* **The Fix:** Introduce `.copy()` as the way to create a truly independent list.

#### 2. Truthy vs. Falsy Values

Explore how Python evaluates non-boolean types in `if` and `while` statements.

* **The String Trap:** Run `if "z" or "x" in s:`. This is the "big" trap. Because `"z"` is a non-empty string, Python evaluates it as `True` immediately, regardless of what is in `s`.
* **Testing Types:** Cycle through different types to find the "Falsy" ones:
* **Integers:** `0` is Falsy; everything else (including negative numbers) is Truthy.
* **Collections:** `[]`, `{}`, and `""` are Falsy.
* **The "Evil" Dictionary:** Show that `{"": 0}` is actually **Truthy** because the dictionary itself is not empty.



#### 3. Practical Application

Show how "Truthiness" can be useful for concise logic.

* **The Countdown:** Use a `while num:` loop, where `num` is a number which is steadily decremented. It’s a clean way to run a loop until a counter hits zero without needing an explicit `> 0` check.

### Facilitation Tips

* **Don't Spoil the Surprise:** When running the "Truthy" string examples, don't explain the logic until the learners have seen the surprising result.
* **The "House Address" Analogy:** Explain that `new_list = list` isn't moving furniture to a new house; it's just giving two people the same address. If one person paints the front door, the other person sees a painted door.
