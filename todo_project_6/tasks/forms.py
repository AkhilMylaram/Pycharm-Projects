from django import forms
from pyexpat import model

from tasks.models import Task, Tag


# from model we have Task with some attributes we need to create a form for that
# instead of typing the each and every attribure of the model class Task and making the fields like above
# django provides a models forms which will inherit the models

class TaskForm(forms.ModelForm):
    class Meta:
        model=Task # we are saying explicitly take the model Task form the model
        #fields="__all__" include all
        fields=['content','deadline','tags'] #customizing
        widgets={
            'deadline':forms.DateTimeInput(attrs={"type":"datetime-local"})
        }
class TagForm(forms.ModelForm):
    class Meta:
        model=Tag
        fields=['name']
