from .models import Evenement

def event(request):
    context = {}
    if 'evennement' in request:
        context['evennement'] = request['evennement']
    return context