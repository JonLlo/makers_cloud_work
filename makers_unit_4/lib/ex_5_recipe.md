# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem


As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.


## 2. Design the Class Interface

'''The interface of a class includes:

The name of the class. ✅
The design of its initializer, the parameters it takes, and their data types
The design of any properties the user will need to read or write, and their data types
The design of its public methods, including:
Their names and purposes
What parameters they take and the data types
What they return and that data type
Any other side effects they might have'''

```python

class TaskTracker:

    def __init__(self):
        self.task_list = []
    
    def add_task(self, task):
        self.task_list.append(task)

    def show_tasks(self):
        return self.task_list
    
    def mark_task_as_complete(task):
        self.task_list.remove(task)
        print(f"task {task} has been removed")


## 3. Create Examples as Tests
'''Test: add_task"'''

def test_show_empty_task:
    pass
def test_add_task_then_show:
    pass
def test_complete_task_then_show:
    pass


#4. Implement the Behaviour






## 3. Create Examples as Tests


_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
