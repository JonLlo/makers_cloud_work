# Coach Guidance: DBs From Scratch

In this workshop, you will start by demonstrating how to build a database-backed app from scratch. The intention is not to do this in exactly the same way as we have done in the starter project. Instead, you should start simpler by combining the DatabaseConnection and Repository logic into the Model.


## Intro

Here are the steps to follow...

1. Decide what to build. I built a simple Diary app with an `DiaryEntry` class that is backed by an `entries` table
2. Draw up some requirements for the app
3. Build a simple class with a constructor, some properties and a bit of behaviour
4. Add a `main.py` to use for scripting
5. Demonstrate creating instances of the class in `main.py`
6. Define a method for getting `all` diary entries from `entries`
7. Demonstrate your new `all` method in `main.py`

### Example `DiaryEntry` class

```py
import psycopg
from psycopg.rows import dict_row
from datetime import datetime

class DiaryEntry:

  def __init__(self, content, date = None, id = None):
    self.content = content
    self.date = date if date else datetime.now()
    self.id = id

  def pretty_date(self):
    return self.date.strftime("%a %d %B, %Y - %X")

  @classmethod
  def all(cls):
    connection = psycopg.connect(
      f"postgresql://localhost/diary",
      row_factory=dict_row
    )

    rows = connection.execute('SELECT * from entries')
    entries = []
    for row in rows:
        item = DiaryEntry(row["id"], row["content"], row["date"])
        entries.append(item)
    return entries

```

## Main

Give learners 15-20 mins to work on their choice of exercise. They can choose from...

1. Use a tool like ChatGPT or Copilot to understand the code that already exists
2. Extend the existing codebase without any refactoring
3. Refactor the existing codebase to use the same approach as we've used in the starter codebase, then extend it

## Plenary

Regroup to discuss how everyone got on and reflect on the exercise.
