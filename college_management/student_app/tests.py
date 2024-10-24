from django.test import TestCase
from .models import Student, Teacher, Feedback, Attendance, Marks, FeePayment, StudentLeaveRequest, TeacherLeaveRequest

class StudentModelTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            name='John Doe',
            roll_number='123',
            email='john@example.com'
        )

    def test_student_creation(self):
        self.assertEqual(self.student.name, 'John Doe')
        self.assertEqual(self.student.roll_number, '123')
        self.assertEqual(self.student.email, 'john@example.com')

class TeacherModelTest(TestCase):
    def setUp(self):
        self.teacher = Teacher.objects.create(
            name='Jane Smith',
            subject='Mathematics',
            email='jane@example.com'
        )

    def test_teacher_creation(self):
        self.assertEqual(self.teacher.name, 'Jane Smith')
        self.assertEqual(self.teacher.subject, 'Mathematics')
        self.assertEqual(self.teacher.email, 'jane@example.com')

class FeedbackModelTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(name='John Doe', roll_number='123', email='john@example.com')
        self.teacher = Teacher.objects.create(name='Jane Smith', subject='Mathematics', email='jane@example.com')
        self.feedback = Feedback.objects.create(student=self.student, teacher_name=self.teacher, feedback_text='Great job!')

    def test_feedback_creation(self):
        self.assertEqual(self.feedback.feedback_text, 'Great job!')
        self.assertEqual(self.feedback.student, self.student)
        self.assertEqual(self.feedback.teacher_name, self.teacher)

class AttendanceModelTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(name='John Doe', roll_number='123', email='john@example.com')
        self.attendance = Attendance.objects.create(student=self.student, date='2024-10-01', hours=8, attendance_status='Present')

    def test_attendance_creation(self):
        self.assertEqual(self.attendance.student, self.student)
        self.assertEqual(self.attendance.date, '2024-10-01')
        self.assertEqual(self.attendance.hours, 8)
        self.assertEqual(self.attendance.attendance_status, 'Present')

class MarksModelTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(name='John Doe', roll_number='123', email='john@example.com')
        self.marks = Marks.objects.create(
            student=self.student,
            subject='Mathematics',
            assignment_marks_obtained=15,
            assignment_marks_out_of=20,
            presentation_marks_obtained=18,
            presentation_marks_out_of=20,
            project_marks_obtained=20,
            project_marks_out_of=20,
            exam_marks_obtained=80,
            exam_marks_out_of=100
        )

    def test_marks_creation(self):
        self.assertEqual(self.marks.student, self.student)
        self.assertEqual(self.marks.subject, 'Mathematics')
        self.assertEqual(self.marks.assignment_marks_obtained, 15)
        self.assertEqual(self.marks.assignment_marks_out_of, 20)
        self.assertEqual(self.marks.exam_marks_obtained, 80)

class FeePaymentModelTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(name='John Doe', roll_number='123', email='john@example.com')
        self.fee_payment = FeePayment.objects.create(student=self.student, amount=5000, payment_status='Paid')

    def test_fee_payment_creation(self):
        self.assertEqual(self.fee_payment.student, self.student)
        self.assertEqual(self.fee_payment.amount, 5000)
        self.assertEqual(self.fee_payment.payment_status, 'Paid')

class StudentLeaveRequestModelTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(name='John Doe', roll_number='123', email='john@example.com')
        self.leave_request = StudentLeaveRequest.objects.create(student=self.student, leave_reason='Medical', leave_dates='2024-10-10 to 2024-10-15')

    def test_student_leave_request_creation(self):
        self.assertEqual(self.leave_request.student, self.student)
        self.assertEqual(self.leave_request.leave_reason, 'Medical')
        self.assertEqual(self.leave_request.leave_dates, '2024-10-10 to 2024-10-15')

class TeacherLeaveRequestModelTest(TestCase):
    def setUp(self):
        self.teacher = Teacher.objects.create(name='Jane Smith', subject='Mathematics', email='jane@example.com')
        self.leave_request = TeacherLeaveRequest.objects.create(teacher=self.teacher, leave_reason='Personal', leave_dates='2024-10-20 to 2024-10-25')

    def test_teacher_leave_request_creation(self):
        self.assertEqual(self.leave_request.teacher, self.teacher)
        self.assertEqual(self.leave_request.leave_reason, 'Personal')
        self.assertEqual(self.leave_request.leave_dates, '2024-10-20 to 2024-10-25')

