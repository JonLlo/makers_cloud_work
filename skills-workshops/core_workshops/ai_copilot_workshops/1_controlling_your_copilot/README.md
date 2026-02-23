# Controlling Your Copilot

## Introduction

Coding copilots like GitHub Copilot are extremely powerful but they can be a little over-zealous at times. If you go into Agent mode and ask it to do something and you'll probably find that multiple files are edited and / or and it'll all snowball out of control.

**How can you rein-in and control your copilot, so that it does what you want and no more?**

### Chat Modes

You can achieve _some_ control be selecting an appropriate chatmode – Ask, Edit or Agent.

- **Ask**, will not make any changes to the codebase. It's basically like using ChatGPT (or similar) and providing it with access to your codebase. Use it to learn about the codebase, about things outside the codebase and / or make plans.
- **Edit**, can make changes but [only to the files that you provide as context](https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-ide?tool=jetbrains#edit-mode-1).
- **Agent**, [can autonomously edit any file in your codebase](https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-ide?tool=jetbrains#agent-mode-1), create new files and run terminal commands.

### Slash Commands

Slash commands are built-in Copilot commands that start with a `/`. You can think of them as prewritten prompts to which you can add your own guidance. For example...

- `/explain this code`
- `/explain this error message`
- `/fix the bugs in this file`
- `/fix how would you improve this code?`

> Doing `/` in chat will bring up a list of all available slash commands. They are super useful, but if you find yourself constantly writing the same guidance, you may prefer to use a custom prompt (which will come to later on).

## Learning Objectives

Learn to use Copilot carefully and thoughtfully by...
- Using `/explain` to first understand the codebase
- Implementing a `copilot-instructions.md`
- Implementing custom prompts and chatmodes (or their equivalent)
- Refactoring some code
- Committing changes frequently!

## A Note on Git

As mentioned, Copilot can wreak havoc on your codebase if you're not careful. Luckily, you have the power of git to save you... but only if you use it properly! By that, we mean you should, now more than ever before, be committing your code frequently. This will allow you to easily revert changes, if needed.

As a rule...

- Use descriptive commit messages
- It's better to make "too many", rather than "too few" commits
- Commit after every 3-4 line changes

## Exercise - Refactor and Extend a Confusing Codebase

The codebases we've provided here are deliberately... awful! :) Your job is to...

- Understand it
- Refactor it
- Extend it

> This will be done in three parts. After each part, there will be a mini plenary where you'll share what you have learned.

### Choose Your Challenge

There are currently three options...

- [Java](./java)
- [JavaScript](./javascript)
- [Python](./python)

### Setup: Enabling and Configure Copilot

Enable and configure Copilot as described in the `README.md` for your chosen challenge.

### Part One: Understand

Before changing any of the code, use Copilot to understand what it's doing. To do this...

1. Open the mystery file (`Mystery.java`, `mystery.py` or `mystery.js`)
2. Open Copilot "chat"
3. Select the "Ask" chatmode
4. Use `/explain` followed by a short prompt. For example...
  - `/explain what this code does in simple terms`
  - `/explain what this code does as if you were from ancient Egypt`
5. Ask follow-up questions, if needed

> Keep chatting until you understand what the code does

### Part Two: Refactor

Now you're ready to improve this horrible codebase using the tools described in the `README.md` for your chosen challenge.

### Part Three: Extend

**If you have time**, consider adding some new features of your choosing to the codebase. To do this...

- Create a **new custom prompt** that can be reused to add several new features
- Use your new prompt to **add new features**

> Not sure what features to add? You could create a custom chatmode to make a plan :)

