from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=20, unique=True)
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField()
    course = models.CharField(max_length=100)
    previous_subjects = models.TextField()
    extracurricular_activities = models.TextField()
    gender = models.CharField(max_length=10)
    fathers_name = models.CharField(max_length=50)
    mothers_name = models.CharField(max_length=50)
    address = models.TextField()
    student_mobile_number = models.CharField(max_length=15)
    parent_mobile_number = models.CharField(max_length=15)
    admission_date = models.DateField()
    admission_quota = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=3)
    campus_type = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    annual_income = models.DecimalField(max_digits=10, decimal_places=2)
    aadhar_number = models.CharField(max_length=14)
    admission_tc_number = models.CharField(max_length=20)
    sslc_percentage = models.DecimalField(
        max_digits=5, decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    plus_2_percentage = models.DecimalField(
        max_digits=5, decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    ug_percentage = models.DecimalField(
        max_digits=5, decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    profile_picture = models.ImageField(upload_to='student_photos/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.surname} ({self.student_id})"
    

class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='parent')
    student = models.OneToOneField('Student', on_delete=models.CASCADE, related_name='parent')
    name = models.CharField(max_length=100)  # Parent's name
    email = models.EmailField(unique=True)    # Parent's email (optional, can be unique)
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Parent's phone number
    address = models.TextField(blank=True, null=True)  # Parent's address (optional)
    relationship = models.CharField(max_length=50, default='Mother')  # Relationship to student (e.g., Mother, Father)

    def __str__(self):
        return f"{self.name} - {self.relationship}"


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True)
    subjects = models.ManyToManyField(Subject, blank=True)  # Change to ManyToManyField
    courses_offered = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.email})"


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    hours = models.PositiveIntegerField()
    attendance_status = models.CharField(max_length=10, choices=[('present', 'Present'), ('absent', 'Absent')])

    class Meta:
        unique_together = ('student', 'date')

    def __str__(self):
        return f"{self.student.name} - {self.attendance_status} on {self.date}"


class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    assignment_marks_obtained = models.PositiveIntegerField()
    assignment_marks_out_of = models.PositiveIntegerField()
    presentation_marks_obtained = models.PositiveIntegerField()
    presentation_marks_out_of = models.PositiveIntegerField()
    project_marks_obtained = models.PositiveIntegerField()
    project_marks_out_of = models.PositiveIntegerField()
    exam_marks_obtained = models.PositiveIntegerField()
    exam_marks_out_of = models.PositiveIntegerField()

    class Meta:
        unique_together = ('student', 'subject')

    def __str__(self):
        return f"{self.student.name} - {self.subject.name}"


class FeePayment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=20, choices=[('paid', 'Paid'), ('pending', 'Pending')], default='paid')

    def __str__(self):
        return f"Payment of {self.amount} for {self.student.name} on {self.payment_date.strftime('%Y-%m-%d')}"


class StudentLeaveRequest(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    leave_reason = models.TextField()
    leave_dates = models.CharField(max_length=100)
    submitted_on = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField()

    def __str__(self):
        return f"Leave Request by {self.student.name} from {self.leave_dates} (Status: {self.status})"


class TeacherLeaveRequest(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    leave_reason = models.TextField()
    leave_dates = models.CharField(max_length=100)
    submitted_on = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField()
    def __str__(self):
        return f"Leave Request by {self.teacher.name} from {self.leave_dates} (Status: {self.status})"


class Feedback(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher_name = models.CharField(max_length=100)
    feedback_text = models.TextField()
    submitted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.student.name} for {self.teacher_name} on {self.submitted_on}"
    
class Classes(models.Model):
    class_name = models.TextField(max_length=255)
    teacher_name = models.TextField(max_length=255)
    capacity = models.IntegerField()
