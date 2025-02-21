from django.contrib import admin
from .models import User
from .models import Project
from .models import Task
from .models import Sprint

admin.site.register(User)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Sprint)