
from django import forms
from .models import AddCourse
class AddCourseForm(forms.ModelForm):
    class Meta:
        model = AddCourse
        fields = ['student','course','section']


from .models import Marks
class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = ['student','course','Marks']

from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'phone_number', 'description', 'rating']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring focus:ring-blue-200',
                'placeholder': 'Your Name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring focus:ring-blue-200',
                'placeholder': 'Your Email',
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring focus:ring-blue-200',
                'placeholder': 'Your Phone Number',
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring focus:ring-blue-200',
                'placeholder': 'Enter your feedback here...',
                'rows': 4,
            }),
            'rating': forms.Select(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring focus:ring-blue-200',
            }),
        }
