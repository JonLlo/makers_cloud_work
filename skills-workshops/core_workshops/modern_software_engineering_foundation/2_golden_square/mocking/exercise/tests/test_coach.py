from unittest.mock import Mock
from lib.coach import Coach

def test_coach_adds_student():
    coach = Coach("Alice")

    mock_student = Mock()
    
    coach.add_student(mock_student)
    assert mock_student in coach.students

def test_can_print_student_names():
    coach = Coach("Bob")
    mock_student_1 = Mock("Jonny")
    mock_student_2 = Mock("Anna")
    coach.add_student(mock_student_1)
    coach.add_student(mock_student_2)
    print(mock_student_1)
    print(mock_student_2)


    



    # Create students
    # Set names
    # Assign students to coach
    # print names

    assert coach.print_student_names() == "John, Paul, George, Ringo"

def test_coach_can_count_submissions():
    # 1. Setup: Create the Coach and some "fake" students
    coach = Coach("Alice")

    # Create students
    # Set count_submissions return value
    # Assign students to coach
    # Count coach submissions
    # Assert that submissions for each student tallys given number

    result = coach.count_submissions()

    assert result == 7