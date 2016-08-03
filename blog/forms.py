from django import forms
from .models import Post, Comment, Tag


class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags', 'photo', 'lnglat', 'created_at', 'test_field',]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
