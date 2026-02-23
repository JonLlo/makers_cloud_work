# Accelerating Testing

This final AI Copilot workshop is short and focuses tightly on writing tests with Copilot. You can, if you wish, use your own codebases.

## Setup

Choose an existing codebase. If you're working on a project in a team, choose that codebase.

## Getting Copilot to write your tests

This bit is incredibly simple.

1. Open the file containing the code you want to test
2. Highlight the code you want to test
3. Go to Copilot chat, make sure it's in Agent mode and that your selected code is in context, then do `/tests`

Copilot should now busy itself writing tests!

## Getting Copilot to write good tests :)

There are two things you can (and should) try here.

1. Write some guidance in `copilot-instructions.md`
2. Provide more guidance in your prompt. For example, `/tests for the edge cases where a user <does something weird>`

## Your new role

Now that Copilot is able to write some tests for you, your new role is to quality assure those tests.

- Do they make sense? It should be _possible_ for the tests to fail if someone breaks your app – is that the case? If not, they are a bit useless :)
- Are they "brittle"? I.e. Is there a way they could fail when someone changes in the app in some trivial way that, ideally, wouldn't make any tests fail?
- Do the cover all the scenarios you would expect them to?

> What else would you want / not want to see?

