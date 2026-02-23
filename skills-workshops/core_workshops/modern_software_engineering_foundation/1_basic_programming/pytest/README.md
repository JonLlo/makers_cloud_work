# Pytest Workshop

## Why this session exists

This session is designed to help you get comfortable with `pytest`’s output and learn how to use it as a powerful debugging tool. Common hurdles we will address include:

* **Understanding Error Messages:** Learning what the output actually means rather than guessing.
* **Deciphering Symbols:** Knowing exactly what the `+` and `-` symbols mean in a diff.
* **Getting More Info:** Knowing when and how to use `-v` or `-vv` to see more information.
* **Spotting Differences:** Noticing small discrepancies between what was returned and what was expected.

## Setup

Run the following commands in your terminal to prepare your environment:

```bash
python3 -m venv venv_name
source venv_name/bin/activate
pip install pytest
code .

```

Confirm that the setup is working by running the tests. You should see multiple failures—this is expected!

```bash
pytest

```

## How the session works

The session takes about **30–60 minutes**. First, your coach will introduce the session and demonstrate the task, then you will continue using this three step process...

1. **Step 1: Understand pytest output**
Run `pytest -x` to stop at the first failure. Before looking at your code, analyse the terminal: Where is the error? What line numbers are mentioned? What is the difference between the `+` and `-` lines?
1. **Step 2: Fix the code**
Only after discussing the output should you open the relevant file. Update the code based on the error message and rerun the test.
1. **Step 3: Repeat**
Work through the remaining failures one by one. With each one, focus on **reading** before **fixing**.
