from django import forms
from .models import Trip, Stop, StopTime, Route, Agency

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['route', 'start_time', 'end_time']  # Adding route as ForeignKey field
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class StopForm(forms.ModelForm):
    class Meta:
        model = Stop
        fields = ['stop_id', 'stop_name', 'stop_location']
        widgets = {
            'stop_location': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_stop_id(self):
        stop_id = self.cleaned_data.get('stop_id')
        if Stop.objects.filter(stop_id=stop_id).exists():
            raise forms.ValidationError("This Stop ID is already in use.", code='invalid')
        return stop_id

class StopTimeForm(forms.ModelForm):
    class Meta:
        model = StopTime
        fields = ['trip', 'stop', 'arrival_time', 'departure_time']  # Including trip and stop as ForeignKey fields
        widgets = {
            'arrival_time': forms.TimeInput(attrs={'type': 'time'}),
            'departure_time': forms.TimeInput(attrs={'type': 'time'}),
        }


