from django import forms

from .models import Todo
class PersonForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100, required=True)
    age = forms.IntegerField(label='Your Age')
    job = forms.CharField(label='Your Job', max_length=100, required=False)


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'done', 'deadline', 'priority']

        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        } 