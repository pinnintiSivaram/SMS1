from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import AddCourseForm, MarksForm

def FacultyHomePage(request):
    return render(request, 'facultyapp/FacultyHomePage.html')



def add_course(request):
    if request.method == 'POST':
        form = AddCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facultyapp:facultyhomepage')
    else:
        form = AddCourseForm()
    return render(request,'facultyapp/add_course.html',{'form': form})


from .models import AddCourse
from adminapp.models import StudentList

def view_student_list(request):
    course = request.GET.get('course')
    section = request.GET.get('section')
    student_courses = AddCourse.objects.all()
    if course:
        student_courses = student_courses.filter(course=course)
    if section:
        student_courses = student_courses.filter(section=section)
    students = StudentList.objects.filter(id__in=student_courses.values('student_id'))
    course_choices = AddCourse.COURSE_CHOICES
    section_choices = AddCourse.SECTION_CHOICES
    context = {
        'students': students,
        'course_choices': course_choices,
        'section_choices': section_choices,
        'selected_course': course,
        'selected_section': section,
    }
    return render(request, 'facultyapp/view_student_list.html', context)

def post_marks(request):
    if request.method == "POST":
        form = MarksForm(request.POST)
        if form.is_valid():
            marks_instance = form.save(commit=False)
            marks_instance.save()

            # Retrieve the User email based on the student in the form
            student = marks_instance.student
            student_user = student.user
            user_email = student_user.email

            subject = 'Marks Entered'
            message = f'Hello, {student_user.first_name}  marks for {marks_instance.course} have been entered. Marks: {marks_instance.Marks}'
            from_email = 'sivarampinninti@gmail.com'
            recipient_list = [user_email]
            send_mail(subject, message, from_email, recipient_list)

            return render(request, 'facultyapp/post_marks.html')
    else:
        form = MarksForm()
    return render(request, 'facultyapp/post_marks.html', {'form': form})

from django.shortcuts import render, redirect
from .models import Feedback
from .forms import FeedbackForm

# View to submit feedback
def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()  # Save feedback to the database
            return redirect('facultyapp:feedback_list')  # Redirect to feedback list page after submission
    else:
        form = FeedbackForm()

    return render(request, 'facultyapp/submit_feedback.html', {'form': form})

# View to display list of feedback
def feedback_list(request):
    feedbacks = Feedback.objects.all().order_by('-created_at')  # Get all feedbacks, most recent first
    return render(request, 'facultyapp/faculty_feedback_list.html', {'feedbacks': feedbacks})
