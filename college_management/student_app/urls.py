from django.urls import path
from .views import *
from . import views

app_name = 'student_app'

urlpatterns = [
    path('', homepage, name='home'),
    path('login/',views.login, name='login'),  # Ensure this name matches
    path('admin/dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('student/dashboard/', StudentDashboardView.as_view(), name='student_dashboard'),
    path('parent/dashboard/', ParentDashboardView.as_view(), name='parent_dashboard'),
    path('teacher/dashboard/', TeacherDashboardView.as_view(), name='teacher_dashboard'),
    path('student_profile_edit/',student_profile_edit_page, name='student_profile_edit'),
    path('admin_dashboard/',admin_dashboard, name='admin_dashboard'),
    path('attendance_edit/', attendance_edit, name='attendance_edit'),
    path('attendance/',attendance, name='attendance'),
    path('consolidated_report/',consolidated_report, name='consolidated_report'),
    path('enter_attendance/',enter_attendance, name='enter_attendance'),
    path('exam_application_page/',exam_application_page, name='exam_application_page'),
    path('update_fees/',update_fees, name='update_fees'),  # Updated route
    path('fees_payment/',fees_payment, name='fees_payment'), 
    path('leave_response_page/',leave_response_page, name='leave_response_page'), 
    path('manage_classes/',manage_classes, name='manage_classes'),
    path('manage_students/',manage_students, name='manage_students'),
    path('marks_edit/', views.marks_edit, name='marks_edit'),
    path('parent_dashboard/',parent_dashboard, name='parent_dashboard'),
    path('student_dashboard/',student_dashboard, name='student_dashboard'),
    path('student_exam_application/', student_exam_application, name='student_exam_application'),
    path('student_leave_request_submission/',student_leave_request_submission, name='student_leave_request_submission'),
    path('student_leave_status/',student_leave_status, name='student_leave_status'),
    path('student_profile_edit/',student_profile_edit_page, name='student_profile_edit'),
    path('student_profile/',student_profile, name='student_profile'),
    path('subject_wise_report/',subject_wise_report, name='subject_wise_report'),
    path('teacher_dashboard/',teacher_dashboard, name='teacher_dashboard'),
    path('teacher_leave_request/',teacher_leave_request, name='teacher_leave_request'),
    path('teacher_leave_response/',teacher_leave_response, name='teacher_leave_response'),
    path('teacher_profile_page/',teacher_profile_page, name='teacher_profile_page'),
    path('View_attendance/',View_attendance, name='View_attendance'),
    path('view_fees/',view_fees, name='view_fees'),
    path('View_marks/',View_marks, name='View_marks'),
    path('view_teacher_profile/',view_teacher_profile, name='view_teacher_profile'),
    path('submit_attendance/',submit_attendance, name='submit_attendance'),
    path('submit_student_leave_request/',submit_student_leave_request, name='submit_student_leave_request'),
    path('submit_teacher_leave_request/',submit_teacher_leave_request, name='submit_teacher_leave_request'),
    path('manage_teachers/',manage_teachers, name='manage_teachers'),
    path('manage_teachers_permissions/',manage_teachers_permissions, name='manage_teachers_permissions'),
    path('View_attendance_parent/',View_attendance_parent, name='View_attendance_parent'),
    path('View_marks_parent/',View_marks_parent, name='View_marks_parent'),
]