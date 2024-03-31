from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        error_messages = {
            'text': {
                'required': "Пожалуйста, напишите комментарий.",
            }
        }
