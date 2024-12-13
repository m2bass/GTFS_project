from django.shortcuts import render, redirect, get_object_or_404
from .models import Trip, Stop, StopTime
from .forms import TripForm, StopForm, StopTimeForm

def index(request):
    return render(request, 'index.html')  # Render the index.html page

# Part 4: Create Operation
def create_trip(request):
    if request.method == 'POST':
        trip_form = TripForm(request.POST)
        stop_form = StopForm(request.POST)
        stop_time_form = StopTimeForm(request.POST)

        if trip_form.is_valid() and stop_form.is_valid() and stop_time_form.is_valid():
            trip = trip_form.save()
            stop = stop_form.save()
            stop_time = stop_time_form.save(commit=False)
            stop_time.trip = trip
            stop_time.stop = stop
            stop_time.save()

            # Redirect to the trip list after saving the trip
            return redirect('trip_list')  # Ensure 'trip_list' is the correct URL name

    else:
        trip_form = TripForm()
        stop_form = StopForm()
        stop_time_form = StopTimeForm()

    return render(request, 'rideshare/trip_form.html', {
        'trip_form': trip_form,
        'stop_form': stop_form,
        'stop_time_form': stop_time_form
    })


# Part 2: Read Operation (Listing trips)
def trip_list(request):
    trips = Trip.objects.all()
    print(trips) 
    return render(request, 'rideshare/trip_list.html', {'trips': trips})

# Part 4: Update Operation
def update_trip(request, pk):
    trip = get_object_or_404(Trip, pk=pk)  # Retrieve the trip or raise 404 if not found
    stop_time = StopTime.objects.filter(trip=trip).first()  # Get the first StopTime related to the trip

    if request.method == 'POST':
        trip_form = TripForm(request.POST, instance=trip)
        stop_form = StopForm(request.POST, instance=trip.stop)  # Pre-populate the StopForm with existing Stop
        stop_time_form = StopTimeForm(request.POST, instance=stop_time)  # Update StopTime if it exists

        if trip_form.is_valid() and stop_form.is_valid() and stop_time_form.is_valid():
            trip_form.save()  # Save the Trip updates
            stop = stop_form.save()  # Update or create a new Stop if needed
            stop_time = stop_time_form.save(commit=False)
            stop_time.trip = trip  # Ensure StopTime is still linked to the updated trip
            stop_time.stop = stop  # Ensure StopTime is still linked to the updated Stop
            stop_time.save()  # Save the StopTime
            return redirect('trip_list')  # Ensure the URL name matches the correct view
    else:
        trip_form = TripForm(instance=trip)
        stop_form = StopForm(instance=trip.stop)  # Pre-populate with existing Stop data
        stop_time_form = StopTimeForm(instance=stop_time)  # Pre-populate with existing StopTime data if any

    return render(request, 'rideshare/trip_form.html', {
        'trip_form': trip_form,
        'stop_form': stop_form,
        'stop_time_form': stop_time_form
    })


# Part 4: Delete Operation
def confirm_delete_trip(request, pk):
    trip = get_object_or_404(Trip, pk=pk)  # Retrieve the trip or raise 404 if not found

    if request.method == 'POST':
        trip.delete()  # Delete the trip object
        return redirect('trip_list')  # Redirect to the trip list after deletion

    return render(request, 'rideshare/trips_confirm_delete.html', {'trip': trip}) # Confirmation template

