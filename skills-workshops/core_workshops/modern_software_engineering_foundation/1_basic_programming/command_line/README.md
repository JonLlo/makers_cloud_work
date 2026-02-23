# Command Line Workshop

This workshop focuses exclusively on the **command line**. We will cover how to navigate your computer, manage files, and use shortcuts to speed up your workflow.

---

## Understanding the Terminal

The terminal is a text-based interface that sits between you (the human) and the computer. Think of it as a window that allows you to talk directly to the operating system.

* **Multiple Windows:** You can have several terminal windows open at once.
* **Different "Views":** Whether you use a standalone app like **iTerm2** or the built-in terminal in **VS Code**, they are looking at the same data. It is like looking into a house through different windows—the furniture (your files) remains the same regardless of which window you look through.
* **The File System:** Your computer organises data in a "tree" hierarchy.
* **Root (`/`):** The very top level of your computer.
* **Folders/Directories:** The branches of the tree.
* **Files:** The leaves at the end of the branches.



---

## Editing & Navigation Shortcuts

Making the terminal work for you is about speed and accuracy. Use these shortcuts to move faster and more precisely than you can with a mouse.

### Reading Errors

If you type a command that doesn't exist (e.g., `abcdef`), you will see a **zsh error**.

> **Tip:** Read the error closely. It usually tells you *what* is failing. If it says `zsh: command not found`, it means the shell itself doesn't recognise the word you typed.

### Key Commands

* **Up/Down Arrows:** Cycle through your command history.
* **Left/Right Arrows:** Move the cursor along the current line.
* **Home/End:** Jump to the start or end of a line (on Mac, this is `control + a` or `control + e`).
* **Ctrl + W:** Delete the entire word behind the cursor.
* **Delete vs. Backspace:** On most laptops, **Delete** (removing the character in front of the cursor) is achieved by pressing `Fn + Backspace`.

---

## Directories & Paths

Knowing where you are and where you are going is the most important part of using the terminal.

### Essential Commands

* `pwd`: **Print Working Directory**. Shows you exactly where you are right now.
* `~`: The **Tilde** represents your **Home Directory** (e.g., `/Users/yourname`).
* `..`: Moves you "up" one level in the folder hierarchy (e.g., `cd ..`).
* `history`: Shows a numbered list of every command you've typed recently.
* `Ctrl + R`: Reverse search your history. Start typing a command you used earlier to find it instantly.

### Absolute vs. Relative Paths

* **Absolute Paths:** Start from the **Root (`/`)**. They work from anywhere on the system (e.g., `/Users/name/Projects/my_app`).
* **Relative Paths:** Start from your **current location**. (e.g., `cd documents` only works if you are already in your home folder).

> **Why it matters:** When writing code, **avoid absolute paths**. If you write code that looks for `/Users/paulngilson/my_stuff`, it will break when you give that code to a teammate because they don't have a folder named "paulngilson".

---

## Advanced Commands & Tools

Once you are comfortable navigating, you can use these tools to inspect and manage your system:

| Command | Description |
| --- | --- |
| `ls -l` | List files with detailed information (permissions, size, date). |
| `ls -la` | List **all** files, including hidden ones (like `.env` or `.git`). |
| `which <command>` | Shows the file path of the program you are running (e.g., `which git`). |
| `git --version` | Checks if Git is installed and which version you are using. |
| `vi` / `vim` | A terminal-based text editor for quick file changes. |
| `more` / `less` | View the contents of a file one screen at a time. |
| `grep` | Search for specific text within a file or output. |
| `--help` / `man` | Documentation. Use `--help` for a quick summary or `man <command>` for a full manual. |

---
