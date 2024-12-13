from django.db import models


# Agency model
class Agency(models.Model):
    agency_id = models.CharField(max_length=50, primary_key=True)
    agency_name = models.CharField(max_length=100)

    def __str__(self):
        return self.agency_name

# Routes model
class Route(models.Model):
    route_id = models.CharField(max_length=50, primary_key=True)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    route_long_name = models.CharField(max_length=100)

    def __str__(self):
        return self.route_long_name

    class Meta:
        verbose_name = "Route"
        verbose_name_plural = "Routes"

# Trips model
class Trip(models.Model):
    name = models.CharField(max_length=100, default="Unknown Trip")
    stop = models.ForeignKey('Stop', on_delete=models.CASCADE, null=True, blank=True)
    route = models.ForeignKey('Route', on_delete=models.CASCADE)
    start_time = models.DateTimeField() 
    end_time = models.DateTimeField()    

    def __str__(self):
        return f"Trip on {self.route.route_long_name} from {self.start_time} to {self.end_time}"

# Stops model
class Stop(models.Model):
    stop_id = models.CharField(max_length=50, primary_key=True)
    stop_name = models.CharField(max_length=100)
    stop_location = models.CharField(max_length=255, null=True, blank=True)  # Add this field if needed


# StopTimes model
class StopTime(models.Model):
    stop_time_id = models.AutoField(primary_key=True)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE)
    arrival_time = models.TimeField(null=True, blank=True)
    departure_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.trip} at {self.stop.stop_name} ({self.arrival_time} - {self.departure_time})"


