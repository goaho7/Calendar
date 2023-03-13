from django.shortcuts import render
from .forms import SetFormSet, ExerciseFormSet
from .models import Exercise, Day
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


""" @csrf_exempt
def index(request):
    exercise_form = ExerciseForm()
    day_form = DayForm()
    set_form = SetForm()
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        group = get_object_or_404(Group, id=request.POST.get('group'))
        exercise_form.fields['name_exercise'].queryset = group.exercises.all()
    else:
        group = Group.objects.get(title='Спина')
        exercise_form.fields['name_exercise'].queryset = group.exercises.all()

    print('*'*150)
    print(request.POST)
    context = {
        'exercise_form': exercise_form,
        'day_form': day_form,
        'set_form': set_form,
    }
    return render(request, 'oneapp/index.html', context) """

""" elif request.method == 'POST':
        exercise_formset = ExerciseFormSet(request.POST, instance=day)
        if exercise_formset.is_valid():
            exercise_formset.save() """


def index(request):
    print('*'*150)
    print(request.method)
    day = Day.objects.get(author=1)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form_total = int(request.POST.get('form_total', 1))
        exercise_formset = ExerciseFormSet(instance=day)
    elif request.method == 'POST':
        exercise_formset = ExerciseFormSet(request.POST, instance=day)
        if exercise_formset.is_valid():
            exercise_formset.save()
    else:
        exercise_formset = ExerciseFormSet(queryset=Exercise.objects.none(), instance=day)

    context = {
        'exercise_formset': exercise_formset,
    }
    return render(request, 'oneapp/index.html', context)


""" class DayAddView(TemplateView):
    template_name = 'oneapp/index.html'

    def get(self, *args, **kwargs):
        day = Day.objects.get(author=1)
        ExerciseFormSet = inlineformset_factory(Day, Exercise, fields=('group', 'name_exercise'), can_delete=False, form=ExerciseForm, extra=1)
        formset = ExerciseFormSet(queryset=Exercise.objects.none(), instance=day)
        return self.render_to_response({'formset': formset})

    def post(self, *args, **kwargs):
        day = Day.objects.get(author=1)
        ExerciseFormSet = inlineformset_factory(Day, Exercise, fields=('group', 'name_exercise'), can_delete=False, form=ExerciseForm, extra=1)
        formset = ExerciseFormSet(data=self.request.POST, instance=day)

        return self.render_to_response({'formset': formset}) """
