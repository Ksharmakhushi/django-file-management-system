from django import forms
from .models import File_uploading

class FileManagementForm(forms.ModelForm):

    class Meta:
        model = File_uploading
        fields = '__all__'