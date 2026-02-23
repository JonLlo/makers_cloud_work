# Debugging a web (blog) app

## Learning Objectives

* Use your understanding of how a web application works to debug across the stack.
* Follow the flow of a web application to:
  * find the source of a bug
  * find a way to fix the bug 

## Instructions

In this program, there are many bugs. You have three objectives:

- Find the bugs and fix them. **You can assume that the tests describe the correct behaviour** (so you shouldn't modify anything in the `test/` directory)
- You need to get **all the tests passing**.
- You need to **run the app manually with your browser** and make sure it works. You can have a look at the user stories below to understand how the program is expected to behave (without bugs). 

Previously, you practised this debugging method:

- Tighten the loop (find the _exact line_ the bug is coming from)
- Get visibility (use `print` to inspect everything to help you home in on the exact line)
- Once you know the _one thing_ that is wrong, out of place, misspelled, or not giving you what you expect, try to fix it.

This week, you'll build these skills.  You'll practice:

- Tightening the loop across the whole web stack: from the browser, to a template, to a controller, to a Ruby object, to a test.
- Using error messages and `print` to get visibility in templates, controllers, Python objects and tests.

Note that you don't have to understand **everything** about how this app is working. The process of debugging existing code often involves exploration and trying to work with incomplete knowledge. So it's fine to understand only a part of what the code is doing, as long as this is useful enough to find and fix problems in the app.

## Setup

- Clone the repo
- Make a `venv` and activate it
- Install the dependencies
  - `pip install pytest`
  - `pip install flask`
  - `pip install psycopg`

## Create the databases

- `createdb python_blog_app`
- - `createdb python_blog_app_test`

## Seed the dev database

- `python seed_dev_database.py`

## Run the tests

- Run the tests with `pytest`.

> Some should fail

## Run the app

- Run the app with `python app.py`
- Browse the app at the URL displayed in the terminal

> You should find some broken stuff pretty quickly :)

## User stories

Note that these user stories are **already implemented** by the app — they're here as guidance for you to understand what the program is about and how it should behave when correct.

```
As a developer who likes to blog,
So I can write about my learnings,
I'd like to add a new post on the blog.
```

```
As a developer who likes to read,
So I can read about cool tech things,
I'd like to browse the list of blog posts.
```

```
As a developer who likes to read,
So I can read about the things I'm interested with,
I'd like to browse the list of blog posts having a specific tag.
```
