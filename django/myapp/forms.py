from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description']

        widgets = {
            'title':forms.TextInput(attrs={'class':'rounded-xl py-2 px-3 text-black'}),
            'description': forms.Textarea(attrs={'class':'rounded-xl py-2 px-3 text-black h-[200px]'})
        }