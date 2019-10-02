from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string

from datetime import datetime
from .models import Shuttle,Passenger,Driver
from .forms import PassengerForm

# Create your views here.

def index(request):
    shuttles = Shuttle.objects.filter(departure__gt=datetime.now()).order_by('departure')
    if not 'driver_id' in request.session:
        shuttles = shuttles.filter(driver__isnull = False)
    return render(request, 'shuttle/index.html', { 'shuttles': shuttles, 'show_details': False})

def detail(request, shuttle_id):
    shuttle = get_object_or_404(Shuttle, pk=shuttle_id)
    form = PassengerForm()
    return render(request, 'shuttle/detail.html', { 'shuttle':shuttle, 'form':form, 'show_details': True })

def add_passenger(request, shuttle_id):
    if request.method == 'POST':
        shuttle = get_object_or_404(Shuttle, pk=shuttle_id)
        form = PassengerForm(request.POST)
        if form.is_valid():
            if shuttle.car == None or shuttle.driver == None:
                messages.info(request, 'You can not sign up for this shuttle as it does not have a driver or car assigned. Please try again later')
                return HttpResponseRedirect(reverse('shuttle:index'))
            if shuttle.passenger_set.count() >= shuttle.car.space:
                message.info(request, 'Sorry, this shuttle is already full. Try another one')
                return HttpResponseRedirect(reverse('shuttle:index'))
            passenger = Passenger(nick=form.cleaned_data['nick'], mail=form.cleaned_data['email'], shuttle=shuttle)
            passenger.save()
            messages.success(request, 'You have signed up for {}'.format(shuttle))
            if form.cleaned_data['email']:
                send_mail('Sign Up for Shuttle {}'.format(shuttle), render_to_string('shuttle/passenger.txt', {'shuttle':shuttle, 'passenger':passenger, 'request':request}), 'shuttle@spahan.ch', [ form.cleaned_data['email'] ], fail_silently=True)
        else:
            messages.warning(request,'There is a Problem with your input:' + ''.join(['{}: {}'.format(key, error) for key in form.errors.keys() for error in form.errors[key]]))
    return HttpResponseRedirect(reverse('shuttle:detail', args=(shuttle.id,)))

def remove_passenger(request, shuttle_id, token):
    shuttle = get_object_or_404(Shuttle, pk=shuttle_id)
    passenger = get_object_or_404(Passenger, token=token)
    passenger.delete()
    messages.success(request, 'You have been signed off from {}'.format(shuttle))
    return HttpResponseRedirect(reverse('shuttle:index'))

def add_driver(request, shuttle_id, driver_id):
    shuttle = get_object_or_404(Shuttle, pk=shuttle_id)
    driver = get_object_or_404(Driver, pk=driver_id)
    shuttle.driver = driver
    shuttle.save()
    messages.success(request, 'You are now the driver for {}'.format(shuttle))
    send_mail('Driver Information for {}'.format(shuttle), render_to_string('shuttle/driver.txt', {'shuttle':shuttle, 'driver': driver, 'request':request}), 'shuttle@spahan.ch', [ driver.mail ], fail_silently=True)
    return HttpResponseRedirect(reverse('shuttle:detail', args=(shuttle.id,)))

def login(request):
    if request.method == 'GET':
        driver = get_object_or_404(Driver, token=request.GET['token'])
        request.session['driver_id'] = driver.id
        messages.success(request, 'You are logged in as {} now'.format(driver.nick))
    else:
        messages.info(request, 'HAXXOR!')
    return HttpResponseRedirect(reverse('shuttle:index'))

def logout(request):
    try:
        del request.session['driver_id']
    except KeyError:
        pass
    return HttpResponseRedirect(reverse('shuttle:index'))
