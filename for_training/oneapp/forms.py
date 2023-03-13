from django import forms
from .models import Exercise, Set, Day
from django.forms import inlineformset_factory
from django.forms.models import BaseInlineFormSet


""" class DayForm(forms.ModelForm):

    class Meta:
        model = Day
        fields = ('pub_date', 'weight_body')

    def clean_weight_body(self):
        data = float(self.cleaned_data['weight_body'])
        if data < 20:
            raise forms.ValidationError('Вес может быть от 20 до 300 кг.')
        return data


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


ExerciseFormSet = inlineformset_factory(
                                        Day,
                                        Exercise,
                                        fields=('group', 'name_exercise'),
                                        can_delete=False,
                                        form=ExerciseForm, extra=1)


class SetForm(forms.ModelForm):

    class Meta:
        model = Set
        fields = ('weight', 'reps')

    def clean_weight(self):
        data = self.cleaned_data['weight']
        if data < 0 or data > 700:
            raise forms.ValidationError('Вес может быть от 0 до 700 кг.')
        return data """


SetFormSet = inlineformset_factory(Exercise,
                                   Set,
                                   fields=('weight', 'reps'),
                                   can_delete=False,
                                   #form=SetForm,
                                   extra=1)


class BaseExerciseFormset(BaseInlineFormSet):
    def add_fields(self, form, index):
        super(BaseExerciseFormset, self).add_fields(form, index)

        form.nested = SetFormSet(
                                 instance=form.instance,
                                 data=form.data if form.is_bound else None,
                                 files=form.files if form.is_bound else None,
                                 prefix='address-%s-%s' % (
                                    form.prefix,
                                    SetFormSet.get_default_prefix()),
                                 )

        def is_valid(self):
            result = super(BaseExerciseFormset, self).is_valid()

            if self.is_bound:
                for form in self.forms:
                    if hasattr(form, 'nested'):
                        result = result and form.nested.is_valid()

            return result

        def save(self, commit=True):
            result = super(BaseExerciseFormset, self).save(commit=commit)

            for form in self.forms:
                if hasattr(form, 'nested'):
                    if not self._should_delete_form(form):
                        form.nested.save(commit=commit)

            return result


ExerciseFormSet = inlineformset_factory(
                                        Day,
                                        Exercise,
                                        fields=('group', 'name_exercise'),
                                        can_delete=False,
                                        formset=BaseExerciseFormset,
                                        extra=1)
