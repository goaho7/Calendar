from django.contrib import admin
from .models import Exercise, Set, Group, NameExercise, Day


class SetAdmin(admin.ModelAdmin):
    list_display = ('id', 'weight', 'reps', 'exercise')


class DayAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'pub_date', 'weight_body')


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('id', 'day', 'group', 'name_exercise', 'comment')


admin.site.register(Group)
admin.site.register(NameExercise)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Set, SetAdmin)
admin.site.register(Day, DayAdmin)
