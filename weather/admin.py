from django.contrib.gis import admin
from weather.models import WeatherStation, Location

class LocationAdmin(admin.GeoModelAdmin):
    openlayers_url = "//cdn.jsdelivr.net/openlayers/2.13.1/OpenLayers.js"

class WeatherStationAdmin(admin.ModelAdmin):
    pass

site = admin.AdminSite()

site.register(Location, LocationAdmin)
site.register(WeatherStation, WeatherStationAdmin)
