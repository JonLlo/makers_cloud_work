class TaskTracker:

    def __init__(self):
        self.task_list = []
    
    def add_task(self, task):
        self.task_list.append(task)
        pass

    def show_tasks(self):
        if self.task_list == []:
            return "No"
        return self.task_list

    def complete_task(self, task):
        self.task_list.remove(task)
        print(f"task {task} has been removed")