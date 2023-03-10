from django.utils import timezone


def data(request):
    return {
        'data': timezone.now()
    }
