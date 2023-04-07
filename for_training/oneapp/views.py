from django.shortcuts import render
from .forms import ExerciseFormSet, DayForm
from .models import Day
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


@csrf_exempt
def index(request):

    if request.method == 'POST':
        dayform = DayForm(request.POST)
        if dayform.is_valid():
            day, _ = Day.objects.get_or_create(
                pub_date=request.POST['pub_date'],
                author=request.user,
            )
            if request.POST['weight_body']:
                day.weight_body = request.POST['weight_body']
            day.save()

            exerciseformset = ExerciseFormSet(request.POST, instance=day)

            if exerciseformset.is_valid():
                exerciseformset.save()
    else:
        dayform = DayForm()
        exerciseformset = ExerciseFormSet()

    context = {
        'dayform': dayform,
        'exerciseformset': exerciseformset,
    }
    return render(request, 'oneapp/index.html', context)




#if request.headers.get('x-requested-with') == 'XMLHttpRequest':
#    form_total = int(request.POST.get('form_total', 1))
#    exercise_formset = ExerciseFormSet(instance=day)
