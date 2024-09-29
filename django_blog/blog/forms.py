from django import forms
from taggit.forms import TagWidget
from django.utils.text import slugify
from .models import Profile, Post, Comment, Tag


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'bio', 'picture')

class CreatePostForm(forms.ModelForm):
    tags = forms.CharField(required=False, widget=TagWidget())

    class Meta:
        model = Post
        fields = ('title', 'content')
        widgets = {
            'tags': TagWidget
        }

    def clean_tags(self):
        tags = self.cleaned_data['tags']
        existing_tags = Tag.objects.filter(name__in=[slugify(tags) for tag in tags.split(',')])
        new_tags = [tag for tag in tags.split(',') if slugify(tag) not in existing_tags.values_list('name', flat=True)]
        return ', '.join(existing_tags.values_list('name', flat=True) + new_tags)

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'})

        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)