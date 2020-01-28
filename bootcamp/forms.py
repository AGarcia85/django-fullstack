from django import forms
from .models import Instructor, Post

class InstructorForm(forms.ModelForm):

    class Meta:
        model = Instructor
        fields = ('name', 'photo_url', 'immersive', 'school', 'campus')

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('instructor', 'post', 'date')