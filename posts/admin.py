from django.contrib import admin
from posts.models import Post, Comment, HashTag
from django.db.models import ManyToManyField
from django.forms import CheckboxSelectMultiple

# Register your models here.
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class LikeUserInline(admin.TabularInline):
    model = Post.like_users.through
    verbose_name = "좋아요 한 사용자"
    verbose_name_plural = f"{verbose_name} 목록"
    extra = 1

    def has_change_permission(self, request, obj = None):
        return False

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "review",
        "short_comment",
        "created",
    ]
    inlines = [
        CommentInline,
        LikeUserInline,
    ]

    formfield_overrides = {ManyToManyField : {"widget" : CheckboxSelectMultiple}}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "post",
        "content",
        "created",
    ]

@admin.register(HashTag)
class HashTagAdmin(admin.ModelAdmin):
    pass