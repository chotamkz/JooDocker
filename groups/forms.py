from django.forms import ModelForm
from .models import Group


class GroupFrom(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
