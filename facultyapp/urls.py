from django.urls import path, include
from . import views

app_name='facultyapp'
urlpatterns = [

    path('facultyhomepage/',views.FacultyHomePage,name="facultyhomepage"),
    path('add_course/',views.add_course,name="add_course"),
    path('view_course/',views.view_student_list,name="view"),
    path('view_marks/',views.post_marks,name="post_marks"),
    path('feedback/', views.submit_feedback, name='feedback'),
    path('feedback/list/', views.feedback_list, name='feedback_list'),
]