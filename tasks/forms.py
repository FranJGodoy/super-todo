from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['nombre', 'descripcion', 'completada'] # Los campos del modelo

        # Le decimos a Django qué clases de CSS y placeholders ponerle al HTML
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Nombre'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control mb-2', 'placeholder': 'Descripción'}),
            'completada': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

        labels = {
            'completada': '¿Tarea finalizada?',
        }
