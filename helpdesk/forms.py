from django import forms
from .models import Task, Comment

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        field = ('title', 'desc', 'priority', 'status')
        exclude = ['author', 'status', 'created_at', 'updated_at']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        widgets = {
            'text': forms.Textarea(attrs={'rows': 5, 'cols': 100}),
        }
        field = ('text')

        exclude = ['author', 'created_at', 'task']
