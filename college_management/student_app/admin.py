from django.contrib import admin
from .models import (
    Subject, Student, Teacher, Attendance,
    Marks, FeePayment, StudentLeaveRequest,
    TeacherLeaveRequest, Feedback, Classes,Parent
)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('student', 'teacher_name', 'submitted_on', 'feedback_text')  # 'created_at' changed to 'submitted_on'
    search_fields = ('student__name', 'teacher_name')

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'get_subjects', 'courses_offered', 'created_at', 'updated_at')
    search_fields = ('name', 'email')

    def get_subjects(self, obj):
        return ", ".join([subject.name for subject in obj.subjects.all()])  # List the subject names
    get_subjects.short_description = 'Subjects'  # Name displayed in the admin

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'attendance_status', 'hours')
    search_fields = ('student__name',)

class MarksAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'exam_marks_obtained', 'exam_marks_out_of')
    search_fields = ('student__name', 'subject__name')

class FeePaymentAdmin(admin.ModelAdmin):
    list_display = ('student', 'amount', 'payment_date', 'payment_status')
    search_fields = ('student__name',)

class StudentLeaveRequestAdmin(admin.ModelAdmin):
    list_display = ('student', 'leave_reason', 'leave_dates', 'submitted_on', 'status')
    search_fields = ('student__name',)

class TeacherLeaveRequestAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'leave_reason', 'leave_dates', 'submitted_on', 'status')
    search_fields = ('teacher__name',)
    

# Register models with custom admin classes
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Teacher, TeacherAdmin)  # Register Teacher with TeacherAdmin
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Marks, MarksAdmin)
admin.site.register(FeePayment, FeePaymentAdmin)
admin.site.register(StudentLeaveRequest, StudentLeaveRequestAdmin)
admin.site.register(TeacherLeaveRequest, TeacherLeaveRequestAdmin)
admin.site.register(Feedback, FeedbackAdmin)  # Register Feedback with FeedbackAdmin
admin.site.register(Classes)  # Register Feedback with FeedbackAdmin
admin.site.register(Parent)  # Register Feedback with FeedbackAdmin

