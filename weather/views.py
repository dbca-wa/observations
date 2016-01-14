from __future__ import absolute_import, unicode_literals

from .models import WeatherStation

from django.shortcuts import render_to_response

def index (request):
    return render_to_response("index.html", {
        "stations": WeatherStation.objects.all()
    })

def weatherstation (request, station):
    return render_to_response("station.html", {
        "station": WeatherStation.objects.get(id=station)
    })

