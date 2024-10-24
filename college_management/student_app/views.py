from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.utils import timezone
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.views import View
from .models import Student,Attendance,Marks,Subject, Teacher, Classes, StudentLeaveRequest, TeacherLeaveRequest
from .forms import AttendanceForm, MarksForm, FeePaymentForm, StudentLeaveRequestForm, TeacherLeaveRequestForm

def homepage(request):
    return render(request, 'bda_college.html')  # Create a homepage.html template

class AdminDashboardView(View):
    def get(self, request):
        return render(request, 'admin_dashboard.html')

class StudentDashboardView(View):   
    def get(self, request):
        return render(request, 'student_dashboard.html')

class ParentDashboardView(View):
    def get(self, request):
        return render(request, 'parent_dashboard.html')

class TeacherDashboardView(View):
    def get(self, request):
        return render(request, 'teacher_dashboard.html')

class StudentProfileEditView(UpdateView):
    model = Student
    template_name = 'student_app/student_profile_edit.html'  
    fields = ['name', 'email', 'grade']

    def get_object(self, queryset=None):
        student_id = self.kwargs.get("student_id")
        return get_object_or_404(Student, id=student_id)

# Utility function for rendering templates
def render_template(request, template_name):
    return render(request, template_name)

# Admin Dashboard
def admin_dashboard(request):
    return render_template(request, 'admin_dashboard.html')

# Attendance Edit
def attendance_edit(request):

    if request.method == 'POST':
        if request.method == 'POST':
            # Collect data from the request
            reg_no = request.POST.get('reg_no')
            date = request.POST.get('date')
            hours = request.POST.get('hours')
            attendance_status = request.POST.get('present')

            # Fetch the student based on the register number or name
            try:
                student = Student.objects.get(student_id=reg_no)  # Adjust based on your model
            except Student.DoesNotExist:
                return HttpResponse("Student not found.", status=404)

            # Print data for debugging
            print(f"Register Number: {reg_no}")
            print(f"Date: {date}")
            print(f"Hours: {hours}")
            print(f"Attendance Status: {attendance_status}")

            # Save the attendance record
            attendance_record, created = Attendance.objects.update_or_create(
                student=student,
                date=date,
                defaults={'hours': hours, 'attendance_status': attendance_status}
            )
            print("Successfully added")
            return render(request, 'attendance_edit.html',{'message':'Successfully added'})
    return render(request, 'attendance_edit.html')

# Consolidated Report
def consolidated_report(request):
    return render_template(request, 'consolidated_report.html')

# Enter Attendance
def enter_attendance(request):
    return render_template(request, 'enter_attendance.html')

# Exam Application Page
def exam_application_page(request):
    return render_template(request, 'exam_application_page.html')

# Marks Edit
def marks_edit(request):
    if request.method == 'POST':
        # Collect data from the request
        student_id = request.POST.get('student-id')
        subject_name = request.POST.get('subject')
        
        # Marks information
        assignment_marks_obtained = request.POST.get('assignment-marks')
        assignment_marks_out_of = request.POST.get('assignment-out-of')
        presentation_marks_obtained = request.POST.get('presentation-marks')
        presentation_marks_out_of = request.POST.get('presentation-out-of')
        project_marks_obtained = request.POST.get('project-marks')
        project_marks_out_of = request.POST.get('project-out-of')
        exam_marks_obtained = request.POST.get('exam-marks')
        exam_marks_out_of = request.POST.get('exam-out-of')

        try:
            # Fetch the student and subject based on input
            student = Student.objects.get(id=student_id)  # Adjust as needed based on your model
            subject = Subject.objects.get(name=subject_name.lower())  # Adjust if needed

            # Create and save the marks object
            marks_record = Marks(
                student=student,
                subject=subject,
                assignment_marks_obtained=assignment_marks_obtained,
                assignment_marks_out_of=assignment_marks_out_of,
                presentation_marks_obtained=presentation_marks_obtained,
                presentation_marks_out_of=presentation_marks_out_of,
                project_marks_obtained=project_marks_obtained,
                project_marks_out_of=project_marks_out_of,
                exam_marks_obtained=exam_marks_obtained,
                exam_marks_out_of=exam_marks_out_of
            )
            marks_record.save()

            return render(request, 'Marks_edit.html',{'message':"Successfully added"}) # Success message
        except (Student.DoesNotExist, Subject.DoesNotExist) as e:
            return HttpResponse(f"Error: {str(e)}", status=404)
    return render(request, 'Marks_edit.html',)

# Fees Payment
@login_required
def fees_payment(request):
    if request.method == 'POST':
        form = FeePaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_app:admin_dashboard')
    else:
        form = FeePaymentForm()
    return render(request, 'submit_fee_payment.html', {'form': form})

# Login Functionality
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')  

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)  
            return redirect({
                'admin': 'student_app:admin_dashboard',
                'student': 'student_app:student_dashboard',
                'parent': 'student_app:parent_dashboard',
                'teacher': 'student_app:teacher_dashboard'
            }.get(user_type, 'login'))  # Default to login if user_type is invalid
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')

def attendance(request):
    # Your code for handling attendance here
    return render(request, 'attendance.html')

def update_fees(request):
    # Your logic for updating fees here
    return render(request, 'fees_edit_page.html')

def leave_response_page(request):
    # Your logic for the leave response page here
    return render(request, 'leave_response_page.html')

def manage_classes(request):
    classes = Classes.objects.all()
    return render(request, 'manage_classes.html',{'classes':classes})

def manage_students(request):
    students = Student.objects.all()  # Fetch all students
    return render(request, 'manage_students.html', {'students': students})


def manage_teachers_permissions(request):
    # Logic to manage classes
    return render(request, 'manage_teachers_permissions.html')

def manage_teachers(request):
    # students = Student.objects.all() 
    teachers = Teacher.objects.all()
    return render(request, 'manage_teachers.html', {'teachers':teachers})

def parent_dashboard(request):
    # Logic to manage classes
    return render(request, 'parent_dashboard.html')

def student_dashboard(request):
    # Logic to manage classes
    return render(request, 'student_dashboard.html')

@login_required
def student_leave_request_submission(request):
    if request.method == 'POST':
        # Get form data from the POST request
        reg_no = request.POST.get('regNo')
        name = request.POST.get('name')
        leave_reason = request.POST.get('leaveReason')
        leave_dates = request.POST.get('leaveDates')

        # Fetch the Student object using the registration number (assuming reg_no is unique)
        try:
            student = Student.objects.get(student_id=reg_no)
        except Student.DoesNotExist:
            return HttpResponse("Student with this Register Number does not exist", status=404)

        # Create a new leave request instance
        leave_request = StudentLeaveRequest(
            student=student,
            leave_reason=leave_reason,
            leave_dates=leave_dates,
            submitted_on=timezone.now(),
            status=False 
        )
        
        # Save the instance to the database
        leave_request.save()

        # Redirect or return success response
        return render(request, 'student_leave_request_submission.html',{'message':"Succesfully added"})
    return render(request, 'student_leave_request_submission.html')

def student_leave_status(request):
    # Logic to manage classes
    student = request.user.student  # OneToOneField connection to Student model

    # Fetch all leave requests for this student
    leave_requests = StudentLeaveRequest.objects.filter(student=student)
    return render(request, 'student_leave_status.html',{'leave_requests':leave_requests})

def student_profile_edit_page(request):
    # Logic to manage classes
    return render(request, 'student_profile_edit_page.html')

@login_required
def student_profile(request):
    current_user = request.user
    return render(request, 'student_profile.html',{"user":current_user})

def student_exam_application(request):
    # Logic to manage classes
    return render(request, 'student_exam_application.html')

@login_required
def subject_wise_report(request):
    user = request.user
    student = user.student
    attendance = Attendance.objects.filter(student=student)
    return render(request, 'subject_wise_report.html',{'attendance':attendance})

@login_required
def View_attendance_parent(request):
    user = request.user
    parent = user.parent
    student = parent.student
    attendance = Attendance.objects.filter(student=student)
    return render(request, 'subject_wise_report.html',{'attendance':attendance})

def teacher_dashboard(request):
    return render(request,'teacher_dashboard.html')

def teacher_leave_request(request):
    if request.method == 'POST':
        # Get form data from the POST request
        name = request.POST.get('name')
        leave_reason = request.POST.get('leaveReason')
        leave_dates = request.POST.get('leaveDates')

        # Fetch the Student object using the registration number (assuming reg_no is unique)
        try:
            teacher = Teacher.objects.get(name=name)
        except Teacher.DoesNotExist:
            return HttpResponse("Teacher does not exist", status=404)

        try:
            leave_request = TeacherLeaveRequest(
                teacher=teacher,
                leave_reason=leave_reason,
                leave_dates=leave_dates,
                submitted_on=timezone.now(),
                status=False 
            )
            leave_request.save()
            return render(request, 'teacher_leave_request.html',{'message':"Succesfully added"})
        except:
            return render(request, 'teacher_leave_request.html',{'message':"Error"})
    return render(request, 'teacher_leave_request.html')

def teacher_leave_response(request):
    teacher = request.user.teacher
    leave_requests = TeacherLeaveRequest.objects.filter(teacher=teacher)
    return render(request, 'teacher_leave_response.html',{'leave_requests':leave_requests})

def teacher_profile_page(request):
    # Logic to manage classes
    return render(request, 'teacher_profile_page.html')

def View_attendance(request):
    # Logic to manage classes
    return render(request, 'View_attendance.html')

def view_fees(request):
    # Logic to manage classes
    return render(request, 'view_fees.html')

@login_required
def View_marks(request):
    user = request.user
    student = user.student
    marks = Marks.objects.filter(student=student)
    return render(request, 'View_marks.html',{'marks':marks})

@login_required
def View_marks_parent(request):
    user = request.user
    parent = user.parent
    student = parent.student
    marks = Marks.objects.filter(student=student)
    return render(request, 'View_marks.html',{'marks':marks})

def view_teacher_profile(request):
    user = request.user
    teacher = user.teacher
    return render(request, 'view_teacher_profile.html',{'teacher':teacher})

# Submit Attendance
@login_required
def submit_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_app:admin_dashboard')
    else:
        form = AttendanceForm()
    return render(request, 'submit_attendance.html', {'form': form})

# Submit Marks
@login_required
def submit_marks(request):
    if request.method == 'POST':
        form = MarksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_app:admin_dashboard')
    else:
        form = MarksForm()
    return render(request, 'Marks_edit.html', {'form': form})

# Student Leave Request Submission
@login_required
def submit_student_leave_request(request):
    if request.method == 'POST':
        form = StudentLeaveRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_app:student_dashboard')
    else:
        form = StudentLeaveRequestForm()
    return render(request, 'student_leave_request_submission.html', {'form': form})

# Teacher Leave Request Submission
@login_required
def submit_teacher_leave_request(request):
    if request.method == 'POST':
        form = TeacherLeaveRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_app:teacher_dashboard')
    else:
        form = TeacherLeaveRequestForm()
    return render(request, 'submit_teacher_leave_request.html', {'form': form})
