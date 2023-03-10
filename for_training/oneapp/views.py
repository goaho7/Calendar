from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ExerciseForm, DayForm, SetForm
from .models import Exercise, NameExercise, Group
from django.views.generic.edit import CreateView
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
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
    return render(request, 'oneapp/index.html', context)
