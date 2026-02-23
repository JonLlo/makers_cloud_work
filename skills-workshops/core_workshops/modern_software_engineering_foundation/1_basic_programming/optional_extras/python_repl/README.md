## Python REPL Workshop

### What is the REPL?

REPL stands for **Read-Eval-Print Loop**. It is the interactive heart of Python. When you type `python3` in your terminal without a file name, you enter a sandbox where Python reads your code, evaluates it, and prints the result immediately.

### 💡 Tips, Tricks, and Traps

#### 1. Returning vs. Printing

There is a big difference between a function **returning** a value and **printing** one:

* **`s.upper()`**: This creates and **returns** a brand-new string. You can assign this to a variable: `t = s.upper()`.
* **`print(s)`**: This is for humans. It shows you the value on the screen but returns `None`. You cannot "save" the output of a print statement into a variable for later use.

#### 2. Discovery via Tabbing

The `Tab` key is your best friend for discovery.

* Type `s.` and press `Tab` twice. Python will show you every method available for that string.
* Start typing `s.u` and press `Tab` to auto-complete `s.upper()`.

#### 3. Chaining

You can link methods together in a single line. Python resolves them from left to right.

* **Example:** `a.upper().strip()[0]`
* This takes a string, makes it uppercase, removes the surrounding whitespace, and then grabs the first character.

#### 4. The "In-Place" Trap

Be careful with how Python handles different data types, especially lists:

* **`sorted(my_list)`**: Returns a *new* sorted list. The original list stays exactly as it was.
* **`my_list.sort()`**: Changes the *original* list directly ("in-place") and returns `None`.

### Why use the REPL?

While we use VS Code to write scripts and save our work, the REPL is a powerful "sandbox." Use it to:

* **Experiment:** Test a small bit of logic before putting it in your main code.
* **Discover:** See what methods are available for an object you've just created.
* **Debug:** Load your own files into the REPL to test functions individually:
```bash
python3 -i your_file.py

```
