from django import forms

class TodoForm(forms.Form):
    tarefa = forms.CharField(label='Tarefa', max_length=100)