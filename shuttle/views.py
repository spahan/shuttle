from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponseRedirect

from django.core.mail import send_mail



from datetime import datetime
from .models import Shuttle,Passenger,Driver
from .forms import PassengerForm

# Create your views here.

def index(request):
    future_shuttle_list = Shuttle.objects.filter(departure__gt=datetime.now()).order_by('departure')[:10]
    return render(request, 'shuttle/index.html', { 'future_shuttle_list':future_shuttle_list,'session': request.session, 'show_details': False})

def detail(request, shuttle_id):
    shuttle = get_object_or_404(Shuttle, pk=shuttle_id)
    form = PassengerForm()
    return render(request, 'shuttle/detail.html', { 'shuttle':shuttle, 'form':form, 'session': request.session, 'show_details': True })

def add_passenger(request, shuttle_id):
    if request.method == 'POST':
        shuttle = get_object_or_404(Shuttle, pk=shuttle_id)
        if shuttle.car != None and shuttle.car.space > shuttle.passenger_set.count():
            form = PassengerForm(request.POST)
            if form.is_valid():
                passenger = Passenger(nick=form.cleaned_data['nick'], mail=form.cleaned_data['email'], shuttle=shuttle)
                passenger.save()
                if form.cleaned_data['email']:
                    send_mail('Sign Up for Shuttle {}'.format(shuttle),"Ohai,\n\nYou have been signed up to the shuttle {}.\nTo remove yourself from the Shuttle open {}\n\nHave a nice day".format(shuttle, request.build_absolute_uri(reverse('shuttle:remove', args=[shuttle.id,passenger.token]))), 'shuttle@spahan.ch', [ form.cleaned_data['email'] ], fail_silently=False)
                return HttpResponseRedirect(reverse('shuttle:detail', args=(shuttle.id,)))
        else:
            return HttpResponseRedirect(reverse('shuttle:index'))
    else:
        form = PassengerForm()

    #return HttpResponseRedirect(reverse('shuttle:detail', args=(shuttle.id,)))
    return render(request, 'shuttle/detail.html', { 'shuttle':shuttle, 'form':form })

def remove_passenger(request, shuttle_id, token):
    shuttle = get_object_or_404(Shuttle, pk=shuttle_id)
    passenger = get_object_or_404(Passenger, token=token)
    passenger.delete()
    return HttpResponseRedirect(reverse('shuttle:index'))

from django.http import HttpResponse
def add_driver(request, shuttle_id, driver_id):
    shuttle = get_object_or_404(Shuttle, pk=shuttle_id)
    driver = get_object_or_404(Driver, pk=driver_id)
    shuttle.driver = driver
    shuttle.save()
    return HttpResponseRedirect(reverse('shuttle:detail', args=(shuttle.id,)))

def login(request):
    if request.method == 'GET':
        driver = get_object_or_404(Driver, token=request.GET['token'])
        request.session['driver_id'] = driver.id
    else:
        try:
            del request.session['driver_id']
        except KeyError:
            pass
    return HttpResponseRedirect(reverse('shuttle:index'))

def logout(request):
    try:
        del request.session['driver_id']
    except KeyError:
        pass
    return HttpResponseRedirect(reverse('shuttle:index'))
