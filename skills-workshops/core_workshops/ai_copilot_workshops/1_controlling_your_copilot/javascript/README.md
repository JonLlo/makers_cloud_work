## Enabling Copilot

You can [setup GitHub Copilot for VS Code from within VS Code](https://code.visualstudio.com/docs/copilot/setup?ref_product=copilot&ref_type=engagement&ref_style=text#_set-up-copilot-in-vs-code). If you don't already have a GitHub Copilot subscription, you'll automatically get a free one.

## Configuring Copilot

### 1. Implement a `copilot-instructions.md`

Using [custom instructions](https://code.visualstudio.com/docs/copilot/copilot-customization#_custom-instructions) means you don't have to explicitly tell the model things like style guidelines in a prompt. It also means that your preferences, whatever they are, will not fall out of context.

There are several approaches. We'll use this one for now...
- Create a `.github/copilot-instructions.md`
- Add your instructions!

For example...

```
---
applyTo: "**"
---
# Project general coding standards

## Naming Conventions
- Use descriptive variable names in snake_case
- Use ALL_CAPS for constants

## General
- Code should be readable and concise (prioritising the former)
- Use 4 spaces per indentation level
- Limit all lines to a maximum of 79 characters
- Class names should normally use the CapWords convention
- Code should be written in a way that does not disadvantage other implementations of Python (PyPy, Jython, IronPython, Cython, Psyco, and such)
- Surround top-level function and class definitions with two blank lines.
- Method definitions inside a class are surrounded by a single blank line.

```

Or...

```
---
applyTo: "**"
---
# Project general coding standards

## Naming Conventions
- Make all names of all things as confusing as possible
- Change names of things occasionally just to keep people on their toes

## Style
- Use recursion as much as possible, especially when it's not needed
- Use the most difficult to parse data structures
```


### 2. Implement some custom prompts

*Nobody* likes repetition, right? Prompt files allow you to store your most frequently used prompts, so you don't have to keep typing out "suggest some ways to improve this code" with minor variations. Again, there are several approaches. We're going to use this one...

- Create `.github/prompts/performance.prompt.md`
- Add your prompt (perhaps the one below)
- Do `/performance` (or whatever you renamed your prompt to) in the Chat View to use your prompt

An example prompt...

```
---
mode: 'ask'
model: GPT-4o
tools: ['githubRepo', 'codebase']
description: 'Suggest performance optimisations'
---
Your goal is to suggest performance optimisations for a given block of code.

Requirements:
* Try to assess the likely memory and CPU costs
* Explain these costs and how they might change at scale
* Suggest improvements, explaining any tradeoffs between memory and CPU optimisation

```


### 3. Create a custom chat mode

There are three built-in chat modes – Ask, Edit and Agent – with differing capabilities, but you can also [create your own](https://code.visualstudio.com/docs/copilot/customization/custom-chat-modes).

Basic custom chat modes have four properties / parts...

- **Description**, to tells users what this chat mode is for. It will appear as a placeholder in the chat input field.
- **Tools**, which lists the tools your custom chatmode can use. These can be chosen from the [built-in tools](https://code.visualstudio.com/docs/copilot/reference/copilot-vscode-features#_chat-tools) or they could be third party tools.
- **Model**, to choose which LLM you want your custom chat mode should use.
- The **body**, which is where you provide specific prompts and guidelines which determine how your chatmode will behave.


To get started, create a new file called `planning.chatmode.md` in your `.github` directory. Then paste in the following, which I have largely 'borrowed' from the official docs...


```
---
description: Generate an implementation plan for new features or refactoring existing code.
tools: ['fetch', 'githubRepo', 'search', 'usages']
model: Claude Sonnet 4

---
# Planning mode instructions
You are in planning mode. Your task is to generate an implementation plan for a new feature or for refactoring existing code.
Don't make any code edits, just generate a plan. It should be a plan that I can use to implement the changes myself. My current programming skill level is: <INSERT SKILL LEVEL / DESCRIPTION>

The plan consists of a Markdown document that describes the implementation plan, including the following sections:

* Overview: A brief description of the feature or refactoring task.
* Requirements: A list of requirements for the feature or refactoring task.
* Implementation Steps: A detailed list of steps to implement the feature or refactoring task.
* Testing: A list of tests that need to be implemented to verify the feature or refactoring task.

```

