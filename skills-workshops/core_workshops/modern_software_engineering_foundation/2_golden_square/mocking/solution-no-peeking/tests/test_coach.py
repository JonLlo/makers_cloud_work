from unittest.mock import Mock
from lib.coach import Coach

def test_coach_adds_student():
    coach = Coach("Alice")

    mock_student = Mock()
    
    coach.add_student(mock_student)
    assert mock_student in coach.students

def test_can_print_student_names():
    coach = Coach("Bob")
    
    mock_student_1 = Mock()
    mock_student_2 = Mock()
    mock_student_3 = Mock()
    mock_student_4 = Mock()

    mock_student_1.name = "John"
    mock_student_2.name = "Paul"
    mock_student_3.name = "George"
    mock_student_4.name = "Ringo"

    coach.add_student(mock_student_1)
    coach.add_student(mock_student_2)
    coach.add_student(mock_student_3)
    coach.add_student(mock_student_4)

    assert coach.print_student_names() == "John, Paul, George, Ringo"

def test_coach_can_count_submissions():
    # 1. Setup: Create the Coach and some "fake" students
    coach = Coach("Alice")
    
    mock_student_1 = Mock()
    mock_student_2 = Mock()

    mock_student_1.count_submissions.return_value = 2
    mock_student_2.count_submissions.return_value = 5
    
    coach.add_student(mock_student_1)
    coach.add_student(mock_student_2)
    
    result = coach.count_submissions()
    
    assert result == 7

def test_coach_delegates_upload_to_all_students_manual_tracker():
    coach = Coach("Alice")
    
    mock_student_1 = Mock()
    mock_student_2 = Mock()
    
    mock_student_1.submissions_received = []
    mock_student_2.submissions_received = []
    
    def fake_add_submission_1(title):
        mock_student_1.submissions_received.append(title)
        
    def fake_add_submission_2(title):
        mock_student_2.submissions_received.append(title)
        
    mock_student_1.add_submission = fake_add_submission_1
    mock_student_2.add_submission = fake_add_submission_2
    
    coach.add_student(mock_student_1)
    coach.add_student(mock_student_2)
    
    coach.upload_submission_for_students("Final Project")
    
    assert len(mock_student_1.submissions_received) == 1
    assert mock_student_1.submissions_received[0] == "Final Project"
    
    assert len(mock_student_2.submissions_received) == 1
    assert mock_student_2.submissions_received[0] == "Final Project"