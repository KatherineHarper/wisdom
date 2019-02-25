from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
import logging

from .models import Pet

def home(request):
    pets = Pet.objects.all()
    return render(request, 'home.html', {'pets': pets, 'user': request.user})

@login_required
def pet_detail(request, id):
    try:
        pet = Pet.objects.get(id=id)
    except Pet.DoesNotExist:
        raise Http404('Pet not found')
    return render(request, 'pet_detail.html', {'pet': pet})

def login(request):
    return render(request, 'login.html')

def logout(request):
    django_logout(request)
    return render(request, 'logged_out.html')

log = logging.getLogger(__name__)

@login_required
def reset_request(request):
    # some code here to send an email - not relevant to this assessment.
    log.warning('Password change request made for {name}'.format(
        name = request.user.username
    ))
    return render(request, 'reset_request.html', {'user': request.user})
