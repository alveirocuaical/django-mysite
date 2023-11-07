from django import forms

class CreateNewTaskForm(forms.Form):
    title = forms.CharField(label="Title", max_length=200)
    description = forms.CharField(label= 'Descripcion de la tarea ', widget=forms.Textarea)
    
    
class CreateProjectForm(forms.Form):
    name = forms.CharField(label="Name", max_length=200, widget=forms.TextInput({'class': 'input'}))
    