# Generated by Django 5.1.2 on 2024-10-22 03:26

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("student_id", models.CharField(max_length=20, unique=True)),
                ("surname", models.CharField(max_length=50)),
                ("name", models.CharField(max_length=50)),
                ("date_of_birth", models.DateField()),
                ("email", models.EmailField(max_length=254)),
                ("course", models.CharField(max_length=100)),
                ("previous_subjects", models.TextField()),
                ("extracurricular_activities", models.TextField()),
                ("gender", models.CharField(max_length=10)),
                ("fathers_name", models.CharField(max_length=50)),
                ("mothers_name", models.CharField(max_length=50)),
                ("address", models.TextField()),
                ("student_mobile_number", models.CharField(max_length=15)),
                ("parent_mobile_number", models.CharField(max_length=15)),
                ("admission_date", models.DateField()),
                ("admission_quota", models.CharField(max_length=50)),
                ("religion", models.CharField(max_length=50)),
                ("category", models.CharField(max_length=50)),
                ("blood_group", models.CharField(max_length=3)),
                ("campus_type", models.CharField(max_length=50)),
                ("nationality", models.CharField(max_length=50)),
                ("state", models.CharField(max_length=50)),
                ("district", models.CharField(max_length=50)),
                ("annual_income", models.DecimalField(decimal_places=2, max_digits=10)),
                ("aadhar_number", models.CharField(max_length=14)),
                ("admission_tc_number", models.CharField(max_length=20)),
                (
                    "sslc_percentage",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=5,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100),
                        ],
                    ),
                ),
                (
                    "plus_2_percentage",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=5,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100),
                        ],
                    ),
                ),
                (
                    "ug_percentage",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=5,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100),
                        ],
                    ),
                ),
                (
                    "profile_picture",
                    models.ImageField(
                        blank=True, null=True, upload_to="student_photos/"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Subject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("code", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="Teacher",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("phone", models.CharField(blank=True, max_length=15)),
                ("social_media_links", models.TextField(blank=True)),
                ("location", models.CharField(blank=True, max_length=100)),
                ("bio", models.TextField(blank=True)),
                ("degrees_and_institutions", models.TextField(blank=True)),
                ("certifications", models.TextField(blank=True)),
                ("relevant_courses", models.TextField(blank=True)),
                ("total_years_of_experience", models.PositiveIntegerField(default=0)),
                ("institutions_taught_at", models.TextField(blank=True)),
                ("subjects_and_levels_taught", models.TextField(blank=True)),
                ("subject_matter_expertise", models.TextField(blank=True)),
                ("technical_skills", models.TextField(blank=True)),
                ("soft_skills", models.TextField(blank=True)),
                ("achievements", models.TextField(blank=True)),
                ("teaching_philosophy", models.TextField(blank=True)),
                ("courses_offered", models.TextField(blank=True)),
                ("student_reviews", models.TextField(blank=True)),
                ("professional_development", models.TextField(blank=True)),
                ("languages_spoken", models.CharField(blank=True, max_length=100)),
                ("availability", models.TextField(blank=True)),
                ("hobbies_and_interests", models.TextField(blank=True)),
                (
                    "profile_picture",
                    models.ImageField(
                        blank=True, null=True, upload_to="teacher_photos/"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="FeePayment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("payment_date", models.DateTimeField(auto_now_add=True)),
                (
                    "payment_status",
                    models.CharField(
                        choices=[("paid", "Paid"), ("pending", "Pending")],
                        default="paid",
                        max_length=20,
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="student_app.student",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Feedback",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("teacher_name", models.CharField(max_length=100)),
                ("feedback_text", models.TextField()),
                ("submitted_on", models.DateTimeField(auto_now_add=True)),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="student_app.student",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="StudentLeaveRequest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("leave_reason", models.TextField()),
                ("leave_dates", models.CharField(max_length=100)),
                ("submitted_on", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("approved", "Approved"),
                            ("rejected", "Rejected"),
                        ],
                        default="pending",
                        max_length=20,
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="student_app.student",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TeacherLeaveRequest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("leave_reason", models.TextField()),
                ("leave_dates", models.CharField(max_length=100)),
                ("submitted_on", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("approved", "Approved"),
                            ("rejected", "Rejected"),
                        ],
                        default="pending",
                        max_length=20,
                    ),
                ),
                (
                    "teacher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="student_app.teacher",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Attendance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("hours", models.PositiveIntegerField()),
                (
                    "attendance_status",
                    models.CharField(
                        choices=[("present", "Present"), ("absent", "Absent")],
                        max_length=10,
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="student_app.student",
                    ),
                ),
            ],
            options={
                "unique_together": {("student", "date")},
            },
        ),
        migrations.CreateModel(
            name="Marks",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("assignment_marks_obtained", models.PositiveIntegerField()),
                ("assignment_marks_out_of", models.PositiveIntegerField()),
                ("presentation_marks_obtained", models.PositiveIntegerField()),
                ("presentation_marks_out_of", models.PositiveIntegerField()),
                ("project_marks_obtained", models.PositiveIntegerField()),
                ("project_marks_out_of", models.PositiveIntegerField()),
                ("exam_marks_obtained", models.PositiveIntegerField()),
                ("exam_marks_out_of", models.PositiveIntegerField()),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="student_app.student",
                    ),
                ),
                (
                    "subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="student_app.subject",
                    ),
                ),
            ],
            options={
                "unique_together": {("student", "subject")},
            },
        ),
    ]
