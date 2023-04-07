from django import forms
from .models import Exercise, Set, Day
from django.forms import inlineformset_factory
from django.forms.models import BaseInlineFormSet


class ExerciseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name_exercise'].empty_label = None
        self.fields['group'].empty_label = None

    class Meta:
        model = Exercise
        fields = ('group', 'name_exercise')


class SetForm(forms.ModelForm):

    class Meta:
        model = Set
        fields = ('weight', 'reps')

    def clean_weight(self):
        data = self.cleaned_data['weight']
        if data < 0 or data > 1000:
            raise forms.ValidationError('Вес может быть от 0 до 1000 кг.')
        return data

    def clean_reps(self):
        data = self.cleaned_data['reps']
        if data < 0 or data > 1000:
            raise forms.ValidationError('Повторений быть от 0 до 1000.')
        return data


SetFormSet = inlineformset_factory(
    Exercise, Set, form=SetForm, extra=1, can_delete=False
)


class ExerciseInlineFormSet(BaseInlineFormSet):
    def add_fields(self, form, index):
        super().add_fields(form, index)
        form.sets = SetFormSet(
            instance=form.instance, data=form.data if form.is_bound else None,
            prefix='%s-%s' % (form.prefix, SetFormSet.get_default_prefix())
        )

    def is_valid(self):
        result = super(ExerciseInlineFormSet, self).is_valid()
        if self.is_bound:
            for exercise in self.forms:
                result = result and exercise.sets.is_valid()
        return result

    def save(self, commit=True):
        result = super(ExerciseInlineFormSet, self).save(commit=commit)

        for exercise in self.forms:
            if hasattr(exercise, 'sets'):
                exercise.sets.save(commit=commit)

        return result


ExerciseFormSet = inlineformset_factory(
    Day, Exercise, form=ExerciseForm, extra=1,
    can_delete=False, formset=ExerciseInlineFormSet
)


class DayForm(forms.ModelForm):

    class Meta:
        model = Day
        fields = ('pub_date', 'weight_body')

    def clean_weight_body(self):
        data = float(self.cleaned_data['weight_body'])
        if (data < 20 or data > 500) and data != '':
            raise forms.ValidationError(
                'Вес не должен быть меньше 20 кг и больше 500 кг.'
            )
        return data
