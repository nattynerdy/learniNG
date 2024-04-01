from django.contrib import admin
from content import models as content
from courses import models as courses
from tags import models as tags

# Register your models here.
@admin.register(content.Content)
class contentAdmin(admin.ModelAdmin):
    pass

@admin.register(courses.Course)
class courseAdmin(admin.ModelAdmin):
    pass

@admin.register(tags.Tag)
class tagAdmin(admin.ModelAdmin):
    pass
