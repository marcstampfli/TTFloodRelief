from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from .models import Location
from django.core.paginator import Paginator
from .forms import GetListed
from django.views.generic import CreateView


def index(request):
    locations = Location.objects.all()
    total_locations = Location.objects.all()

    paginator = Paginator(locations, 6)
    page = request.GET.get('page')

    locations = paginator.get_page(page)
    return render(request, 'index.html', {
        'locations': locations,
        'total_locations': total_locations
    })


def detail(request, location_id):
    location_id = get_object_or_404(Location, id=location_id)
    return render(request, 'detail.html', {
        'location_id': location_id
    })


def get_listed(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = GetListed(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/locations/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = GetListed()

    return render(request, 'get_listed.html', {'form': form})


class LocationCreateView(CreateView):
    model = Location
    fields = ('name', 'description', 'address1', 'address2')
