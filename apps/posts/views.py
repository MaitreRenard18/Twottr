from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import get_sample


@login_required(login_url='/login')
def home(request):
    return render(request, 'timeline.html', {"twots": get_sample(10)})
