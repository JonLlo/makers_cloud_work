class Student:
    # User-facing properties:
    #   name: string
    #   submissions: list of strings (submission names)

    def __init__(self, name):
        # Parameters:
        #   name: string
        # Side-effects:
        #   Sets the name property and initializes submissions to an empty list
        self.name = name
        self.submissions = []

    def add_submission(self, submission):
        # Parameters:
        #   submission: string (name of the assignment/challenge)
        # Side-effects:
        #   Adds the submission to the submissions property
        self.submissions.append(submission)

    def count_submissions(self):
        # Returns:
        #   The integer count of all submissions made by the student.
        return len(self.submissions)

