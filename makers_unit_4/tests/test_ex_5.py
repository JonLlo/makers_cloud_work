from lib.ex_5 import *


def test_add_task_then_show():
    taskTracker = TaskTracker()
    result = taskTracker.show_tasks()
    assert result == 'No'

def test_add_task_then_show():
    taskTracker = TaskTracker()
    taskTracker.add_task("Data report")
    taskTracker.add_task("Onboarding")
    result = taskTracker.show_tasks()
    assert result == ["Data report", "Onboarding"]

def test_complete_task_then_show():
    taskTracker = TaskTracker()
    taskTracker.add_task("Data report")
    taskTracker.add_task("Onboarding")
    taskTracker.complete_task("Onboarding")
    result = taskTracker.show_tasks()
    assert result == ["Data report"]

    

