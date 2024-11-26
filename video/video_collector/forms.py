from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['name', 'url', 'notes']

# form for searching feature, it is not related to the database
class SearchForm(forms.Form):
        search_term = forms.CharField()