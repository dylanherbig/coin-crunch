from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.eyJ1IjoiZGhwMnJwZSIsImEiOiJjbDI0enpvbnowMHc2M2JvNTdkZnMxNjViIn0.jMXoAk9xqZfs_-4U_bQpDg'
    return render(request, 'mapPage.html', 
                  { 'mapbox_access_token': mapbox_access_token })