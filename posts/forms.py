from django import forms
from posts.models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # tag는 부가적인 요소이므로 fields에 함께 묶지 않는다.
        fields = [
            "movies",
            "review",
            "short_comment",
        ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "post",
            "content"
        ]