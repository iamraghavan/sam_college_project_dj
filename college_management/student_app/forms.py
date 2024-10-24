from django import forms
from .models import Feedback, Attendance, Marks, FeePayment, StudentLeaveRequest, TeacherLeaveRequest
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['student', 'teacher_name', 'feedback_text']
        widgets = {
            'feedback_text': forms.Textarea(attrs={
                'placeholder': 'Enter your feedback here',
                'rows': 5,
                'class': 'form-control'
            }),
        }

    def clean_feedback_text(self):
        feedback_text = self.cleaned_data.get('feedback_text')
        if len(feedback_text) < 10:
            raise ValidationError("Feedback must be at least 10 characters long.")
        return feedback_text


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'date', 'hours', 'attendance_status']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'hours': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
        }


class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = [
            'student', 'subject',
            'assignment_marks_obtained', 'assignment_marks_out_of',
            'presentation_marks_obtained', 'presentation_marks_out_of',
            'project_marks_obtained', 'project_marks_out_of',
            'exam_marks_obtained', 'exam_marks_out_of'
        ]
        widgets = {
            'assignment_marks_obtained': forms.NumberInput(attrs={'class': 'form-control'}),
            'assignment_marks_out_of': forms.NumberInput(attrs={'class': 'form-control'}),
            'presentation_marks_obtained': forms.NumberInput(attrs={'class': 'form-control'}),
            'presentation_marks_out_of': forms.NumberInput(attrs={'class': 'form-control'}),
            'project_marks_obtained': forms.NumberInput(attrs={'class': 'form-control'}),
            'project_marks_out_of': forms.NumberInput(attrs={'class': 'form-control'}),
            'exam_marks_obtained': forms.NumberInput(attrs={'class': 'form-control'}),
            'exam_marks_out_of': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class FeePaymentForm(forms.ModelForm):
    class Meta:
        model = FeePayment
        fields = ['student', 'amount', 'payment_status']
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }


class StudentLeaveRequestForm(forms.ModelForm):
    class Meta:
        model = StudentLeaveRequest
        fields = ['student', 'leave_reason', 'leave_dates']
        widgets = {
            'leave_dates': forms.TextInput(attrs={'placeholder': 'e.g. 2024-10-20 to 2024-10-25', 'class': 'form-control'}),
            'leave_reason': forms.Textarea(attrs={'class': 'form-control'}),
        }


class TeacherLeaveRequestForm(forms.ModelForm):
    class Meta:
        model = TeacherLeaveRequest
        fields = ['teacher', 'leave_reason', 'leave_dates']
        widgets = {
            'leave_dates': forms.TextInput(attrs={'placeholder': 'e.g. 2024-10-20 to 2024-10-25', 'class': 'form-control'}),
            'leave_reason': forms.Textarea(attrs={'class': 'form-control'}),
        }

