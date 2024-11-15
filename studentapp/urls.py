from django.urls import path, include
from . import views
app_name='studentapp'
urlpatterns = [
path('studenthomepage/',views.StudentHomePage,name="studenthomepage"),
path('view_marks/',views.view_marks,name="marks"),
]