from django.forms import ModelForm
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        # fields = ['title', 'slug', 'tags', 'description', 'demo_link', 'source_link']
