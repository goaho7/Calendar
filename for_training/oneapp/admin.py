from django.contrib import admin
from .models import Exercise, Set, Group, NameExercise, Day

admin.site.register(Group)
admin.site.register(NameExercise)
admin.site.register(Exercise)
admin.site.register(Set)
admin.site.register(Day)
