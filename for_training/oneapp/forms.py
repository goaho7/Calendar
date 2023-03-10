from django import forms
from .models import Exercise, Group, NameExercise, Set, Day
from django.forms import inlineformset_factory


class ExerciseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name_exercise'].empty_label = None
        self.fields['group'].empty_label = None

    class Meta:
        model = Exercise
        fields = ('group', 'name_exercise')
        widgets = {
            'comment': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
        }


class DayForm(forms.ModelForm):

    class Meta:
        model = Day
        fields = ('pub_date', 'weight_body')


class SetForm(forms.ModelForm):

    class Meta:
        model = Set
        fields = ('weight', 'reps')
