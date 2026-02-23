## Enabling Copilot

IntelliJ comes with GitHub copilot built in, but you will need to log into GitHub from inside your IDE.

### Download / Update

Go to `IntelliJ IDEAD` > `Settings` > `Plugins` and find `GitHub Copilot` in the list.
- If it's not already installed, install it now.
- If it is already installed, you might be prompted to update it – do that now.

### Login

Before you can use Copilot, you'll need to log in to GitHub. To do that go to `Tools` > `GitHub Copilot` > `Login to GitHub` and complete the login step/s.

### Further Guidance

[Further configuration guidance can be found in the official docs](https://docs.github.com/en/copilot/how-tos/configure-personal-settings/configure-in-ide?tool=jetbrains).

## Configuring Copilot

### 1. Implement a `copilot-instructions.md`

Using [custom instructions](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions?tool=jetbrains) means you don't have to explicitly tell the model things like style guidelines in a prompt. It also means that your preferences, whatever they are, will not fall out of context.

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
- Use descriptive variable names in camelCase
- Use ALL_CAPS for constants

## General
- Code should be readable and concise (prioritising the former)
- Use 2 spaces per indentation level
- Limit all lines to a maximum of 79 characters
- Class names should normally use the PascalCase convention
- Code should be correct, clear and concise in that order
- Prioritise readability over performance

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

### 2. Implement a custom prompt

Custom prompts can be used to save you from repeatedly typing out the same boiler plate prompts when, for example, you want to create a new method or function.

According to the official guidance, you *should* be able to create custom prompts by adding a file like `awesome.prompt.md` to `.github/prompts`. It should then be available as a slash command (`/awesome`) in Copilot chat. At the time of writing (13/11/2025) this feature [wasn't working](https://github.com/microsoft/copilot-intellij-feedback/issues/913), so we'll need to find a workaround.

#### A custom prompts workaround

Add a `## Custom Prompts` section to your `copilot-instructions.md`. For example...

```
## Custom Prompts

You should clearly indicate when one of the following prompts is used.

### /refactor
When I start a prompt with /refactor, your job is to refactor the code I've referred to by making it...
- Easier to read
- More concise
- More performant

If I have not referred to any code in the prompt, you should ask me to clarify what exactly I would like to be refactored.

## /break_stuff
When I start a prompt with /break_stuff, your job is to introduce a single bug without explanation
```

### 3. Implement a custom chatmode

There are three built-in chat modes – Ask, Edit and Agent – with differing capabilities. You should be able to add your own but, again, we'll need a workaround for now :/

#### A custom chatmode workaround 

Basic custom chat modes have four properties / parts...

- **Description**, to tells users what this chat mode is for. It will appear as a placeholder in the chat input field.
- **Tools**, which lists the tools your custom chatmode can use. To see a list of built-in tools, go to chatmode and then click on the tools icon underneath the chat input.
- **Model**, to choose which LLM you want your custom chat mode should use.
- The **body**, which is where you provide specific prompts and guidelines which determine how your chatmode will behave.

> In this workaround, it's likely that only the `description` and `body` will do anything meaningful but it's still worth knowing about the other parts.

Add a new chatmode to your `copilot-instructions.md` like this...

```
## Chatmodes

### Planning
---
Description: A chatmode for making plans. Use this mode whenever you are asked to make a plan.
Tools: insert_edit_into_file, replace_string_in_file, create_file, open_file, read_file, file_search
Model: GPT-4.1
---
Body:
You are in planning mode. Your task is to generate an implementation plan for a new feature or for refactoring existing code.
Don't make any code edits, just generate a plan. If needed, you can creatre a plan.md. If a plan.md already exists, update that file. It should be a plan that I can use to implement the changes myself. My current programming skill level is: <INSERT SKILL LEVEL / DESCRIPTION>

The plan should consist of the following sections:

* Overview: A brief description of the feature or refactoring task.
* Requirements: A list of requirements for the feature or refactoring task.
* Implementation Steps: A detailed list of steps to implement the feature or refactoring task.
* Testing: A list of tests that need to be implemented to verify the feature or refactoring task.
```
