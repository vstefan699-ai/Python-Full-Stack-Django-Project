from django.contrib import admin
from .models import WorkoutPlan, Exercise, WorkoutLog, UserProfile

# Register your models here
admin.site.register(WorkoutPlan)
admin.site.register(Exercise)
admin.site.register(WorkoutLog)
admin.site.register(UserProfile)