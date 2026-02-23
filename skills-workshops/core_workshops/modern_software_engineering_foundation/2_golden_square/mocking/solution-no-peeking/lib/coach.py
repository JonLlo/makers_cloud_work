
class Coach:
    # User-facing properties:
    #   name: string
    #   students: list of instances of Student

    def __init__(self, name):
        # Parameters:
        #   name: string
        # Side-effects:
        #   Sets the name property and initializes students to an empty list
        self.name = name
        self.students = []

    def add_student(self, student):
        # Parameters:
        #   student: an instance of Student
        # Side-effects:
        #   Adds the student to the students property
        self.students.append(student)

    def count_submissions(self):
        # Returns:
        #   The integer sum of submissions from all students the coach manages. (Delegation)
        return sum(student.count_submissions() for student in self.students)

    def print_student_names(self):
        # Returns:
        #   A string of all student names, separated by ", "
        return ", ".join(student.name for student in self.students)
    
    def upload_submission_for_students(self, submission):
        # Parameters:
        #   submission: string (name of the assignment/challenge)
        # Side-effects:
        #   Calls student.add_submission(submission) on every student the coach manages. (Delegation)
        for student in self.students:
            student.add_submission(submission)
