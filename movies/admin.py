from django.contrib import admin
from movies.models import movies_post, FamousLine

# Register your models here.
@admin.register(movies_post)
class postAdmin(admin.ModelAdmin):
    pass

@admin.register(FamousLine)
class LineAdmin(admin.ModelAdmin):
    pass