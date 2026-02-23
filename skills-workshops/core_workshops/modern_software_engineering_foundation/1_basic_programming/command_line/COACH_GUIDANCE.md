# Coach Guide: Command Line Workshop

This session covers only the command line—no Git/GitHub or Python. **It is intended to be a short demo with time for Q and A at the end.**

## Timing & Context
* **When to run:** Ideally on Day 2, after onboarding and introductory sessions.
* **Target Audience:** Learners who are either past the command line material or currently embedded within it.
* **Justification:** In a remote environment, it is harder for learners to pick up the "passive" tips and tricks they would usually see by sitting next to a colleague. This session makes those "shortcuts" explicit.

## Session Intro & Concepts

### The Interface
* **Terminal vs. Computer:** Diagram the terminal as an interface (a window) sitting between the human and the computer.
* **The House Analogy:** Explain that you can have multiple terminal windows (iTerm, VS Code terminal, etc.). They are like different windows of a house; you see the same "furniture" (files/folders) inside, just from different vantage points.

### File System Hierarchy
* Diagram the structure: Folders, files, and the **root** directory (`/`).

---

## Live Demonstration Flow

### 1. Handling Errors
* Type a nonsense command (e.g., `abcdef`).
* **Key Lesson:** Teach them to *read* the error. Point out that `zsh` is the reporter, not the command itself failing.

### 2. Navigation & Editing
* **History:** Show `up`/`down` arrows.
* **Cursor:** Show `left`/`right` arrows.
* **Customization:** Mention `home`/`end` keys (keyboards vary). Encourage them to search online for shortcuts and "make the terminal work for you."
* **Deletion:** Demonstrate `Ctrl+w` or `Cmd+w` to remove a whole word. 
* **Backspace vs. Delete:** Note that on many laptops, "Delete" is `Fn + Backspace`.

### 3. Directories & Paths
* **`pwd`:** Show the current location, `cd` somewhere else, and run `pwd` again.
* **The Home Shortcut:** Explain `~` as the home directory.
* **Absolute vs. Relative Paths:**
    * `/` is the root and start of an absolute path.
    * **The "Teammate" Problem:** Explain that coding absolute paths (e.g., `/Users/yourname/...`) breaks code when shared because others don't have your specific directory structure.
* **Navigation Shortcuts:** Demonstrate `..` (e.g., `cd ..` or `ls ../..`).

### 4. Advanced History
* Use the `history` command.
* Demonstrate rerunning a command using the index (e.g., `!1234`).
* Demonstrate `Ctrl+r` for reverse history search.

## Optional Extension Topics
* `ls -l` and `ls -la` (hidden files).
* Environment checks: `which git` and `git --version`.
* File inspection: `vi`, `more`, or `less`.
* Searching: `grep`.
* Documentation: `--help` vs `man` (and when to use each).
